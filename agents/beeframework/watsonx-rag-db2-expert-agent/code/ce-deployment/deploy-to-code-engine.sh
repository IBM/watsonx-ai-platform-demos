#
# Copyright 2024 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#!/bin/bash

# **************** Global variables
export HOME_PATH=$(pwd)
export CONTAINER_RUNTIME=podman

# IBM Cloud - variables
source "$HOME_PATH"/.env
# Application - variables
source "$HOME_PATH"/../.env

# Optional to change
export CODEENGINE_CR_ACCESS_NAME=$CR
export CODEENGINE_CR_SERVER_NAME=$CR

export CODEENGINE_APP_IMAGE_URL=""
export CODEENGINE_APP_CPU_CONFIG=1
export CODEENGINE_APP_MEMORY_CONFIG=2G
export CODEENGINE_APP_MAX_SCALE=1
export CODEENGINE_APP_MIN_SCALE=0
export CODEENGINE_APP_PORT=8080
export CODEENGINE_PROJECT_NAMESPACE=""

export COMMIT_ID=""
export DOCKERFILE_NAME="Dockerfile.podman"
export FOLDERNAME=""

# **********************************************************************************
# Functions definition
# **********************************************************************************

function check_podman () {
    ERROR=$(${CONTAINER_RUNTIME} ps 2>&1)
    RESULT=$(echo $ERROR | grep 'Cannot' | awk '{print $1;}')
    VERIFY="Cannot"
    if [ "$RESULT" == "$VERIFY" ]; then
        echo "Podman is not running. Stop script execution."
        exit 1 
    fi
}

function login_to_ibm_cloud () {
    
    echo ""
    echo "*********************"
    echo "loginIBMCloud"
    echo "*********************"
    echo ""

    ibmcloud login --apikey $IBM_CLOUD_API_KEY 
    ibmcloud target -r $IBM_CLOUD_REGION
    ibmcloud target -g $IBM_CLOUD_RESOURCE_GROUP
}

function setup_ce_project() {
  echo "**********************************"
  echo " Using following project: $CODEENGINE_PROJECT_NAME" 
  echo "**********************************"

  RESULT=$(ibmcloud ce project get --name $CODEENGINE_PROJECT_NAME | grep "Status" |  awk '{print $2;}')
  if [[ $RESULT == "active" ]]; then
        echo "*** The project $PROJECT_NAME exists."
        ibmcloud ce project select -n $CODEENGINE_PROJECT_NAME
  else
        ibmcloud ce project create --name $CODEENGINE_PROJECT_NAME 
        ibmcloud ce project select -n $CODEENGINE_PROJECT_NAME
  fi

  #to use the kubectl commands
  ibmcloud ce project select -n $CODEENGINE_PROJECT_NAME --kubecfg
  
  CODEENGINE_PROJECT_NAMESPACE=$(ibmcloud ce project get --name $CODEENGINE_PROJECT_NAME --output json | grep "namespace" | awk '{print $2;}' | sed 's/"//g' | sed 's/,//g')
  echo "Code Engine project namespace: $CODEENGINE_PROJECT_NAMESPACE"
  kubectl get pods -n $CODEENGINE_PROJECT_NAMESPACE
}

function build_and_push_container () {
  
    # 1. Get commit id
    export COMMIT_ID=$(git rev-parse HEAD)
    export CI_TAG=$COMMIT_ID

    # 2. Create container image URL
    export CODEENGINE_APP_IMAGE_URL="$CR/$CR_REPOSITORY/$CI_NAME:$CI_TAG"
    
    echo "**********************************"
    echo " Building: $CODEENGINE_APP_IMAGE_URL" 
    echo "**********************************"

    # 3. Build container image
    echo "****** BUILD *********"
    cd "$HOME_PATH"/..
    ${CONTAINER_RUNTIME} build --platform linux/amd64 -f "$HOME_PATH"/../"$DOCKERFILE_NAME" -t "$CODEENGINE_APP_IMAGE_URL" .
    cd "$HOME_PATH"
    
    # 4. Login to  IBM Cloud Container Registry
    ibmcloud cr namespace-list -v
    ibmcloud cr image-list
    rm $HOME/.docker/config.json
    ibmcloud cr login --client ${CONTAINER_RUNTIME}
    
    # 5. In case the IBM Cloud resource group for the IBM Container Registry is different, the automation changes the IBM Cloud target for the resource group.
    ERROR=$(ibmcloud target -g $CR_RESOURCE_GROUP 2>&1)
    RESULT=$(echo $ERROR | grep 'FAILED' | awk '{print $1;}')
    
    VERIFY="FAILED"
    if [ "$RESULT" == "$VERIFY" ]; then
        echo "Can't set to resource group: ($CR_RESOURCE_GROUP) I move on with the existing resource group."
    fi

    # 6. Set to the right container registry region
    ibmcloud cr region-set $CR_REGION

    # 7. Create a new namespace; if the namespace doesn't exists
    CURR_CONTAINER_NAMESPACE=$(ibmcloud cr namespace-list -v | grep $CR_REPOSITORY | awk '{print $1;}')
    if [ "$CR_REPOSITORY" != "$CURR_CONTAINER_NAMESPACE" ]; then
        ibmcloud cr namespace-add $CR_REPOSITORY
    fi

    # 8. Create new container image if it doesn't exists
    CURR_CONTAINER_IMAGE=$(ibmcloud cr image-list | grep $CI_TAG | awk '{print $2;}')
    if [ "$CI_TAG" != "$CURR_CONTAINER_IMAGE" ]; then
        ${CONTAINER_RUNTIME} push "$CODEENGINE_APP_IMAGE_URL"
    else
        echo "Container exists: ($CODEENGINE_APP_IMAGE_URL)"
    fi

    # 9. Set back to the right IBM Cloud resource group, in case the resource group was changed
    ibmcloud target -g $IBM_CLOUD_RESOURCE_GROUP

}

function setup_ce_container_registry_access() {

    RESULT=$(ibmcloud ce registry get --name ${CODEENGINE_CR_ACCESS_NAME} --output  jsonpath='{.metadata.name}')
    if [[ $RESULT == $CODEENGINE_CR_ACCESS_NAME ]]; then
        echo "*** The ce container registry ${CODEENGINE_CR_ACCESS_NAME} for the ${CODEENGINE_PROJECT_NAME} exists."
    else
        echo "*** Create new container registry assess: ${CODEENGINE_CR_ACCESS_NAME} in project ${CODEENGINE_PROJECT_NAME}."
        echo "${CODEENGINE_CR_ACCESS_NAME}"
        echo "${CODEENGINE_CR_SERVER_NAME}"
        echo "${CODEENGINE_CR_USERNAME}"
        echo "${CODEENGINE_CR_EMAIL}"
        echo "${CODEENGINE_CR_PASSWORD}"
        
        ibmcloud ce registry create --name ${CODEENGINE_CR_ACCESS_NAME} \
                                    --username ${CODEENGINE_CR_USERNAME} \
                                    --password ${CODEENGINE_CR_PASSWORD} \
                                    --server ${CODEENGINE_CR_SERVER_NAME} \
                                    --email ${CODEENGINE_CR_EMAIL}
    fi
}

# **** Kubernetes CLI ****

function kube_information(){

    echo "************************************"
    echo " Kubernetes info '$CODEENGINE_APP_NAME': pods, deployments and configmaps details "
    echo "************************************"
    
    kubectl get pods -n $CODEENGINE_PROJECT_NAMESPACE
    kubectl get deployments -n $CODEENGINE_PROJECT_NAMESPACE
    kubectl get configmaps -n $CODEENGINE_PROJECT_NAMESPACE

}

function kube_pod_log(){

    echo "************************************"
    echo " Kubernetes $CODEENGINE_APP_NAME: log"
    echo "************************************"

    FIND=$CODEENGINE_APP_NAME
    APP_POD=$(kubectl get pod -n $CODEENGINE_PROJECT_NAMESPACE | grep $FIND | awk '{print $1}')
    echo "************************************"
    echo "Show log for the pod: $APP_POD"
    echo "************************************"
    kubectl logs $APP_POD
}

function create_configmap () {
    echo "************************************"
    echo "Create configmap"
    echo "************************************"
    cd  $HOME_PATH

    "/bin/sh" ./generate-configmap-file.sh > ./configmap_values.txt
    ibmcloud ce configmap create --name ${CODEENGINE_CONFIGMAP_NAME} --from-env-file ./configmap_values.txt
}

function deploy_ce_application_configmap () {
    
    # Valid vCPU and memory combinations: https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo
    RESULT=$(ibmcloud ce application get --name "$CODEENGINE_APP_NAME" --output  jsonpath='{.metadata.name}')
    if [[ $RESULT == $CODEENGINE_APP_NAME ]]; then
        echo "*** The ce application $CODEENGINE_APP_NAME for the $CODEENGINE_PROJECT_NAME exists."
        echo "*** Delete application!"
        RESULT=$(ibmcloud ce application delete --name $CODEENGINE_APP_NAME --force)
        VERIFY=$(echo $RESULT | grep OK | awk -F" " '{print $NF}')
        if [[ $VERIFY != "OK" ]]; then
           echo "Error problem to delete the ${CODEENGINE_APP_NAME} application"
           echo "$RESULT"
           echo "The script stops here."
           exit 1
        fi
    fi
    
    echo "*** Create application $CODEENGINE_APP_NAME for the $CODEENGINE_PROJECT_NAME"
    ibmcloud ce application create --name ${CODEENGINE_APP_NAME} \
                                   --image ${CODEENGINE_APP_IMAGE_URL} \
                                   --cpu ${CODEENGINE_APP_CPU_CONFIG} \
                                   --memory ${CODEENGINE_APP_MEMORY_CONFIG} \
                                   --registry-secret ${CODEENGINE_CR_ACCESS_NAME} \
                                   --env-from-configmap ${CODEENGINE_CONFIGMAP_NAME} \
                                   --max-scale $CODEENGINE_APP_MAX_SCALE \
                                   --min-scale $CODEENGINE_APP_MIN_SCALE \
                                   --port $CODEENGINE_APP_PORT
    
    ibmcloud ce application get --name "$CODEENGINE_APP_NAME"
    export CODEENGINE_APP_NAME_URL=$(ibmcloud ce application get --name "$CODEENGINE_APP_NAME" -o url)
    echo "************************************"
    echo "Access the application ${CODEENGINE_APP_NAME} - URL: ${CODEENGINE_APP_NAME_URL}/"
    echo "************************************"

}

function check_parameters () {

    if [ "$ARG_REUSE" == "no_reuse" ]; then
        export REUSE="false"
    else
        if [ "$ARG_REUSE" == "reuse" ]; then
            export REUSE="true"
            echo "Resue configuration: $REUSE"
            echo "Commit ID: $REUSE_REPO_COMMIT_ID"
            echo "Repo URL: $REUSE_REPO_URL"
            echo "Env filename: $REUSE_REPO_ENV_NAME"
        else
            echo "No reuse configuration: $ARG_REUSE"
            export REUSE="false"
        fi    
    fi
}

function verifyDeployment () {

    echo "**********************************"
    echo " Verify deployment: $CODEENGINE_APP_NAME_URL" 
    echo "**********************************"
    
    curl -X GET "${CODEENGINE_APP_NAME_URL}" 
}


#**********************************************************************************
# Execution
# *********************************************************************************

check_podman
login_to_ibm_cloud
check_parameters
build_and_push_container
setup_ce_project
setup_ce_container_registry_access
create_configmap
deploy_ce_application_configmap
kube_information
kube_pod_log
verifyDeployment

cd ${HOME_PATH}
rm ./configmap_values.txt
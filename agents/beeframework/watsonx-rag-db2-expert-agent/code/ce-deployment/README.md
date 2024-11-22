# Automation of deployment of the container to the IBM Cloud Code Engine 

To deploy the example container to `IBM Cloud Code Engine` we need to create and configure the following:

* In an `IBM Cloud Code Engine Project` we need:
    * An `application` to run the container
    * A `configmap` to provide the environment variables for the application
    * A `container image registry to access rights` to access the save container in the `IBM Cloud Container Image Registry`
* `IBM Cloud Container Image Registry` to save the container image

To ensure you don't need to do this manually, we provide automation that takes all the necessary steps.

1. Log in to [IBM Cloud](https://cloud.ibm.com)
2. Build and push the container image to [IBM Cloud Container Image Registry](https://www.ibm.com/products/container-registry) (_the container tag is the last GitHub commit id_)
3. Create a new Code Engine project
4. Create an [IBM Cloud Container Image Registry](https://www.ibm.com/products/container-registry) access for the [IBM Cloud Code Engine](https://www.ibm.com/products/code-engine) project
5. Deploys the **container** to Code Engine
6. Shows the plain `kubectl` information for the containers in the project
7. Shows the plain `kubectl` log information for the first container

## 0. Prerequisites

Need to be installed.

* [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started)
* IBM Cloud Code Engine Plugin
* IBM Cloud Container Registry Plugin
* [`kubectl` command line](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
* [GitHub CLI](https://cli.github.com/)

```sh
ibmcloud update
ibmcloud plugin list
ibmcloud plugin install container-registry
ibmcloud plugin install container-service
ibmcloud plugin install code-engine
```

## 1. Setup

### 1.1. Create the needed `.env` files

* Set the `Code Engine` and `IBM Cloud` environment variables

```sh
cat ./ce-deployment/.env_template >  ./ce-deploment/.env
```

* Ensure you set environment variables for the application

```sh
cat ./code/.env_template >  ./.env
```

* These are the variables you must configure in the created `.env` file.

_Note:_ You must have access rights to the `resource group`, `region`, `code engine service`, `code engine service` in your IBM Cloud account. 

```sh
# IBM Cloud
export IBM_CLOUD_RESOURCE_GROUP=default
export IBM_CLOUD_REGION="us-south"
export IBM_CLOUD_API_KEY=YOUR_IBM_CLOUD_API_KEY

# Code Engine
export CODEENGINE_PROJECT_NAME=rag-agent-demo-project
export CODEENGINE_APP_NAME=rag-agent-demo

# Container registry
export CR_RESOURCE_GROUP=default
export CR_REGION=global
export CR=icr.io
export CR_REPOSITORY=rag-agent-demo-repo
```

## 2. Run the automation

### 2.1. Run the automation

```sh
cd /ce-deployment
bash deploy-to-code-engine.sh
```

### 2.2. Open your `Code Engine` project in the `IBM Cloud Console`

### 2.3. Open your `configmap` defined for your Code Engine application

### 2.4. Remove the `''` entries in your `configmap` and save the changes

### 2.5. Create a new application configuration, reflect the reason for the change in the name, and save the change

### 2.6. Wait until the application instance is restarted to apply the `configmap` changes

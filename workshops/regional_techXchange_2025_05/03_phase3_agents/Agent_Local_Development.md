# Build and deploy an AI Agent in watsonx and IBM Cloud

[`Link to Workshop Home`](../README.md)

**Table of contents**

1. Simplified Architecture for the Agent in watsonx and IBM Cloud
2. Setup
3. Test the given `tools` for the Agent
4. Addional tests for the  given `tools`
5. Run the Agent locally
6. Deploy the Agent
7. Integrate the deployed Agent into a local application

## 1. Simplified Architecture for the Agent in watsonx and IBM Cloud

* Software implementation architecture for an Agent (simplified)

![](./images/agents-03.png)

* Software implementation architecture for an Agent (simplified)

![](./images/agents-02.png)

* Software deployment of an Agent (simplified)

![](./images/agents-04.png)

## 2. Setup

### 2.1. Set up the environment

#### Step 1: Verify the installed Python version

```sh
pyenv versions
pyenv install -l | grep 3.11.9
pyenv install 3.11.9
pyenv global 3.11.9
```

#### Step 2: Install the needed virtual environment

```sh
cd agents/langgraph_implementation
python3.11 -m venv .venv
source ./.venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install poetry
poetry install
poetry add --no-cache traceloop-sdk==0.38.7
```

#### Step 3: Ensure the Python environment  is accessible 

```sh
export PYTHONPATH=$(pwd):${PYTHONPATH}
echo ${PYTHONPATH}
```

#### 2.1.1 Configure the environment

##### Step 1: Configure the `config.toml` file

```sh
cat ./agents/langgraph_implementation/config.toml_template > ./agents/langgraph_implementation/config.toml
```

```sh
[cli.options]
  # If true, cli `invoke` command is trying to use `ai_service.generate_stream` function for local tests, and `ai_service.generate` otherwise.
  # Default: true
  stream = true

  # Path to json file with a complete payload that will be send to proper AI service generate function.
  # Note that, the payload file will be only used when no `query` is provided when running `invoke ` command
  # Default: None
  payload_path = ""

[deployment]
  # One of the below is required.
  # To determine your `api_key`, refer to `IBM Cloud console API keys <https://cloud.ibm.com/iam/apikeys>`_.
  watsonx_apikey = ""
  watsonx_token = ""

  # should follow the format: `https://{REGION}.ml.cloud.ibm.com`
  watsonx_url = ""

  # Deployment space id is required to create deployment with AI service content.
  space_id = "PLACEHOLDER_FOR_YOUR_SPACE_ID"

  # variable, that is populated with last created deployment_id every time when command `watsonx-ai service new` finish successfully
  deployment_id = ""

[deployment.online.parameters]
# during creation of deployment additional parameters can be provided inside `ONLINE` object for further referencing
# please refer to the API docs: https://cloud.ibm.com/apidocs/machine-learning-cp#deployments-create
  model_id = "mistralai/mistral-large"  # underlying model of WatsonxChat
  thread_id = "thread-1" # More info here: https://langchain-ai.github.io/langgraph/how-tos/persistence/
  url = ""  # should follow the format: `https://{REGION}.ml.cloud.ibm.com`

[deployment.software_specification]
  # Name for derived software specification. If not provided, default one is used that will be build based on the package name: "{pkg_name}-sw-spec"
  name = ""

  # Whether to overwrite (delete existing and create new with the same name) watsonx derived software specification
  # Default: false
  overwrite = false

  # The base software specification used to deploy the AI service. The template dependencies will be installed based on the packages included in the selected base software specification
  # Default: "runtime-24.1-py3.11"
  base_sw_spec = "runtime-24.1-py3.11"
```

##### Step 2: Configure the `.env` file 

```sh
cat ./agents/langgraph_implementation/src/langgraph_react_agent/.env_template > ./agents/langgraph_implementation/src/langgraph_react_agent/.env
```

```sh
# watsonx-saas-showcase
export WATSONX_REGION=us-south
export WATSONX_APIKEY=YOUR_KEY
export WATSONX_DEPLOYMENT_ID=YOUR_ID
export WATSONX_DEPLOYMENT_ID_RAG=YOUR_RAG_ID
export WATSONX_DEPLOYMENT_ID_EMAIL=YOUR_EMAIL_ID
export WATSONX_SPACE_ID=YOUR_SPACE_ID

# Common
export WATSONX_PUB_DEPLOYMENT_URL="https://${WATSONX_REGION}.ml.cloud.ibm.com/ml/v4/deployments"
export WATSONX_SOFTWARE_NAME="ai_service"
export WATSONX_INSTANCE_ID=XXX
export WATSONX_URL="https://${WATSONX_REGION}.ml.cloud.ibm.com"
export USER_AGENT="0001"
```

## 3. Test the given `tools` for the Agent

```sh
cd agents/langgraph_implementation
source ./.venv/bin/activate
source ./src/langgraph_react_agent/.env
poetry run pytest -rA tests/
```

## 4. Addional testx for the  given `tools`

```sh
cd agents/langgraph_implementation
source ./.venv/bin/activate
source ./src/langgraph_react_agent/.env
poetry run python tests/debug_request_email_expert.py 
poetry run python tests/debug_request_db2_expert.py 
```

## 5. Run the Agent locally

```sh
cd agents/langgraph_implementation
source ./src/langgraph_react_agent/.env
source ./.venv/bin/activate
poetry run python examples/execute_ai_service_single_agent_locally.py
```

Possible question:

* "Can you please answer the question, 'What is a DB2 routine?' and then send me a mail I can send to a customer?"


## 6. Deploy the Agent

```sh
cd agents/langgraph_implementation
source ./.venv/bin/activate
poetry run python scripts/deploy_single_agent.py
```

* Final output

Copy the `deployment_id` value.

```sh
-----------------------------------------------------------------------------------------------
Successfully finished deployment creation, deployment_id='a76d3649-d836-4e85-862b-b8e356c99b4a'
-----------------------------------------------------------------------------------------------
```

1. Insert the `deployment_id` value in the [`config.toml` file](./agents/langgraph_implementation/config.toml_template)
2. Insert the `deployment_id` value in the [`.env` file](./ui/code/.env_template) for the Streamlit application. If you already have created the file.

## 6.1 Run the local CLI with the deployed Agent

```sh
cd agents/langgraph_implementation
source ./.venv/bin/activate
poetry run python examples/query_existing_deployment.py
```


## 7. Integrate the deployed Agent to a local application

### 7.1 CLI application

Example questions:

1) What is a DB2 routine?
2) Can you please create an answer to the question, 'What is a DB2 routine?' and then provide me with a mail I can send to the customer?

```sh
cd agents/langgraph_implementation
source ./.venv/bin/activate
poetry run python examples/query_existing_deployment.py
```

### 7.2 Streamlit application


#### Step 1: Generate an [`.env` file](./ui/code/.env_template) for the application

```sh
cd agents
cat ./ui/code/.env_template > ./ui/code/.env
```

* Content

```sh
# WATSONX
export WATSONX_APIKEY=XXX
export WATSONX_REGION=us-south
export WATSONX_DEPLOYMENT_ID=XXX
export WATSONX_PUB_DEPLOYMENT_URL="https://${WATSONX_REGION}.ml.cloud.ibm.com/ml/v4/deployments"
export WATSONX_SOFTWARE_NAME="ai_service"
export WATSONX_SPACE_ID=XXX
export WATSONX_INSTANCE_ID=XXX
export WATSONX_URL="https://${WATSONX_REGION}.ml.cloud.ibm.com"

# APP
export APP_USER=admin
export APP_PASSWORD=admin
```

### Step 2: Start the application

```sh
cd ui/code
bash start_sdk.sh
```

1. Log on `admin/admin`
2. Ask a question
 Possible question:

 * "Can you please answer the question, 'What is a DB2 routine?' and then send me a mail I can send to a customer?"


## 8. Additional resources

* [watsonx Developer Hub](https://github.com/IBM/watsonx-developer-hub)
* [LangGraph multi agent](https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/#using-with-a-prebuilt-react-agent)
* [TextChatParameters](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters)
* [LangChain ChatModels](https://github.com/langchain-ai/langchain-ibm/blob/main/libs/ibm/langchain_ibm/chat_models.py)
* [Develop and Deploy Custom AI Agents to watsonx.ai on IBM Cloud](https://suedbroecker.net/2025/02/25/develop-and-deploy-custom-ai-agents-to-watsonx-ai-on-ibm-cloud/)
# Overview

This readme is about running the example agent locally on a TypeScript server. The example implementation does not connect to any external database for the `Bee Agent configuration` to save a status or more.

If you want to run the application in a container, here are the two options we provide:

1. Run as a container locally

  You can run the example application locally in a container with Podman. To do this, please follow the instructions in the [README_CONTAINER.md](/agents/beeframework/watsonx-rag-db2-expert-agent/code/README.md) file.

2. Run the container on the IBM Cloud Code Engine

  You can run the example application container in IBM Cloud Code Engine. To do this, please follow the instructions in this [README.md](/03_bee_agent/code/bee_local_app_db2_rag_container_ce_node_server/ce-deployment/README.md) file.

# 1. Setup

The following instructions are for the setup on a MacOS environment.

# 1.1 Prerequisits

* [Brew (for Mac)](https://brew.sh/)
* [Node](https://nodejs.org/en/download/package-manager)
* npm and yarn
* [corepack](https://yarnpkg.com/corepack)
* Optionally nvm
* [Podman Desktop](https://podman-desktop.io/)
* Access to IBM watsonx.ai

Example verification:

```sh
node -v
v20.17.0
npm -v
10.8.2
```

## 1.2 Install typescript

```sh
sudo npm install typescript -g
sudo npm i tsx -g
sudo npm i typescript-rest-swagger -g
```

## 1.3 Install the needed package

The `yarn ensure-env` invokes  `"cp -n .env.template .env || true"` for the script specification in the `package.json`.
It creates a copy of the `.env.template`.

```sh
cd agents/beeframework/watsonx-rag-db2-expert-agent/code
```

```sh
yarn install
yarn ensure-env
```

## 1.4 Insert the needed value into the newly create `.env` file with variables

```sh
# WatsonX
export WATSONX_BASE_URL=https://us-south.ml.cloud.ibm.com
export WATSONX_PROJECT_ID=
export WATSONX_API_KEY=
export WATSONX_REGION="us-south"
export WATSONX_MODEL="meta-llama/llama-3-1-70b-instruct"
export WATSONX_DEPLOYMENT_ID=""
```

# 2. Build and run

## 2.1 Build the server

The `yarn build` invokes  `"build": "yarn clean && yarn ts:check && tsc"` for the script specification in the `package.json`.

```sh
yarn build
```

## 2.2 Run the server

The `yarn start:prod` invokes  `"start:prod": "node dist/index.js"` for the script specification in the `package.json`.

```sh
yarn start:prod
```

## 2.3 Open Swagger-UI in browser

```sh
http://localhost:8080/docs
```

## 2.4 Invoke endpoint

* Browser

Insert following question into the `Request body` of the `/db2_agent_help` endpoint.

```text
{
  "question": "I'm trying to execute a routine amed GET_CUSTOMER_DATA in DB2, but it returns an error: 'Routine not found in schema.' I double-checked the routine name, and it exists in the catalog."
}
```

* Terminal

Invoke the endpoint by using curl

```sh
curl -X 'POST' \
  'http://localhost:8080/db2_agent_help' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ "question": "I am trying to execute a routine amed GET_CUSTOMER_DATA in DB2, but it returns an error: *Routine not found in schema.* I double-checked the routine name, and it exists in the catalog." }'
```
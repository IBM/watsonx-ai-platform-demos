# AI Application

This is draft documentation only.

## Prerequisits

* Brew (for Mac)
* [Node](https://nodejs.org/en/download/package-manager)
* npm and yarn
* [corepack](https://yarnpkg.com/corepack)
* Optionally nvm
* [Podman Desktop](https://podman-desktop.io/)
* [Ollama](https://ollama.com/)
* Access to IBM watsonx.ai

```bash
node -v
v20.17.0
npm -v
10.8.2
```

```bash
sudo npm install typescript -g
sudo npm i tsx -g
sudo npm i typescript-rest-swagger -g
```

## Setup

```bash
git clone git@github.ibm.com:niklas-heidloff/watsonx-demo.git
cd watsonx-demo/application
yarn install
yarn ensure-env
// .env: WATSONX_PROJECT_ID and WATSONX_API_KEY
source .env

yarn start:appOneLLMOneAgent
or
yarn start:appOneLLMTwoAgents
or
yarn start

// to udpate swagger: tsoa spec

// optional: yarn infra:start-code-interpreter
```

## REST Endpoints

See [Endpoints.md](Endpoints.md#ollama-summary).

```bash
tsoa spec
yarn start
```

```bash
open http://localhost:8080/docs

curl -X 'POST' \
  'http://localhost:8080/all' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "transcript": "string"
}'

curl -X 'POST' \
  'http://localhost:8080/summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "transcript": "string"
}'

curl -X 'POST' \
  'http://localhost:8080/router' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "summary": "string"
}'

curl -X 'POST' \
  'http://localhost:8080/mail' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "string",
  "summary": "string"
}'
```

## Build and run Container

```bash
Mac:
podman build -t watson-demo .
Linux:
podman build --platform linux/amd64 -t watson-demo-linux-amd64 .

podman run -it --rm -e "WATSONX_API_KEY=xxx" -e "WATSONX_PROJECT_ID=xxx" watson-demo /bin/ash

node dist/appOneLLMOneAgent.js

or
podman run -p 8080:8080 -e "WATSONX_API_KEY=xxx" -e "WATSONX_PROJECT_ID=xxx" watson-demo
```

## Push Container

```bash
open https://cloud.ibm.com/docs/cli?topic=cli-getting-started

ibmcloud plugin install container-registry
ibmcloud plugin install ce
ibmcloud login --sso -r eu-de
ibmcloud target -g niklas
ibmcloud cr login 

// create namespace

podman tag watson-demo-linux-amd64 icr.io/niklas/watson-demo-linux-amd64:7
podman push icr.io/niklas/watson-demo-linux-amd64:7
```

## Deploy to Code Engine

```bash
// create project niklas-watson-demo

// create application niklas-watson-demo

// create secret for private.icr.io

// define WATSONX_API_KEY and WATSONX_PROJECT_ID

// get URL and invoke [endpoints](Endpoints.md)

## build ollama custom transcript summary model - see instructlab/README.md

// get gguf of model and modify path in Modelfile

ollama create transcript-summary -f Modelfile

ollama run transcript-summary
```

Invoke [endpoint](Endpoints.md#ollama-summary).
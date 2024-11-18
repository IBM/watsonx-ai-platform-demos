# Container

* Ensure you installed [Podman](https://podman.io/)

The following diagram shows the simplified architecture for running the server as a TypeScript application and as a container locally.

![](/agents/beeframework/watsonx-rag-db2-expert-agent/images/watsonx-rag-db2-expert-agent-03.png)

## 1. Build the container

* Build the container on MacOS

```sh
podman build -t rag-db2-agent-demo:0.0.1 -f ./Dockerfile.podman
```

_Note:_ We need to build the container for a `Linux/amd64` environment, when we deploy the container to `IBM Cloud Code Engine`. Therefore we can use the [multi architecture Podman](https://blog.while-true-do.io/podman-multi-arch-images/) functionality for the container in Podman.

Example command:

```sh
podman build --platform linux/amd64 -t rag-db2-agent-demo-linux-amd64:0.0.1 -f ./Dockerfile.
```

## 2. Run the container

1. We need to load the environment variables in the terminal with `source .env`, because our container needs these variables to run.

```sh
source .env
```

2. Run the container

```sh
podman run -it -p 8080:8080 -e WATSONX_BASE_URL=${WATSONX_BASE_URL} \
                            -e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
                            -e WATSONX_API_KEY=${WATSONX_API_KEY} \
                            -e WATSONX_MODEL=${WATSONX_MODEL} \
                            -e WATSONX_DEPLOYMENT_ID=${WATSONX_DEPLOYMENT_ID} \
                            -e CODE_INTERPRETER_URL=${CODE_INTERPRETER_URL} \
                            -e BEE_FRAMEWORK_LOG_PRETTY=${BEE_FRAMEWORK_LOG_PRETTY} \
                            -e BEE_FRAMEWORK_LOG_LEVEL=${BEE_FRAMEWORK_LOG_LEVEL} \
                            -e BEE_FRAMEWORK_LOG_SINGLE_LINE=${BEE_FRAMEWORK_LOG_LEVEL} \
                            --name rag-db2-agent-demo \
                            "localhost/rag-db2-agent-demo:0.0.1"
```

## 3. Open Swagger-UI in the browser

```sh
http://localhost:8080/docs
```
# Bee Framework Agent example for a simple travel assistant

This repository is based on the [Bee Agent Framework Starter Template](https://github.com/i-am-bee/bee-agent-framework).

Table of contents:

1. Motivation
2. Architecture
3. System Requirements
4. Setup
5. Execution of the agent locally
6. Execution of the agent locally with the external observer

## 1. Motivation

This example wants to show how to implement a Bee Agent configuration and implementation with one custom Bee Agent tool and one Out-Of-The-Box tool.

The agent should be able to interact in a chat to suggest vacation offerings and tell the temperature in the proposed location.

Therefore, we need two tools to get the information we need.

* Connect to another large language model to suggest the locations (custom tool)
* Connect to a weather server to get the actual weather information (Out-Of-The-Box tool)

We want to ask a question later that requires the agent to use both tools to answer, like the following question.

> "What is the best vacation city in Europe, and can you tell me the current temperature in this city?"


## 2. Architecture

The diagram below shows the simplified dependencies of the implementation in two levels.

1. The implementation of the agent with Out-Of-The-Box and custom tools.

![](/agents/beeframework/watsonx-simple-travel-agent/images/architectue.drawio.png)

2. The observability of the agent with an external tool

![](/agents/beeframework/watsonx-simple-travel-agent/images/architectue-observe.drawio.png)

## 3.  📦 System Requirements

- JavaScript runtime [NodeJS > 18](https://nodejs.org/) (ideally installed via [nvm](https://github.com/nvm-sh/nvm)).
- Container system [Podman](https://podman.io/) (VM must be rootfull machine)
  _Note:_ You can find an example configuration in this blog post [CheatSheet: Essential Steps to Configure Podman Machines](https://suedbroecker.net/2024/11/08/cheetsheet-essential-steps-to-configure-podman-machines/)
- Large language model provider [watsonx](https://www.ibm.com/watsonx)

## 4. 🛠️ Setup

### 4.1 Install Node.js

#### Step 1: Node.js

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
```

* Output

```sh
cat /Users/[USER]/.zshrc
```

```sh
# Created by `pipx` on 2024-04-15 12:44:54
export PATH="$PATH:/Users/[USER]/.local/bin"
export PATH="/opt/homebrew/opt/libpq/bin:$PATH"
. ~/.ilab-complete.zsh
. ~/.ilab-complete.zsh
​
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

_Note:_ You may need to execute in addition to the following command.

```sh
cudo chown -R 501:20 "/Users/[USER]/.npm"
```

#### Step 2: Node Version Manager (nvm)

The following installation ensures you install a specific version of Node Version Manager (nvm), and you can also use the nvm install.

```sh
nvm install 20
```

#### Step 3: Install TypeScript

You don't need to install TypeScript globally, but we do it in this case.

```sh
sudo npm install typescript -g
sudo npm i tsx -g
sudo npm i typescript-rest-swagger -g
```

#### Step 4: Install dependencies

```sh
npm ci
```

#### Step 5: Set the environment variabled

Configure your project by filling in missing values in the `.env` file

```sh
cat .env.template > .env
```

```sh
## WatsonX
export WATSONX_BASE_URL=https://eu-de.ml.cloud.ibm.com
export WATSONX_PROJECT_ID="XXXX"
export WATSONX_API_KEY="XXXX"
export WATSONX_MODEL="meta-llama/llama-3-1-70b-instruct"
```

### Step 5: Verify the container Infrastructure

Ensure you have [Podman](https://podman.io/) installed - requires [compose](https://podman-desktop.io/docs/compose/setting-up-compose) and **rootful machine** (if your current machine is rootless, please create a new one, also ensure you have enabled Docker compatibility mode).

_Note:_ You can find an example configuration in this blog post [CheatSheet: Essential Steps to Configure Podman Machines](https://suedbroecker.net/2024/11/08/cheetsheet-essential-steps-to-configure-podman-machines/)


## 5. 🛠️ Execution of the agent locally

To execute the agent locally, execute the following command.

```sh
npm run start src/agent.ts
```

_Note:_ The `npm run start` invokes  `"start": "npm exec tsx"` for the script specification in the `package.json`.

This command will ask the agent the following question:

```text
"What is the best vacation city in Europe, and can you tell me the current temperature in this city?"
```

This question requires that the agent use both tools to answer the input, and the result will look like this answer from the agent.

```text
According to my research, the best vacation city in Europe is Paris, France. The City of Light offers a unique blend of history, culture, art, fashion, and gastronomy. As for the current temperature, it's 2.5°C (36.5°F) in Paris right now.
```

## 6. 🔎 Execution of the agent locally with the external observer

To enable the complete visibility of the agent's inner workings, we connect to the observability stack running in Podman compose.

- The [MLFlow](https://mlflow.org/) is used as UI for observability.
- The [Bee Observe](https://github.com/i-am-bee/bee-observe) is the observability service (API) for gathering traces from [Bee Agent Framework](https://github.com/i-am-bee/bee-agent-framework).
- The [Bee Observe Connector](https://github.com/i-am-bee/bee-observe-connector) is the observability connector that sends traces from [Bee Agent Framework](https://github.com/i-am-bee/bee-agent-framework) to [Bee Observe](https://github.com/i-am-bee/bee-observe).

### Step 1: Start all needed services with Podman compose

```sh
npm run infra:start --profile=observe
```

_Note:_ Configuration file is [infra/observe/.env.docker](./infra/observe/.env.docker).

### Step 2: Run the agent

```sh
npm run start src/agent_observe.ts
```

### Step 3: Run the agent

See visualized trace in MLFlow web application [`http://127.0.0.1:8080/#/experiments/0`](http://localhost:8080/#/experiments/0)
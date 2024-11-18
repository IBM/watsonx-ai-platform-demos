# watsonx 'Retrieval Augmented Generation (RAG)' - DB2 Expert Agent (Bee Framework)

This code is in the context of the workshop [`regional_techXchange_nov24`](/workshops/regional_techXchange_nov24/README.md).

0. Motivation
1. Overview of the basic architecture of the `Retrieval Augmented Generation (RAG)` 
2. Overview of the basic architecture of the `DB2 expert agent` 
3. Setup
    3.1 Set up the RAG environment
    3.2 Set up the TypeScript server

# 0. Motivation

We want to create an independent AI agent using tools to answer DB2 expert questions. The AI agent should work in chat mode and also be able to answer common questions that are not related to DB2 questions and use tools to answer DB2 expert questions. The first `AI agent tool` we provide is the `Retrieval Augmented Generation (RAG) AI solution` we built before.

The AI agent should run as a stand-alone backend service (server) to be integrated into other applications and provide a REST API for the integration.

We use the `Bee Framework` and build a `TypeScript` server to realize this functionality.

We call our AI agent: `DB2 expert agent` 

## 1. Overview of the basic architecture of the `Retrieval Augmented Generation (RAG)` setup

We have a `Retrieval Augmented Generation (RAG)` setup for DB2 expert questions made with the `watsonx prompt lab`.
For the deployment use of a `Jupyter Notebook` function, calls are being deployed as a Watsonx deployment with access to a `Milvus DB`.

So, we can get results from this deployment using the provided REST endpoints by the deployment.

The image below shows a simplified architecture.

1. We ask a question using the REST Endpoint of the RAG deployment
2. The deployment searches for the best-fitting content in the Milvus database
3. The deployment LLM generates the best answer based on the results we provided

![](/agents/beeframework/watsonx-rag-db2-expert-agent/images/watsonx-rag-db2-expert-agent-01.png)

## 2. Overview of the basic architecture of the `DB2 expert agent` setup

Finally, we run our server, which contains the AI agent with the tool on the serverless container platform `IBM Cloud Code Engine`. The container is save in the `IBM Cloud Container Registry`.

The image below shows a simplified architecture.

1. We ask a question using the REST Endpoint of the TypeScript server running on Code Engine in a container
2. The AI agent uses the LLM to do all the needed steps of thinking, reasoning, and final answers.
3. The AI agent notices that the tool is the best to answer DB2-related questions with the DB2 expert tool.
4. The DB2 expert invokes the REST endpoint of the deployment RAG for the DB2 questions
5. The deployment searches for the best-fitting content in the Milvus database
6. The deployment LLM generates the best answer based on the results we provided

![](/agents/beeframework/watsonx-rag-db2-expert-agent/images/watsonx-rag-db2-expert-agent-02.png)

The simplified TypeScript backend server code dependencies.

![](/agents/beeframework/watsonx-rag-db2-expert-agent/images/watsonx-rag-db2-expert-agent-04.png)


## 3. Setup

### 3.1 Set up the RAG environment

Follow the steps for the [setup steps in the workshop documentation for the regional_techXchange_nov24 workshop](workshops/regional_techXchange_nov24/00_setup/readme.md) .


### 3.2 Set up the TypeScript server

Therefore, you can follow the code documentation.

[Source code](/agents/beeframework/watsonx-rag-db2-expert-agent/code/README.md)

What we did before:

1. Implemented the server
2. Implemented the agent
3. Implemented the tool
4. Run it locally
5. Run it in a container locally
6. Run it on a containerized platform
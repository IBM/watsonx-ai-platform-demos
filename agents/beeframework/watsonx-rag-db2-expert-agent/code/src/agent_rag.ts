/**
 * Copyright 2024 IBM Corp.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import "dotenv/config";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import { createConsoleReader } from "./helpers/io.js";
import { DB2AgentTool } from "./custom_tools/rag_agent_tools.js";
import { FrameworkError } from "bee-agent-framework/errors";
import { Logger } from "bee-agent-framework/logger/logger";
import { UnconstrainedMemory } from "bee-agent-framework/memory/unconstrainedMemory";
import { BaseMessage } from "bee-agent-framework/llms/primitives/message";
import { WatsonXChatLLM } from "bee-agent-framework/adapters/watsonx/chat";
import { WatsonXLLM } from "bee-agent-framework/adapters/watsonx/llm";
import { GenerateCallbacks } from "bee-agent-framework/llms/base";
import { PromptTemplate } from "bee-agent-framework/template";

const logger = new Logger({ name: "app", level: "trace" });
/// *******************************
/// 1. The definition of a chat prompt template.
/// *******************************
const template = new PromptTemplate({
  schema: {
    messages: {
        "system": "",
        "user": "",
        "assistant": "",
    },
  },
  template: `{{#messages}}{{#system}}<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{{system}}<|eot_id|>{{/system}}{{#user}}<|start_header_id|>user<|end_header_id|>

{{user}}<|eot_id|>{{/user}}{{#assistant}}<|start_header_id|>assistant<|end_header_id|>

{{assistant}}<|eot_id|>{{/assistant}}{{/messages}}<|start_header_id|>assistant<|end_header_id|>

`,
});
/// *******************************
/// 2. The integration to watsonx is set up.
/// *******************************
const llm_lama = new WatsonXLLM({
  modelId: "meta-llama/llama-3-70b-instruct",
  projectId: process.env.WATSONX_PROJECT_ID,
  baseUrl: process.env.WATSONX_BASE_URL,
  apiKey: process.env.WATSONX_API_KEY,
  parameters: {
    decoding_method: "greedy",
    max_new_tokens: 500,
  },
});                
/// *******************************
/// 3. The definition to use for the LLM interaction the chat mode.
/// *******************************
const chatLLM = new WatsonXChatLLM({
  llm: llm_lama,
  config: {
    messagesToPrompt(messages: BaseMessage[]) {
      return template.render({
        messages: messages.map((message) => ({
          system: message.role === "system" ? [message.text] : [],
          user: message.role === "user" ? [message.text] : [],
          assistant: message.role === "assistant" ? [message.text] : [],
        })),
      });
    },
  },
});
/// *******************************
/// 4. Create an agent and provide the used tools. 
///    In this case, only the `DB2AgentTool` contains 
///    the function does the invocation of RAG implementation for DB2 issues.
/// *******************************
const agent = new BeeAgent({
  llm: chatLLM,
  memory: new UnconstrainedMemory(),
  tools: [
    new DB2AgentTool()
  ]
});

/// *******************************
/// 5. Create a `createConsoleReader`, is a part of the downloaded helpers. The reader helps to display all the steps the agent takes easily.
/// *******************************
const reader = createConsoleReader();
/// *******************************
/// 6. Invoke the agent and display the steps.
/// *******************************

export async function runAgentDB2(question :string ){
  try {
    console.log("DB2:")
    console.info("\n" + question + "\n");
    let prompt = question;
    console.info("\n" + prompt + "\n");
    const response = await agent
      .run(
        { prompt },
        {
          execution: {
            maxRetriesPerStep: 3,
            totalMaxRetries: 10,
            maxIterations: 20,
          },
        },
      )
      .observe((emitter) => {
        emitter.on("start", () => {
          reader.write(`Agent 🤖 : `, "starting new iteration");
        });
        emitter.on("error", ({ error }) => {
          reader.write(`Agent 🤖 : `, FrameworkError.ensure(error).dump());
        });
        emitter.on("retry", () => {
          reader.write(`Agent 🤖 : `, "retrying the action...");
        });
        emitter.on("update", async ({ data, update, meta }) => {
          reader.write(`Agent (${update.key}) 🤖 : `, update.value);
        });
        emitter.match("*.*", async (data: any, event) => {
          if (event.creator === chatLLM) {
            const eventName = event.name as keyof GenerateCallbacks;
            switch (eventName) {
              case "start":
                console.info("LLM Input");
                console.info(data.input);
                break;
              case "success":
                console.info("LLM Output");
                console.info(data.value.raw.finalResult);
                break;
              case "error":
                console.error(data);
                break;
            }
          }
        });
      });
      reader.write(`Agent 🤖 : `, response.result.text);
      let result = { "answer" : response.result.text}
      return result;
  } catch (error) {
    logger.error(FrameworkError.ensure(error).dump());
    let result = { "answer": FrameworkError.ensure(error).dump().toString() }
    return result;
  }
}
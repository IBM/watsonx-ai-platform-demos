import "dotenv/config.js";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import { createConsoleReader } from "./helpers/io.js";
import { TravelAgentTool } from "./custom_tools/travel_agent_tools.js";
import { FrameworkError } from "bee-agent-framework/errors";
import { Logger } from "bee-agent-framework/logger/logger";
import { OpenMeteoTool } from "bee-agent-framework/tools/weather/openMeteo";
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
  modelId: "mistralai/mixtral-8x7b-instruct-v01",
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
/// 4. Create an agent and provide the used tools. In this case, only the `OpenMeteoTool` contains the function to invoke the weather service.
/// *******************************
const agent = new BeeAgent({
  llm: chatLLM,
  memory: new UnconstrainedMemory(),
  tools: [
    new OpenMeteoTool(), new TravelAgentTool()
  ]
});

/// *******************************
/// 5. Create a `createConsoleReader`, is a part of the downloaded helpers. The reader helps to display all the steps the agent takes easily.
/// *******************************
const reader = createConsoleReader();
/// *******************************
/// 6. Invoke the agent and display the steps.
/// *******************************
try {
  let prompt = "What is the best vacation city in Europe, and can you tell me the current temperature in this city?";
  console.info("Prompt:\n" + prompt + "\n");
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
      emitter.on("update", async ({ data, update, meta}) => {
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
} catch (error) {
  logger.error(FrameworkError.ensure(error).dump());
} finally {
  process.exit(0);
}
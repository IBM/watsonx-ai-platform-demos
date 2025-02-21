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

import { WatsonXChatLLM } from "bee-agent-framework/adapters/watsonx/chat";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import { UnconstrainedMemory } from "bee-agent-framework/memory/unconstrainedMemory";
import { RouterUpdateTool } from "./toolRouterUpdate.js";
import { WatsonXChatLLMPresetModel } from "bee-agent-framework/adapters/watsonx/chatPreset";
import { createConsoleReader } from "./io.js";
import { FrameworkError, Logger, PromptTemplate } from "bee-agent-framework";
import { GenerateCallbacks } from "bee-agent-framework/llms/base";
import { BeeAgentTemplates } from "bee-agent-framework/agents/bee/types";
import { readFileSync } from 'fs';

const instructionFile = './prompts/instructionAgentOne.md'
const reader = createConsoleReader();
const logger = new Logger({ name: "app", level: "trace" });

let instruction:string = readFileSync(instructionFile, 'utf-8').split("\\n").join("\n")
const WATSONX_MODEL = process.env.WATSONX_MODEL as WatsonXChatLLMPresetModel
const chatLLM = WatsonXChatLLM.fromPreset(WATSONX_MODEL, {
    apiKey: process.env.WATSONX_API_KEY,
    projectId: process.env.WATSONX_PROJECT_ID,
    baseUrl: process.env.WATSONX_BASE_URL,
    parameters: (defaultParameters) => ({
        ...defaultParameters,
        decoding_method: "greedy",
        max_new_tokens: 1500,
    })
})
const agent = new BeeAgent({
    llm: chatLLM,
    memory: new UnconstrainedMemory(),
    templates: {
        user: new PromptTemplate({
            variables: ["input"],
            template: instruction + `{{input}}`,
        }),
    },
    tools: [
        new RouterUpdateTool()
    ]
});

export async function runAgentUpdateRouterIfNecessary(transcriptSummary:string) {   
    try {
        //console.log("Agent UpdateRouterIfNecessary Prompt Addition:")
        //console.log(transcriptSummary)

        return await agent
            .run(
            { prompt: transcriptSummary },
            {
                execution: {
                maxRetriesPerStep: 5,
                totalMaxRetries: 5,
                maxIterations: 5,
                },
            },
            )
            .observe((emitter) => {
                emitter.on("start", () => {
                    reader.write(`Agent UpdateRouterIfNecessary 🤖 : `, "starting new iteration");
                });
                emitter.on("error", ({ error }) => {
                    reader.write(`Agent UpdateRouterIfNecessary 🤖 : `, FrameworkError.ensure(error).dump());
                });
                emitter.on("retry", () => {
                    reader.write(`Agent UpdateRouterIfNecessary 🤖 : `, "retrying the action...");
                });
                emitter.on("update", async ({ data, update, meta }) => {
                    reader.write(`Agent UpdateRouterIfNecessary (${update.key}) 🤖 : `, update.value);
                });
                emitter.match("*.*", async (data: any, event) => {
                    if (event.creator === chatLLM) {
                        const eventName = event.name as keyof GenerateCallbacks;
                        switch (eventName) {
                            case "start":
                                console.info("Agent UpdateRouterIfNecessary LLM Input");
                                console.info(data.input);
                                break;
                            case "success":
                                console.info("Agent UpdateRouterIfNecessary LLM Output");
                                console.info(data.value.raw.finalResult);
                                break;
                            case "error":
                                console.error(data);
                                break;
                        }
                    }
            });
        });
    } catch (error) {
        logger.error(FrameworkError.ensure(error).dump());
    } 
}
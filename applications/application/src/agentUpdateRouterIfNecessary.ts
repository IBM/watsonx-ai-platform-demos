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

import { WatsonxChatModel } from "bee-agent-framework/adapters/watsonx/backend/chat";
import { BeeAgent } from "bee-agent-framework/agents/bee/agent";
import { UnconstrainedMemory } from "bee-agent-framework/memory/unconstrainedMemory";
import { RouterUpdateTool } from "./toolRouterUpdate.js";
import { RunContextCallbacks } from "bee-agent-framework/context";
import { createConsoleReader } from "./io.js";
import { FrameworkError, Logger, PromptTemplate } from "bee-agent-framework";
import { readFileSync } from 'fs';
import { z } from "zod";

const instructionFile = './prompts/instructionAgentOne.md'
const reader = createConsoleReader();
const logger = new Logger({ name: "app", level: "trace" });

let instruction:string = readFileSync(instructionFile, 'utf-8').split("\\n").join("\n")
const chatLLM = new WatsonxChatModel("meta-llama/llama-3-1-70b-instruct")
chatLLM.parameters.maxTokens = 1500;
chatLLM.parameters.temperature = 0.5;

const agent = new BeeAgent({
    llm: chatLLM,
    memory: new UnconstrainedMemory(),
    templates: {
        user: (template) => 
            template.fork((config) => {
                config.schema = z.object({ input: z.string()}).passthrough();
                config.template = instruction + '{(input)}';
            })
    },
    tools: [
        new RouterUpdateTool()
    ]
});

export async function runAgentUpdateRouterIfNecessary(transcriptSummary:string) {   
    try {
        //console.log("Agent UpdateRouterIfNecessary Prompt Addition:")
        //console.log(transcriptSummary)

        const response = await agent
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
                        const eventName = event.name as keyof RunContextCallbacks;
                        switch (eventName) {
                            case "start":
                                console.info("Agent UpdateRouterIfNecessary LLM Input");
                                console.info(data.input);
                                break;
                            case "success":
                                console.info("Agent UpdateRouterIfNecessary LLM Output");
                                console.info(data.value?.text || data.value);
                                break;
                            case "error":
                                console.error(data);
                                break;
                        }
                    }
                });
        }); return response;
    } catch (error) {
        logger.error(FrameworkError.ensure(error).dump());
    } 
}
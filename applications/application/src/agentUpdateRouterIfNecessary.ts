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
import { FrameworkError, Logger, PromptTemplate } from "bee-agent-framework";
import { readFileSync } from 'fs';
import { z } from "zod";

const instructionFile = './prompts/instructionAgentOne.md'

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
                config.template = instruction + '{{input}}';
            }),
    },
    tools: [
        new RouterUpdateTool()
    ]
});

export async function runAgentUpdateRouterIfNecessary(transcriptSummary:string) {   
    try {
        console.log("🚀 Starting Router Update...");
        let fullResponse = " ";

        return await agent
            .run(
            { prompt: transcriptSummary },
            {
                execution: {
                maxRetriesPerStep: 2,
                totalMaxRetries: 3,
                maxIterations: 2,
                },
            },
            )
            .observe((emitter) => {
                emitter.on("start", () => {
                    console.log(`🛠️ Processing Router Update...`);
                });
                emitter.on("error", ({ error }) => {
                    console.error(`🛠️ Router Update Error ❌:`, FrameworkError.ensure(error).dump());
                });
                emitter.on("retry", () => {
                    console.log(`🛠️ Retrying the Router Update...`);
                });
                emitter.on("update", async ({ update }) => {
                    if (update.key === "tool_output") {
                        fullResponse += update.value + " ";
                    }
                });
                emitter.on("success", async () => {
                    console.info("🛠️ Router Update Completed ✅:", fullResponse.trim());
                });
        });
    } catch (error) {
        console.error('🛠️ Router Update failed ❌:', FrameworkError.ensure(error).dump());
    } 
}
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
import { readFileSync } from 'fs';
import { FrameworkError } from "bee-agent-framework";
import { WriteMailTool } from "./toolWriteMail.js";
import { z } from "zod";

const instructionFile = './prompts/instructionAgentTwo.md'

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
        new WriteMailTool()
    ]
});

export async function runAgentWriteMailIfNecessary(routerUpdated:string, transcriptSummary:string) {
    try {
        console.log("🚀 Starting WriteMail...");
        let fullResponse = "";
        let prompt = routerUpdated + "\n\n" + transcriptSummary;

        return await agent
            .run(
            { prompt },
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
                    console.log(`📩 WriteMail started...`);
                });
                emitter.on("error", ({ error }) => {
                    console.error(`📩 WriteMail Error ❌:`, FrameworkError.ensure(error).dump());
                });
                emitter.on("retry", () => {
                    console.log(`📩 Retrying WriteMail...`);
                });
                // emitter.on("update", async ({ data, update, meta }) => {
                //     if (update.key === "tool_output") {
                //         fullResponse += update.value + " ";
                //     }
                // });
                emitter.on("success", async ({ data }) => {
                    console.info("📩 Email Sent Successfully ✅:", fullResponse.trim());
                });
        });
    } catch (error) {
        console.error("📩 WriteMail Agent Failed ❌:", FrameworkError.ensure(error).dump());
    } 
}
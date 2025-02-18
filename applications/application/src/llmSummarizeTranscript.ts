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

import { readFileSync } from 'fs';
import "dotenv/config.js";
import { createConsoleReader } from "./io.js";
import { WatsonXChatLLM } from "bee-agent-framework/adapters/watsonx/chat";
import { WatsonXChatLLMPresetModel } from 'bee-agent-framework/adapters/watsonx/chatPreset';
import { BeeAgent } from 'bee-agent-framework/agents/bee/agent';
import { UnconstrainedMemory } from "bee-agent-framework/memory/unconstrainedMemory";
import { PromptTemplate } from "bee-agent-framework";
import { createTraceConnector } from '.././infra/observe/mlflow.ts';


const WATSONX_MODEL = process.env.WATSONX_MODEL as WatsonXChatLLMPresetModel
const summarizer = WatsonXChatLLM.fromPreset(WATSONX_MODEL, {
    apiKey: process.env.WATSONX_API_KEY,
    projectId: process.env.WATSONX_PROJECT_ID,
    baseUrl: process.env.WATSONX_BASE_URL,   
    parameters: (defaultParameters) => ({
        ...defaultParameters,
        decoding_method: "greedy",
        max_new_tokens: 1500,
    })
})

const instructionFileLLM = './prompts/instructionLLM.md'
const instructionLLM = readFileSync(instructionFileLLM, 'utf-8').split("\\n").join("\n")

const agent = new BeeAgent({
    llm: summarizer,
    memory: new UnconstrainedMemory(),
    templates: {
        user: new PromptTemplate({
            variables: ["input"],
            template: instructionLLM + `{{input}}`,
        }),
    },
    tools: [],
});    

export async function generateSummary(transcript:string) {
    const reader = createConsoleReader();
    const traceConnector = createTraceConnector();
    let prompt = instructionLLM + "\n\n" + transcript
    console.log("Prompt LLM:")
    console.log(prompt)
    
    

    return await agent.run( {prompt} )
    .middleware(traceConnector)
    .observe((emitter) => {
        emitter.on("start", () => {
            reader.write(`LLM 🤖 : `, "starting new iteration");
        });
        emitter.on("error", ({ error }) => {
            reader.write('LLM error', '');
        });
    });
}
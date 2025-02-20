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
import { UserMessage } from "bee-agent-framework/backend/message";
import { OllamaChatModel } from "bee-agent-framework/adapters/ollama/backend/chat";

export async function generateSummary(transcript:string) {
    const reader = createConsoleReader();

    
    const llm = new OllamaChatModel("llama3.1")
    llm.parameters.temperature = 0.0;
    llm.parameters.maxTokens = 400;
    llm.parameters.stopSequences = ["<|endoftext|>"];
    
    const instructionFileLLM = './prompts/instructionLLMLocal.md'
    const instructionLLM = readFileSync(instructionFileLLM, 'utf-8').split("\\n").join("\n")
    let prompt = instructionLLM + transcript + "\n<|assistant|>\n"
    console.log("Prompt LLM:")
    console.log(prompt)
    
    return await llm.create
    ({
        messages: [new UserMessage(prompt)],
    })
    
    .observe((emitter) => {
        emitter.on("start", () => {
            reader.write(`LLM 🤖 : `, "starting new iteration");
        });
        emitter.on("error", ({ error }) => {
            reader.write('LLM error', '');
        });
    });
}
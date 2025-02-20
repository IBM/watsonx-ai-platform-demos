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
import { WatsonxChatModel } from "bee-agent-framework/adapters/watsonx/backend/chat";

export async function generateSummary(transcript:string) {
    try {    
        console.log("🚀 Starting Transcript Summary Generation...");
        let fullResponse = "";

        const llm = new WatsonxChatModel("meta-llama/llama-3-1-70b-instruct")
        llm.parameters.maxTokens = 1500;

        const instructionFileLLM = './prompts/instructionLLM.md'
        const instructionLLM = readFileSync(instructionFileLLM, 'utf-8').split("\\n").join("\n")

        let prompt = instructionLLM + "\n\n" + transcript
        console.log("\n\n📜 Transcript:\n")
        console.log(transcript, "\n\n")
        
        return await llm.create({
            messages: [new UserMessage(prompt)],
        })
        .observe((emitter) => {
            emitter.on("start", () => {
                console.log(`📝 Transcript Generation Started...`);
            });
            emitter.on("error", ({ error }) => {
                console.error("📝 Transcript Generation Error ❌:", error);
            });
            emitter.on("success", async () => {
                console.info("📝 Transcript Generated ✅");
            });
        });
    } catch (error) {
        console.error("📝 Transcript Generation Failed ❌:", error);
    }
}
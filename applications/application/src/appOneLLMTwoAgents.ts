/**
 * Copyright 2025 IBM Corp.
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
import { generateSummary } from './llmSummarizeTranscript.js';
import { createConsoleReader } from "./io.js";
import { runAgentUpdateRouterIfNecessary } from './agentUpdateRouterIfNecessary.js';
import { runAgentWriteMailIfNecessary } from './agentWriteMailIfNecessary.js';

const transcriptFile = './prompts/prompt4.md'
const reader = createConsoleReader();

console.log("\n🐝✨ Welcome to the Agentic Customer Support Demo built with BeeAI! ✨🐝");
console.log("\n-------------------------------------------------------------------------\n");

//////////////////////////////////////////////////////////////////
// Step 1: LLM summarization
//////////////////////////////////////////////////////////////////
console.log("🔎 Running Transcript Summary Agent...");
let transcript:string = readFileSync(transcriptFile, 'utf-8').split("\\n").join("\n")
const llmResponse = await generateSummary(transcript)
if (!llmResponse) {
    console.error("❌ Transcript Summary Generation Failed: No response received.");
    process.exit(1);
}
let transcriptSummary = llmResponse?.getTextContent()
reader.write(`\n🤖 Transcript Summary : \n`, transcriptSummary);

//////////////////////////////////////////////////////////////////
// Step 2: Agent One with RouterUpdateTool
//////////////////////////////////////////////////////////////////

console.log("\n🔎 Running Router Update Agent...");
const agentOneResponse = await runAgentUpdateRouterIfNecessary(transcriptSummary)
let agentOneResponseText = "";
if (agentOneResponse) {
    let agentOneResponseText = agentOneResponse.result.text
    reader.write(`\n🤖 Router Update: `, agentOneResponseText);
} else {
    console.error("🤖 Router Update: Returned no response");
    process.exit(1);
}

//////////////////////////////////////////////////////////////////
// Step 3: One Agent with RouterUpdateTool and WriteMailTool
//////////////////////////////////////////////////////////////////

console.log("\n🔎 Running Email Notification Agent...");
const agentTwoResponse = await runAgentWriteMailIfNecessary(agentOneResponseText, transcriptSummary)
let agentTwoResponseText = "";
if (agentTwoResponse) {
    let agentTwoResponseText = agentTwoResponse.result.text
    reader.write(`\n🤖 Email Notification: `, agentTwoResponseText);
} else {
    console.error("🤖 Email could not be sent: Returned no response");
    process.exit(1);
}

console.log("\n🎉 All agents have completed their tasks successfully!");
if (process.env.BEE_FRAMEWORK_INSTRUMENTATION_ENABLED === 'true') {
    console.log("Waiting for traces to be exported (5 seconds)...");
    await new Promise(resolve => setTimeout(resolve, 5000));
    console.log("Traces exported to Jaeger UI at http://localhost:16686");
}
process.exit(0);
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
import { generateSummary } from './llmSummarizeTranscript.js';
import { createConsoleReader } from "./io.js";
import { runAgentUpdateRouterIfNecessary } from './agentUpdateRouterIfNecessary.js';
import { runAgentWriteMailIfNecessary } from './agentWriteMailIfNecessary.js';
import { Message, messageStore } from './globalMessageStore.js';

const transcriptFile = './prompts/prompt4.md'
const reader = createConsoleReader(messageStore);

//////////////////////////////////////////////////////////////////
// Step 1: LLM summarization
//////////////////////////////////////////////////////////////////

let transcript:string = readFileSync(transcriptFile, 'utf-8').split("\\n").join("\n")
const llmResponse = await generateSummary(transcript, messageStore)
let transcriptSummary = llmResponse.getTextContent()
reader.write(`Response LLM 🤖 (text) : `, transcriptSummary);

//////////////////////////////////////////////////////////////////
// Step 2: Agent One with RouterUpdateTool
//////////////////////////////////////////////////////////////////

const agentOneResponse = await runAgentUpdateRouterIfNecessary(transcriptSummary, messageStore)
let agentOneResponseText
if (agentOneResponse) {
    agentOneResponseText = agentOneResponse.result.text
    reader.write(`Response UpdateRouterIfNecessary 🤖 : `, agentOneResponseText);

//////////////////////////////////////////////////////////////////
// Step 3: One Agent with RouterUpdateTool and WriteMailTool
//////////////////////////////////////////////////////////////////

    console.log("=================================================================");
    console.log("=================================================================");
    const agentTwoResponse = await runAgentWriteMailIfNecessary(agentOneResponseText, transcriptSummary, messageStore)
    if (agentTwoResponse) {
        let agentTwoResponseText = agentTwoResponse.result.text
        reader.write(`Response WriteMailIfNecessary 🤖 : `, agentTwoResponseText);
    }
}

console.log("Message Store:", JSON.stringify(messageStore, null, 2));
process.exit(0);
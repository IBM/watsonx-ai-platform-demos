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

import { Body, OperationId, Post, Route, Security, Tags } from "tsoa";
import { generateSummary } from "./llmSummarizeTranscript.js";
import { runAgentUpdateRouterIfNecessary } from "./agentUpdateRouterIfNecessary.js";
import { runAgentWriteMailIfNecessary } from "./agentWriteMailIfNecessary.js";

export interface EndpointAllInput {
  transcript: string;
}

interface EndpointAllOutput {
  text: string;
}

@Route("all")
export default class EndpointAllController {
  /**
   * Step 1 - 3
   * @summary step 1 - 3
   */
  @Post("/")
  @OperationId('step123')
  @Tags('Demo')
  public async run(@Body() requestBody: EndpointAllInput): Promise<EndpointAllOutput> {
    let transcript = requestBody.transcript;
    const output: EndpointAllOutput = {
      text: "error"
    };
//////////////////////////////////////////////////////////////////
// Step 1: LLM summarization
//////////////////////////////////////////////////////////////////

    const llmResponse = await generateSummary(transcript)
    let transcriptSummary = llmResponse.getTextContent()

//////////////////////////////////////////////////////////////////
// Step 2: Agent One with RouterUpdateTool
//////////////////////////////////////////////////////////////////

    const agentOneResponse = await runAgentUpdateRouterIfNecessary(transcriptSummary)
    let agentOneResponseText
    if (agentOneResponse) {
        agentOneResponseText = agentOneResponse.result.text

//////////////////////////////////////////////////////////////////
// Step 3: One Agent with RouterUpdateTool and WriteMailTool
//////////////////////////////////////////////////////////////////

        const agentTwoResponse = await runAgentWriteMailIfNecessary(agentOneResponseText, transcriptSummary)
        if (agentTwoResponse) {
            output.text = agentTwoResponse.result.text
        }
      }
      return output
    }
}
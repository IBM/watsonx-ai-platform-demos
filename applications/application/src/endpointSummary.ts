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
import { generateSummary } from './llmSummarizeTranscript.js';

export interface EndpointSummaryInput {
  transcript: string;
}

interface EndpointSummaryOutput {
  summary: string;
}

@Route("summary")
export default class EndpointSummaryController {
  /**
   * Step 1
   * @summary step 1
   */
  @Post("/")
  @OperationId('step1')
  @Tags('Demo')
  public async run(@Body() requestBody: EndpointSummaryInput): Promise<EndpointSummaryOutput> {
    let transcript = requestBody.transcript;
    transcript.split("\\n").join("\n")

    const llmResponse = await generateSummary(transcript)
    let transcriptSummary = llmResponse.getTextContent()

    const output: EndpointSummaryOutput = {
      summary: transcriptSummary
    };
    return output;
  }
}
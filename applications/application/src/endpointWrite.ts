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

import { Body, OperationId, Post, Route, Tags } from "tsoa";
import { runAgentWriteMailIfNecessary } from "./agentWriteMailIfNecessary.js";

export interface EndpointMailInput {
  text: string;
  summary: string
}

interface EndpointMailOutput {
  text: string;
}

@Route("mail")
export default class EndpointMailController {
  /**
   * Step 3
   * @summary step 3
   */
  @Post("/")
  @OperationId('step3')
  @Tags('Demo')
  public async run(@Body() requestBody: EndpointMailInput): Promise<EndpointMailOutput> {
    let text = requestBody.text;
    let summary = requestBody.summary
    const output: EndpointMailOutput = {
      text: "error"
    };
    const agentTwoResponse = await runAgentWriteMailIfNecessary(text, summary)
    if (agentTwoResponse) {
        output.text = agentTwoResponse.result.text
    }
    return output;
  }
}
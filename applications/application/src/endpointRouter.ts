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
import { runAgentUpdateRouterIfNecessary } from "./agentUpdateRouterIfNecessary.js";

export interface EndpointRouterInput {
  summary: string;
}

interface EndpointRouterOutput {
  text: string;
}

@Route("router")
export default class EndpointRouterController {
  /**
   * Step 2
   * @summary step 2
   */
  @Post("/")
  @OperationId('step2')
  @Tags('Demo')
  public async run(@Body() requestBody: EndpointRouterInput): Promise<EndpointRouterOutput> {
    let summary = requestBody.summary;
    const agentOneResponse = await runAgentUpdateRouterIfNecessary(summary)
    const output: EndpointRouterOutput = {
      text: "error"
    };
    if (agentOneResponse) {
      output.text = agentOneResponse.result.text
    }
    return output;
  }
}
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

import { z } from "zod";
import { Tool, ToolInput, BaseToolOptions, BaseToolRunOptions, ToolOutput } from "bee-agent-framework/tools/base";

export interface WriteMailToolOptions extends BaseToolOptions {}

export interface WriteMailToolRunOptions extends BaseToolRunOptions {}

export interface WriteMailResult {
  success: string;
  text: string;
}

export class WriteMailToolOutput extends ToolOutput{
  constructor(result:WriteMailResult) {
    super();
    this.finalResult = JSON.stringify(result)
  }
  finalResult:string;
  isEmpty(): boolean {
    return false;
  }
  createSnapshot(): unknown {
    throw new Error("Method not implemented.");
  }
  loadSnapshot(snapshot: unknown): void {
    throw new Error("Method not implemented.");
  }
  static {
    this.register();
  }
  getTextContent(): string {
    return this.finalResult
  }
}

export class WriteMailTool extends Tool<
  WriteMailToolOutput,
  WriteMailToolOptions,
  WriteMailToolRunOptions
> {
  name = "WriteMail"; // no spaces
  description =
    "Writes an email to the subscriber, but only if and after the router could be updated successfully remotely";
    //"Writes an email to the subscriber if the router could be updated successfully remotely"; 
    // Not strong enough. Invokes Write Mail tool before Router Update tool.

  inputSchema() {
    return z.object({
      phoneNumber: z
        .string({ description: `Phone number of a subscriber, for example '123-456-7890'` })
        .min(1)
        .max(40),
      summary: z
        .string({ description: `Summary of the transcript between the agent and the subscriber` })
        .min(1)
        .max(4000),
    });
  }

  public constructor(public readonly config: WriteMailToolOptions = {}) {
    super(config);
  }

  static {
    this.register();
  }

  protected async _run({ phoneNumber: phoneNumber, summary: summary }: ToolInput<WriteMailTool>,
    _options?: WriteMailToolRunOptions): Promise<WriteMailToolOutput> {
    
    console.log("Input to Write Mail tool - phoneNumber: " + phoneNumber)
    console.log("Input to Write Mail tool - summary: " + summary)

    // real implementation goes here    
    let results:WriteMailResult = {
      success: "true",
      text: "Mail has been written and sent" // some descriptive text is required to support the LLM to understand the result
    }
    return new WriteMailToolOutput(results);
  }
}

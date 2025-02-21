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

export interface RouterUpdateToolOptions extends BaseToolOptions {}

export interface RouterUpdateToolRunOptions extends BaseToolRunOptions {}

export interface RouterUpdateResult {
  success: string;
  text: string;
}

export class RouterUpdateToolOutput extends ToolOutput{
  constructor(result:RouterUpdateResult) {
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

export class RouterUpdateTool extends Tool<
  RouterUpdateToolOutput,
  RouterUpdateToolOptions,
  RouterUpdateToolRunOptions
> {
  name = "RouterUpdate"; // no spaces
  description =
    "Updates the software of routers remotely for a subscriber with a certain phone number.";

  inputSchema() {
    return z.object({
      phoneNumber: z
        .string({ description: `Phone number of a subscriber, for example '123-456-7890'` })
        .min(1)
        .max(40),
    });
  }

  public constructor(public readonly config: RouterUpdateToolOptions = {}) {
    super(config);
  }

  static {
    this.register();
  }

  protected async _run({ phoneNumber: phoneNumber }: ToolInput<RouterUpdateTool>,
    _options?: RouterUpdateToolRunOptions): Promise<RouterUpdateToolOutput> {
    
    console.log("Input to Router Update tool - phoneNumber: " + phoneNumber)

    // real implementation goes here
    let results:RouterUpdateResult = {
      success: "true",
      text: "Router has been updated" // some descriptive text is required to support the LLM to understand the result
    }
    return new RouterUpdateToolOutput(results);
  }
}

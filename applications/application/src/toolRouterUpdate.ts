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
import { Tool, ToolInput, ToolEmitter, ToolOutput } from "bee-agent-framework/tools/base";
import { Emitter } from "bee-agent-framework/emitter/emitter";

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
  RouterUpdateToolOutput> {
  name = "RouterUpdate"; // no spaces
  description =
    "Updates the software of routers remotely for a subscriber with a certain phone number.";

  public readonly emitter: ToolEmitter<ToolInput<this>, RouterUpdateToolOutput> = Emitter.root.child({
    namespace: ["tool", "routerUpdate"],
    creator: this,
  })

  inputSchema() {
    return z.object({
      phoneNumber: z
        .string({ description: `Phone number of a subscriber, for example '123-456-7890'` })
        .min(1)
        .max(40),
    });
  }

  static {
    this.register();
  }

  protected async _run(input: ToolInput<this>): Promise<RouterUpdateToolOutput> {
    const { phoneNumber } = input;
    console.log("Input to Router Update tool - phoneNumber: " + phoneNumber);

    // Optionally, you can emit a start event if needed:
    // this.emitter.emit("start", { toolName: this.name });

    // Simulate your router update process
    const results: RouterUpdateResult = {
      success: "true",
      text: "Router has been updated",
    };

    // Optionally, emit an update event for final results:
    // this.emitter.emit("update", { key: "final_answer", value: JSON.stringify(results) });

    return new RouterUpdateToolOutput(results);
  }
}

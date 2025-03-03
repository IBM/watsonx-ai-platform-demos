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

// Reference: https://github.com/i-am-bee/bee-agent-framework/blob/e117284496d215e242254473b1ef8d9539d1d532/examples/helpers/io.ts

import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";
import picocolors from "picocolors";
import * as R from "remeda";
import stripAnsi from "strip-ansi";
import { inspect } from "util";

interface ReadFromConsoleInput {
  fallback?: string;
  input?: string;
  allowEmpty?: boolean;
}

function omitUnwanted(obj: any, seen = new WeakSet()): any {
  if (obj === null || typeof obj !== "object") {
    return obj;
  }
  if (seen.has(obj)) {
    return obj;
  }
  seen.add(obj);
  if (Array.isArray(obj)) {
    return obj.map(item => omitUnwanted(item, seen));
  }
  const result: any = {};
  for (const key in obj) {
    if (key === "raw" || key === "handlers" || key === "emitter") continue;
    result[key] = omitUnwanted(obj[key], seen);
  }
  return result;
}

export function createConsoleReader({
  fallback,
  input = "User 👤 : ",
  allowEmpty = false,
}: ReadFromConsoleInput = {}) {
  const rl = readline.createInterface({ input: stdin, output: stdout, terminal: true });
  let isActive = true;

  return {
    write(role: string, data: any) {
      if (typeof data === "string") {
        rl.write(
          [
            role && R.piped(picocolors.red, picocolors.bold)(role),
            picocolors.red(stripAnsi(data ?? ""))
          ]
            .filter(Boolean)
            .join(" ")
            .concat("\n"),
        );
        return;
      }
      
      if (data && typeof data === "object") {
        const cleanedData = omitUnwanted(data);
        const output = inspect(cleanedData, {
          depth: null,
          maxArrayLength: null,
          maxStringLength: null,
          colors: true,
          compact: false,
        });
        rl.write(
          [
            role && R.piped(picocolors.red, picocolors.bold)(role),
            output
          ]
            .filter(Boolean)
            .join(" ")
            .concat("\n"),
        );
        return;
      }
      
      rl.write(
        [role && R.piped(picocolors.red, picocolors.bold)(role), stripAnsi(data ?? "")]
          .filter(Boolean)
          .join(" ")
          .concat("\n"),
      );
    },
    async prompt(): Promise<string> {
      for await (const { prompt } of this) {
        return prompt;
      }
      process.exit(0);
    },
    async *[Symbol.asyncIterator]() {
      if (!isActive) {
        return;
      }

      try {
        rl.write(
          `${picocolors.dim(`Interactive session has started. To escape, input 'q' and submit.\n`)}`,
        );

        for (let iteration = 1, prompt = ""; isActive; iteration++) {
          prompt = await rl.question(R.piped(picocolors.cyan, picocolors.bold)(input));
          prompt = stripAnsi(prompt);

          if (prompt === "q") {
            break;
          }
          if (!prompt.trim() || prompt === "\n") {
            prompt = fallback ?? "";
          }
          if (allowEmpty !== false && !prompt.trim()) {
            rl.write("Error: Empty prompt is not allowed. Please try again.\n");
            iteration -= 1;
            continue;
          }
          yield { prompt, iteration };
        }
      } catch (e) {
        if (e.code === "ERR_USE_AFTER_CLOSE") {
          return;
        }
      } finally {
        isActive = false;
        rl.close();
      }
    },
  };
}
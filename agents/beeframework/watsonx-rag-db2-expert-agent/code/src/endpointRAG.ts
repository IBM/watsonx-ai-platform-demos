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

import { runAgentDB2 } from "./agent_rag.js";


interface EndpointDB2Output {
    answer: string;
}

interface EndpointDB2Input {
    question: string;
}

class EndpointDB2Controller {

    public async postResponse(input: EndpointDB2Input): Promise<EndpointDB2Output> {
        let question= input.question;
        const agentDB2 = await runAgentDB2(question)
        console.info("output: agentDB2");
        console.info("\n" + agentDB2.answer + "\n");
        const output: EndpointDB2Output = {
            answer: agentDB2.answer
        };
        return output;
    }
}

export default EndpointDB2Controller;
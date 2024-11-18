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

import "dotenv/config";
import {BaseToolOptions,
        BaseToolRunOptions,
        JSONToolOutput,
        Tool,
        ToolInput, } from "bee-agent-framework/tools/base";
import { RunContext } from "bee-agent-framework/context";
import { z } from "zod";

// Endpoint related
import axios from 'axios';

type ToolOptions = BaseToolOptions;
type ToolRunOptions = BaseToolRunOptions;

interface DB2AgentToolResponse {
    answer: string;
    resources: any[];
}

export class DB2AgentTool extends Tool <JSONToolOutput<DB2AgentToolResponse>,ToolOptions,
ToolRunOptions>{
  name = "DB2AgentTool";
  description = `This tool is an expert for DB2-related technical questions or issues. It identifies if technical problems can be fixed with the available information from an issue database. It also provides suggestions for solving a problem.`;
  
  ///////////////////////////////
  // Tool implementation
  inputSchema() {
      return z.object({ question_input: z.string().describe("Question or issue.")})                                              
  } 
  
  static {
    this.register();
  }

  protected async _run( {question_input: in_question, ...input}: ToolInput<this>,
      _options: BaseToolRunOptions | undefined,
      run: RunContext<this>,
    ) {
      const question = in_question;
      try{
        const resp = this.getRAGResponse(question);
        console.info("Log:\nDB2 result:\n" + resp.toString())
        const data = { "answer": (await resp).answer,
                       "resources": (await resp).resources }
        return new JSONToolOutput(data);
      } catch(err) {
        console.log("Log:\nDB2 error:\n" + err);
        const data = { "answer": err,
                       "resources": [] }
        return new JSONToolOutput(data);
      }
    }

  ////////////////////////////////////////
  // DB2 RAG invocation
  async  getToken(apiKey: any): Promise<string> {
    const url = "https://iam.cloud.ibm.com/identity/token";
    const data = new URLSearchParams();
    data.append("grant_type", "urn:ibm:params:oauth:grant-type:apikey");
    data.append("apikey", apiKey);
    const headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    };
    try {
        const response = await axios.post(url, data.toString(), { headers });
        console.log(response.data.access_token);
        return response.data.access_token
    } catch (error) {
        console.error("Error fetching the token:", error);
        return error
    }
  }

  async getRAGResponse(question : any): Promise<DB2AgentToolResponse>{
    const watsonx_deployment_id = process.env.WATSONX_DEPLOYMENT_ID
    const watsonx_api_key = process.env.WATSONX_API_KEY
    
    try {
        const token = await this.getToken(watsonx_api_key);
        
        const content = { "role": "user", "content": question }
        const messages: any[] = [content];
        const token_array: any[] = [ token ]

        console.info("1. Get IAM access token:\n", token);
    
        const payload_scoring = {
          "input_data": [
            {
              "fields": ["Search", "access_token"],
              "values": [messages, token_array],
            }
          ]
        };

        console.info("2. invokeMLEndpoint payload_scoring:\n", JSON.stringify(payload_scoring));

        const response = await fetch("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/" + watsonx_deployment_id + "/predictions?version=2021-05-01", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
          },
          body: JSON.stringify(payload_scoring)
        });
    
        const data = await response.json();
        console.info("3. response data:\n", JSON.stringify(data.predictions[0].values[1]));
        
        var values_array = data.predictions[0].values[0]
        var resources = new Array();
        
        for(let i=0; i<values_array.length; i++){
          console.log(values_array[i].metadata.asset_name); //use i instead of 0
          resources.push(values_array[i].metadata.asset_name);
        }
        
        const final_data: DB2AgentToolResponse  = { "answer": data.predictions[0].values[1] as string,
                                                    "resources": resources
                                                  };

        return final_data;
    } catch (error) {
          const final_data: DB2AgentToolResponse  = { "answer": error.message as string,
                                                      "resources": []
          };

          return final_data;
    }
  }
}

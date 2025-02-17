import "dotenv/config.js";
import { BaseToolOptions,
         BaseToolRunOptions,
         JSONToolOutput,
         Tool,
         ToolError,
         ToolInput, } from "bee-agent-framework/tools/base";
import { RunContext } from "bee-agent-framework/context";
import { WatsonXLLM,
         WatsonXLLMOutputResult,
         WatsonXLLMOutput } from "bee-agent-framework/adapters/watsonx/llm";
import { z } from "zod";

type ToolOptions = BaseToolOptions;
type ToolRunOptions = BaseToolRunOptions;

interface TravelAgentToolResponse {
    rank: number;
    city: string;
    country: string;
    reason_to_travel: string;
    main_interests_covered: string;
}
  
export class TravelAgentTool extends Tool <JSONToolOutput<TravelAgentToolResponse>,ToolOptions,
ToolRunOptions>{
    name = "TravelAgent";
    description = `Provides a list of vacation options to visit it answers with the reasons to travel to a city.`;
       
    inputSchema() {
        return z.object({ question_input: z.string().describe("Question of the traveler.")})                                              
    }

    static {
        this.register();
    }

    protected async _run( {question_input: question, ...input}: ToolInput<this>,
        _options: BaseToolRunOptions | undefined,
        run: RunContext<this>,
      ) {
    const llm_granite = new WatsonXLLM({
            modelId: "mistralai/mixtral-8x7b-instruct-v01",
            projectId: process.env.WATSONX_PROJECT_ID,
            baseUrl: process.env.WATSONX_BASE_URL,
            apiKey: process.env.WATSONX_API_KEY,
            parameters: {
                decoding_method: "greedy",
                max_new_tokens: 500,
                stop_sequences: ["]\n"],
                repetition_penalty: 1,
            },
    });
    let prompt = '# Role\n' +
        'You are a travel agent and you provide the best suggestions related to vacation trips.\n\n' +
        '# Instructions\n' +
        'You must answer in following a JSON list format that contains following information.\n' +
        'You must provide only 2 entries in the list at the moment.\n\n' +
        '[{\n' +
        '"rank": NUMBER\n' +
        '"city": TEXT\n' +
        '"country": TEXT\n' +
        '"reason_to_travel": TEXT\n' +
        '"main_interests_covered": TEXT\n' +
        '}]\n\n' +
        'Now answer the following question : {question}'
  
    console.log("Log:\nPrompt:\n" + prompt + "\n")
    let formatted_prompt = prompt.replace("{question}", question);
    console.log("Log:\nFormated prompt:\n" + formatted_prompt + "\n")
    try {
        const result = await llm_granite.generate(formatted_prompt);
        console.log(result); // Output: Async data has been fetched!
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    const resp = await llm_granite.generate(formatted_prompt);
    
    console.log("Log:\nLLM result:\n" + resp.toString())
    const data: TravelAgentToolResponse = JSON.parse(resp.results[0].generated_text);

    return new JSONToolOutput(data);
   }
}
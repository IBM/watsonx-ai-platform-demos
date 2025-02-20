import { WatsonxChatModel } from "bee-agent-framework/adapters/watsonx/backend/chat";
import { AgentWorkflow } from "bee-agent-framework/workflows/agent";
import { WriteMailTool } from "./toolWriteMail.js";
import { RouterUpdateTool } from "./toolRouterUpdate.js";
import { createConsoleReader } from "./io.js";
import { UnconstrainedMemory } from "bee-agent-framework/memory/unconstrainedMemory";
import { readFileSync } from "fs";
import { UserMessage } from "bee-agent-framework/backend/message";
import "dotenv/config";

const chatLLM = new WatsonxChatModel("meta-llama/llama-3-1-70b-instruct")
chatLLM.parameters.maxTokens = 1500;
chatLLM.parameters.temperature = 0.5;
const workflow = new AgentWorkflow();
const reader = createConsoleReader();

workflow.addAgent({
    name: "Summarizer",
    instructions: "You are a transcript summarization assistant. Given the transcript, generate a concise summary. \n\n Transcript:\n{context} ",
    llm: chatLLM,
    tools: [],
    execution: {
        maxIterations: 3,
    },
});

workflow.addAgent({
    name: "RouterUpdate",
    instructions: "You are a router update assistant. Review the transcript summary and if needed, update the router. \n\n Transcript Summary:\n{context} ",
    llm: chatLLM,
    tools: [new RouterUpdateTool()],
    execution: {
        maxIterations: 3,
    },
});

workflow.addAgent({
    name: "MailAgent",
    instructions: "You are a mail assistant. Review the router update and if successful, write an email. \n\n Router Update:\n{routerUpdate} \n\n Transcript Summary:\n{context}",
    llm: chatLLM,
    tools: [new WriteMailTool()],
    execution: {
        maxIterations: 3,
    },
});

const memory = new UnconstrainedMemory();

const transcriptFile = "./prompts/prompt4.md";
const transcript = readFileSync(transcriptFile, "utf-8").split("\\n").join("\n");

await memory.add(new UserMessage(transcript, { createdAt: new Date() }));

const observer = (emitter: any) => {
    emitter.on("success", (data: any) => {
      reader.write(
        "Success",
        `\n=== Step Completed: ${data.step} ===\nOutput:\n${data.state?.finalAnswer ?? "-"}\n`
      );
    });
    emitter.on("retry", (data: any) => {
      reader.write(
        "Retry",
        `\n*** Retry on Step: ${data.step} ***\nMessage: ${data.message || "Retrying..."}\n`
      );
    });
    emitter.on("error", (error: any) => {
      reader.write(
        "Error",
        `\n!!! Error encountered: ${error} !!!\n`
      );
    });
  };  

const { result } = await workflow.run(memory.messages).observe(observer);

reader.write('Agent 🤖 Final Answer : ', result.finalAnswer);

await memory.addMany(result.newMessages.slice(-1));

process.exit(0);
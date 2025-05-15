from typing import Callable

from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models.schema import TextGenParameters
from langchain_ibm import ChatWatsonx
from langgraph.graph.graph import CompiledGraph
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


from langgraph_react_agent import TOOLS
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

# Instana code 
# This is no longer needed 
# -> see this is the file 'workshops/regional_techXchange_2025_05/03_phase3_agents/agents/langgraph_implementation/examples/execute_ai_service_single_agent_locally.py'
#from traceloop.sdk import Traceloop
#from traceloop.sdk.decorators import workflow
#from dotenv import load_dotenv
#load_dotenv()
#Traceloop.init(app_name="Build_DACH_agent_llm_observ_thomass", disable_batch=True)

# Instana code (still needed)
#@workflow(name="Build_DACH_agent_llm_observ_thomass")
def get_graph_closure(client: APIClient, model_id: str) -> Callable:
    """Graph generator closure."""

    parameters = TextGenParameters(
                    decoding_method = "greedy",
                    repetition_penalty = 1,
                    max_new_tokens = 4000,
                    min_new_tokens = 0,
                    stop_sequences= [],
                    temperature=0.0,
                    top_p=1,
                )

    # Initialise ChatWatsonx
    chat = ChatWatsonx(model_id=model_id,  
                       parameters= parameters, 
                       watsonx_client=client)

    # Define system prompt
    default_system_prompt = """
    You are a helpful AI assistant, please respond to the user's query to the best of your ability! 
    Execute a tool call whenever you see fit.
    """

    # Initialise memory saver
    memory = MemorySaver()

    def get_graph(system_prompt=default_system_prompt) -> CompiledGraph:
        """Get compiled graph with overwritten system prompt, if provided"""

        # Create instance of compiled graph
        return create_react_agent(
            chat, 
            tools=TOOLS, 
            checkpointer=memory, 
            state_modifier=system_prompt
        )

    return get_graph

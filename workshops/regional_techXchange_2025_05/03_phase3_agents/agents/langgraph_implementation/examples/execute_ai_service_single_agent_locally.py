from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.deployments import RuntimeContext

from ai_service_single_agent import deployable_ai_service
from utils import load_config
from examples._interactive_chat import InteractiveChat

# Instana code
# Documentation: https://www.ibm.com/docs/en/instana-observability/1.0.294?topic=platforms-watsonx
# See for the workflow usage in the agent implementation file: workshops/regional_techXchange_2025_05/03_phase3_agents/agents/langgraph_implementation/src/langgraph_react_agent/agent.py
#from traceloop.sdk import Traceloop
#from traceloop.sdk.decorators import workflow
#from dotenv import load_dotenv
#load_dotenv()
#Traceloop.init(app_name="Build_DACH_agent_llm_observ_thomass", disable_batch=True)
stream = True
config = load_config()
dep_config = config["deployment"]
online_parameters = dep_config["online"]["parameters"]

client = APIClient(
    credentials=Credentials(
        url=dep_config["watsonx_url"], api_key=dep_config["watsonx_apikey"]
    ),
    space_id=dep_config["space_id"],
)

context = RuntimeContext(api_client=client)
ai_service_resp_func = deployable_ai_service(context=context, **online_parameters)[stream]

def ai_service_invoke(payload):
    context.request_payload_json = payload
    return ai_service_resp_func(context)

chat = InteractiveChat(ai_service_invoke, stream=stream)
chat.run()
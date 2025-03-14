from langgraph_react_agent.tools import email_expert_service
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

question = "A"
answer = "B"

logging.debug(f"{email_expert_service.name}")
logging.debug(f"{email_expert_service.description}")
logging.debug(f"{email_expert_service.args}")
dict = {"question": "B", "answer": "A"}
logging.debug(f"{email_expert_service.invoke(dict)}")

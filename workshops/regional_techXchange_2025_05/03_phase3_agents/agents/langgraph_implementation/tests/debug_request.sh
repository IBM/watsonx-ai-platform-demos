deactivate
source ../.venv/bin/activate
source ../src/langgraph_react_agent/.env
python3 debug_request_db2_expert.py
python3 debug_request_email_expert.py
#python3 debug_request_email_expert_function.py
export HOME=$(pwd)

# 1. Source the existing virtual Python environment

cd ../..
cd agents/langgraph_implementation

source ./.venv/bin/activate

# 2. Source the needed environment variables and Streamlit application

cd ${HOME}
source .env
streamlit run app_sdk.py


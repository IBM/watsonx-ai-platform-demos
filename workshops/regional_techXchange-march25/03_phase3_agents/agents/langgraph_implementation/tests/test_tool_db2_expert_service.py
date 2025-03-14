import pytest
from langgraph_react_agent.tools import db2_expert_service
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

testdata = [
    { 
      'question': 'What is a DB2 routine?', 
    },
    {
      'question': 'How to connect to DB2 with a Java application, running on MacOS',
    }
]

@pytest.mark.parametrize("question", testdata)

class TestTools:
     
    def test_db2_expert_service(self, question):
        try:

            logging.debug(f"Toolname:\n{db2_expert_service.name}")
            logging.debug(f"Tool description:\n{db2_expert_service.description}")
            logging.debug(f"Tool arguments:\n{db2_expert_service.args}")
            dict = {"question": question}
            the_result= db2_expert_service.invoke(dict)
            print(f"**Test Case 'db2_expert_service' result: {the_result}")
            assert the_result
        except Exception as error:
            print(f"**Test Case 'email' error: {error}")
            
        result= db2_expert_service(question)
        print(f"**Test Case 'weather' result: {result}")
        assert result

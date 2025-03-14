import pytest
from langgraph_react_agent.tools import email_expert_service
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

testdata = [
    pytest.param("A routine that usually runs in under 2 minutes is now timing out after 30 minutes. No changes were made to the routine or database. How do I resolve this?","What is DB2?",id="run 1"),
    pytest.param("Investigate potential database locking or blocking issues. Advise checking for long-running transactions or locks using db2pd -locks or reviewing system performance metrics.","A Database made by IBM",id="run 2"),
    pytest.param("A","B",id="run 3"),
]

@pytest.mark.parametrize( "in_question, in_answer", testdata)

class TestTools:
    
    def test_email_expert_service(self, in_question, in_answer ): 
        question : str =  in_question
        answer : str =  in_answer
        print(f"**Test Case 'email' parameters: {question}, {answer}")
        try:

            logging.debug(f"Toolname:\n{email_expert_service.name}")
            logging.debug(f"Tool description:\n{email_expert_service.description}")
            logging.debug(f"Tool arguments:\n{email_expert_service.args}")
            dict = {"question": question, "answer": answer}
            the_result= email_expert_service.invoke(dict)
            print(f"**Test Case 'email' result: {the_result}")
            assert the_result
        except Exception as error:
            print(f"**Test Case 'email' error: {error}")
        

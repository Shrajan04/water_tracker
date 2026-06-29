import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(
    api_key=GOOGLE_GENAI_API_KEY,
    model="gemini-2.5-flash",
    temperature=0.5)

class waterIntakeAgent:
    def __init__(self):
       self.history =[]

    def analyze_intake(self, intake_ml):

        prompt =f"""
         you are a hydration assistant. The user has consumed {intake_ml} ml of water today.  
         provide a hydration status and suggest if they need to drink more water
         """

        response = llm.invoke([HumanMessage(content=prompt)])  

        return response.content
    
if __name__=="__main__":
    agent=waterIntakeAgent()
    intake= 1500
    feedback= agent.analyze_intake(intake)
    print(feedback)
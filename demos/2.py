import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.google_genai import GoogleGenAI

from dotenv import load_dotenv
load_dotenv()
def runbash(command:str)->str:
    """runs a terminal command passed to the function as a argument"""
    import subprocess
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

agent=FunctionAgent(
    tools=[runbash],
    llm=GoogleGenAI("gemini-2.0-flash-lite"),
    system_prompt="You are a helpful and safety-conscious AI agent. Your job is to interpret the user's harmless requests and, when appropriate, generate safe and valid terminal commands to accomplish the task"
)

async def main(request):
    response=await agent.run(request)
    print(str(response))

if __name__=="__main__":
    while True:
        x=input("your request:\n")
        if x == "exit": break
        asyncio.run(main(x)) 
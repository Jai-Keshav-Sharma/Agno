from agno.agent import Agent
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
if os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


agent = Agent(
    model=Groq(id="qwen-qwq-32b"),
    description="You are an assistant. Please reply based on the questions.",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who is the President of the United States?")







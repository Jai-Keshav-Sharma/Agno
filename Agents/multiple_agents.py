from agno.agent import Agent
from agno.models.openai import OpenAIChat 
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

if os.getenv("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
if os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

web_agent = Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen-qwq-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources in your response",
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="qwen-qwq-32b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions="Use tables to present the data",
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-qwq-32b"),
    instructions=["Always include sources", "use tables to present the data"],
    show_tool_calls=True,
    markdown=True
)

response = agent_team.print_response("What is the stock price of Apple and compare it to the stock price of Google?")
print(response)
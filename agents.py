# agents.py
from crewai import Agent
from llm import ollama_llm
from tools import web_fetcher #, calculator

explorer = Agent(
    role="Explorer",
    goal="Fetch and read web pages for a given URL.",
    backstory="You are great at extracting useful content from web pages.",
    llm=ollama_llm,
    tools=[web_fetcher],   # tool function from @tool
    verbose=True,
)

summarizer = Agent(
    role="Summarizer",
    goal="Find programming languages name mentioned on the sentense. Summarize the provided text clearly and concisely.",
    backstory="You summarize and find out the programming languages names mentioned there.",
    llm=ollama_llm,
    tools=[],               # NO tools
    allow_delegation=False, # prevent calling tools
    verbose=True,
)


critic = Agent(
    role="Critic",
    goal="Critique summaries and appriciate for the experience and suggest new learning they can make.",
    backstory="You carefully check summaries & find the programming language names for clarity and completeness.",
    llm=ollama_llm,
    tools=[],    # uses calculator tool for any numeric reasoning
    verbose=True,
)

# crew.py
from crewai import Crew, Task
from agents import explorer, summarizer, critic
from tasks import task_fetch, task_summarize, task_critic


crew = Crew(
    agents=[explorer, summarizer, critic],
    tasks=[task_fetch, task_summarize, task_critic],
    memory=False,   # no external memory, no API keys needed
    verbose=True,
    tracing=True
)

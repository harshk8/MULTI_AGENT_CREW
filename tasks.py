# tasks.py
from crewai import Task
from agents import explorer, summarizer, critic

# -------------------------------------------------
# Task 1: Explorer
# -------------------------------------------------
task_fetch = Task(
    description=(
        "You are given a URL: {url}\n\n"
        "Use the web_fetcher tool to fetch the webpage content. "
        "Return ONLY the extracted plain text from the page."
    ),
    agent=explorer,
    expected_output="Plain text extracted from the webpage."
)

# -------------------------------------------------
# Task 2: Summarizer
# -------------------------------------------------
task_summarize = Task(
    description=(
        "You are given the extracted webpage text from the previous task.\n\n"
        "Your job:\n"
        "- Write 4–6 bullet points summarizing the key ideas\n"
        "- Write about the programming languages name do person know"
        "- Write one short summary paragraph\n\n"
        "Do NOT call tools."
    ),
    agent=summarizer,
    expected_output="Bullet points + short summary paragraph."
)

# -------------------------------------------------
# Task 3: Critic
# -------------------------------------------------
task_critic = Task(
    description=(
        "You are given the summary produced in the previous task.\n\n"
        "Your job:\n"
        "1. Critique the summary in 1–2 short paragraphs\n"
        "2. Provide EXACTLY 2 improvement suggestions\n\n"
        "Do NOT call tools unless absolutely necessary."
    ),
    agent=critic,
    expected_output="Critique + 2 improvement suggestions."
)

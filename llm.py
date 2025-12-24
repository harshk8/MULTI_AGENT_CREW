# llm.py
from crewai import LLM
import os

# avoid OpenAI auto-usage
os.environ.setdefault("CREWAI_DISABLE_OPENAI", "1")

ollama_llm = LLM(
    model="ollama/llama3.2",          # use a model you have in Ollama
    base_url="http://localhost:11434"
)

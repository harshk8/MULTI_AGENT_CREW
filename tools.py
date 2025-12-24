# tools.py
from crewai.tools import tool
import requests
from bs4 import BeautifulSoup
import re

@tool("web_fetcher")
def web_fetcher(url: str) -> str:
    """Fetch a webpage and return cleaned text (all the data from paragraphs) try to find online certification mentioned there."""
    print("### Web Fetcher fetching data")
    headers = {"User-Agent": "Mozilla/5.0 (+crewai-web-fetcher)"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    paragraphs = soup.find_all("p")
    text = "\n\n".join(p.get_text(strip=True) for p in paragraphs[:20])
    text = text[:4000]  # cap to avoid huge prompts
    print("### Text found: ", text)
    return text or "No meaningful text found on this page."


# @tool("calculator")
# def calculator(expr: str) -> str:
#     """Safely evaluate a simple arithmetic expression like '2 + 2 * 3'."""
#     expr = expr.strip()
#     if not re.match(r"^[0-9+\-*/().\s]+$", expr):
#         return "Invalid characters in expression."

#     try:
#         result = eval(expr, {"__builtins__": {}}, {})
#     except Exception as e:
#         return f"Error evaluating expression: {e}"

#     return f"{expr} = {result}"

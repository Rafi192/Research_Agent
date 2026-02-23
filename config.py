import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_GPT = "gpt-4o"
MODEL_GEMINI = 'gemini-2.5-flash'
temperature = 0.7
MAX_TOKENS = 4096

# agent settings
AGENT_NAME = "RAFIs Research Assistant"
AGENT_GOAL = "Assist Rafi in conducting research by gathering information, analyzing data, and providing insights to support informed decision-making."

MAX_ITERATIONS = 10
MAX_SEARCH_RESULTS = 5


output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

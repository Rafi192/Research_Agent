# test_config.py
import config
from tools.tools import web_search

print("Testing config.py imports...")
print(f"TAVILY_API_KEY: {config.TAVILY_API_KEY[:10] if config.TAVILY_API_KEY else 'NOT FOUND'}...")
# print(f"MODEL_NAME: {config.MODEL_NAME}")
print(f"MAX_ITERATIONS: {config.MAX_ITERATIONS}")
print(f"AGENT_NAME: {config.AGENT_NAME}")
print(web_search("What is the capital of France?"))
print("✅ Config loaded successfully!")
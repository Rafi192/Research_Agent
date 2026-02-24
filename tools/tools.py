import requests
from typing import List, Dict, Any
import wikipedia
from config import TAVILY_API_KEY
from config import MAX_SEARCH_RESULTS
from tavily import TavilyClient
import config
import os
from dotenv import load_dotenv
load_dotenv()

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def web_search(query: str) -> str:
    # it will search the web using Tavily API
    # args: Search query string
    # it will return search results

    try:
        response = tavily_client.search(
            query=query,
            max_results= MAX_SEARCH_RESULTS
        )

        if response.get('results') is None:
            return "error: No results found"

        return response
    
    except Exception as e:
        print(f"Error occured during web search : {e}")
        return "error "



# print(web_search("What is the capital of France?"))

def wikipedia_search():
    pass


def fetch_url():
    pass



def execute_tools():
    pass


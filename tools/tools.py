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

def wikipedia_search(query:str):
    try:
        search_results = wikipedia.search(query, results= 1)

        if not search_results:
            return "no result found from wikipedia"
        
        page_title = search_results[0]
        page_summary = wikipedia.summary(page_title, sentences=3)
        page_url = wikipedia.page(page_title).url

        result = f"wikipedia page title:{page_title}\n"
        result += f"{page_summary}\n"
        result += f"Read more: {page_url}"

        return result
    
    except Exception as e:
        print(f"Error occured during wikipedia search: {e}")
        return "error"


def fetch_url():
    pass



def execute_tools():
    pass


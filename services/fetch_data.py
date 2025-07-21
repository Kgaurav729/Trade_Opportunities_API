from duckduckgo_search import DDGS
from typing import List

def get_market_data(sector: str, max_results: int = 5) -> List[str]:
    query = f"latest news in Indian {sector} sector"
    results = []

    with DDGS() as ddgs:
        for result in ddgs.text(query, region='in-en', safesearch='Moderate', max_results=max_results):
            if "body" in result:
                results.append(result["body"])
    
    return results

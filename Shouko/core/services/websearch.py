from duckduckgo_search import DDGS

def web_search(query, max_results=3):
    ddgs = DDGS()
    results = []
    for r in ddgs.text(query, max_results=max_results):
        results.append({
            "title": r.get("title", ""),
            "href": r.get("href", ""),
            "body": r.get("body", ""),
            "image": r.get("image", None)
        })
        
    return results
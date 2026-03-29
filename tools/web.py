from ddgs import DDGS

def buscar_web(query):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=3))
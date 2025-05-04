from fastapi import FastAPI
from pydantic_models.chat_body import ChatBody
from services.search_service import SearchService

app = FastAPI()
search_service = SearchService()

# chat
@app.post("/chat")
def chat_endpoint(body: ChatBody):
    print("Endpoint hit with query:", body.query)
    search_result = search_service.web_search(body.query)
    print(search_result)
    # sort sources
    # LLM
    return body.query




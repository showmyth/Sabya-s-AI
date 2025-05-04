from config import Settings

settings = Settings()
print("TRAVILY KEY:", settings.TRAVILY_API_KEY)

class SearchService:
    def web_search(self, query: str):
        print("Inside web_search")
        print("Key from settings:", settings.TRAVILY_API_KEY)

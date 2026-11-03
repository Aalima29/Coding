import requests
import json

query=input("What type of news are you intrested in ! : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-09-15&sortBy=publishedAt&apiKey=6d264b3048d54e718c302681ff23856a"
r=requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------")
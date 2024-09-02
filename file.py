import json
from urllib.parse import urlsplit, parse_qsl
from serpapi import GoogleSearch
import pandas as pd
import schedule
import time
import os

if os.path.exists("_data/publications.json"):
    os.remove("_data/publications.json")
else:
    print("File does not exist")
author_article_results_data = []
api_key = open(".api.txt","r")

params = {
    "api_key": api_key,
    "engine": "google_scholar_author",
    "hl": "en",
    "sort": "pubdate",
    "author_id": "H0ZQKBsAAAAJ",
    "start": 0,
    "num": 100
}

articles_is_present = True

while articles_is_present:
    search = GoogleSearch(params)
    results = search.get_dict()

    for article in results.get("articles", []):
        year = article.get("year")
        print(year)
        if year and int(year) >= 2001:
            title = article.get("title")
            link = article.get("link")
            citation_id = article.get("citation_id")
            authors= article.get("authors")
            publication = article.get("publication")
            cited_by_value = article.get("cited_by", {}).get("value")
            cited_by_link = article.get("cited_by", {}).get("link")
            cited_by_cites_id = article.get("cited_by", {}).get("cites_id")

            author_article_results_data.append({
            "article_title": title,
            "article_link": link,
            "article_year": year,
            "article_citation_id": citation_id,
            "article_authors": authors,
            "article_publication": publication,
            "article_cited_by_value": cited_by_value,
            "article_cited_by_link": cited_by_link,
            "article_cited_by_cites_id": cited_by_cites_id,
            })

    if "next" not in results.get("serpapi_pagination", []):
        articles_is_present = False
    else:
        search.params_dict.update(dict(parse_qsl(urlsplit(results.get("serpapi_pagination").get("next")).query)))

print("Waiting for author articles to save..")
with open('_data/publications.json', 'a') as f:
    json.dump(author_article_results_data, f)
print("Author Articles Saved.")


os.system("git add _data/publications.json")


commit_msg = "Update every friday publications data"
os.system(f'git commit -a -m "{commit_msg}"')


os.system("git push")
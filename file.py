import json
from urllib.parse import urlsplit, parse_qsl
from serpapi import GoogleSearch
import os

if os.path.exists("_data/publications.json"):
    os.remove("_data/publications.json")
else:
    print("File does not exist")

author_article_results_data = []
api_key = open(".api.txt", "r").read().strip()

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
            authors = article.get("authors")
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

    # Check for pagination and update the parameters accordingly
    if "next" in results.get("serpapi_pagination", {}):
        next_page_url = results["serpapi_pagination"]["next"]
        next_params = dict(parse_qsl(urlsplit(next_page_url).query))
        params.update(next_params)
    else:
        articles_is_present = False

print("Waiting for author articles to save...")
with open('_data/publications.json', 'w') as f:  # Changed to 'w' to overwrite instead of append
    json.dump(author_article_results_data, f)
print("Author Articles Saved.")

os.system("git add _data/publications.json")

commit_msg = "update publications data"
os.system(f'git commit -a -m "{commit_msg}"')


os.system("git push")

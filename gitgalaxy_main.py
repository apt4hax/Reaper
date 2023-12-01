import requests
import glob
import time

def read_api_key():
    with open('.auth/github.keys', 'r') as file:
        return file.readline().strip()

def read_keywords_from_files():
    keywords = []
    for file in glob.glob('key/*.txt'):
        with open(file, 'r') as f:
            keywords.extend(f.read().splitlines())
    return keywords

def github_code_search(api_key, keyword):
    url = f"https://api.github.com/search/code?q={keyword}+in:file"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {api_key}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def gitgalaxy_main():
    api_key = read_api_key()
    keywords = read_keywords_from_files()
    results = {}

    for keyword in keywords:
        print(f"Searching for: {keyword}")
        result = github_code_search(api_key, keyword)
        if result:
            results[keyword] = result['items']
        time.sleep(66)

    with open('loot/github_search_results.txt', 'w') as file:
        for keyword, items in results.items():
            file.write(f"Keyword: {keyword}\n")
            for item in items:
                file.write(f"{item['html_url']}\n")
            file.write("\n")

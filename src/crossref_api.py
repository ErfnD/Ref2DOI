import requests
from requests.exceptions import ConnectionError

def get_doi(title: str):
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "rows": 1}
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            items = response.json()["message"]["items"]
            if items:
                return items[0].get("DOI")
    except ConnectionError as ce:
        None
    except requests.exceptions.Timeout:
        None
    return None

def get_title_from_doi(doi: str):
    if not doi or doi == "DOI_NOT_FOUND":
        return None
    url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['message']['title'][0]
    except ConnectionError as ce:
        None
    except requests.exceptions.Timeout:
        None
    return None

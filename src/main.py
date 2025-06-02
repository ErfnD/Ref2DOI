import os
from loading_bar import loading_bar
import requests
from input_handler import get_references_from_input, write_references_to_file
from anystyle_wrapper import parse_references_with_anystyle, extract_titles_from_json
from crossref_api import get_doi, get_title_from_doi
from utils import cleanup_temp_files, compare_lists

def main():
    references = get_references_from_input()
    write_references_to_file(references)

    parse_references_with_anystyle()
    titles = extract_titles_from_json()

    dois = []
    valid_titles = []
    total = len(titles)
    current = 0
    for title in titles:
        loading_bar(current, total, 'Processing References')
        doi = get_doi(title)
        dois.append(doi if doi else "DOI_NOT_FOUND")
        valid_title = get_title_from_doi(doi)
        valid_titles.append(valid_title)
        current += 1

    os.makedirs("exports", exist_ok=True)

    with open("./exports/titles.txt", "w", encoding="utf-8") as f:
        f.write("Extracted Titles:\n")
        for i, title in enumerate(titles, 1):
            f.write(f"{i}. {title}\n")

    with open("./exports/dois.txt", "w", encoding="utf-8") as f:
        f.write("DOIs:\n")
        f.write(", ".join(dois))

    diffs = compare_lists(titles, valid_titles)
    with open("./exports/differences.txt", "w", encoding="utf-8") as f:
        for index, val1, val2 in diffs:
            f.write(f"{index + 1}: you wanted -> {val1}, I exported -> {val2}\n")

    cleanup_temp_files("./tmp/references.txt", "./tmp/references.json")

    try:
        response = requests.get("https://google.com")
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[92mProcess completed successfully. You can access the results from "exports" folder.\n'
            '→ Extracted titles saved to: titles.txt\n'
            '→ DOIs saved to: dois.txt\n'
            '→ Differences between expected and exported titles saved to: differences.txt\n'
            '\033[0m')
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[92m→ Extracted titles saved to: titles.txt\n\033[0m'
            '\033[91m→ DOIs NOT extracted.\n'
            '→ Differences NOT extracted.\n'
            'There is a problem with your internet connection\n\033[0m')

if __name__ == "__main__":
    main()
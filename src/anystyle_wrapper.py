import os
import json

def parse_references_with_anystyle(input_file="./tmp/references.txt", output_file="./tmp/references.json"):
    command = f'anystyle parse "{input_file}" > "{output_file}"'
    exit_code = os.system(command)
    if exit_code != 0:
        print("An error occurred while running anystyle.")
        exit(1)

def extract_titles_from_json(json_file="./tmp/references.json"):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    titles = []
    for ref in data:
        title = ref.get("title")
        if title:
            if isinstance(title, list):
                titles.append(" ".join(title))
            else:
                titles.append(title)
    return titles

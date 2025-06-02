import os

def get_references_from_input():
    print("Enter references one per line. Press Enter on an empty line to finish input:")
    references = []
    while True:
        line = input()
        if line.strip() == "":
            break
        references.append(line.strip())
    os.system('cls' if os.name == 'nt' else 'clear')
    return references

def write_references_to_file(references: list, filename="./tmp/references.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for ref in references:
            f.write(ref + '\n')

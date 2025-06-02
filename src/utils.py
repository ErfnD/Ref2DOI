import os

def cleanup_temp_files(*files):
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass

def compare_lists(list1: list[str], list2: list[str]):
    differences = []
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        if list2[i]:
            if list1[i].lower() != list2[i].lower():
                differences.append((i, list1[i], list2[i]))
    if len(list1) != len(list2):
        print("Warning: Lists have different lengths.")
    return differences

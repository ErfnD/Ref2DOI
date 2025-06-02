import os
import shutil

def cleanup_directory(dir_path):
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
        except PermissionError:
            pass
        except Exception as e:
            pass
    else:
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

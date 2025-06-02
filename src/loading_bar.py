import sys

RESET = '\033[0m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'

def loading_bar(current, total, text):
    length = 40
    filled_len = int(length * current // total)
    bar = GREEN + '█' * filled_len + RESET + YELLOW + '-' * (length - filled_len) + RESET
    percent = f"{(current / total) * 100:.0f}%".rjust(4)
    sys.stdout.write(f"\r{BLUE}{text}:{RESET} |{bar}| {percent}")
    sys.stdout.flush()
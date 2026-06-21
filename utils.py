import re

def extract_score(text):

    match = re.search(r'(\d+)/10', text)

    if match:
        return int(match.group(1))

    return 0
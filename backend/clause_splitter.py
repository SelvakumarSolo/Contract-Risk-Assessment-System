import re

def split_clauses(text):
    clauses = re.split(
        r'\n(?=\d+\.|\([a-z]\)|section\s\d+)', 
        text, 
        flags=re.IGNORECASE
    )
    return [c.strip() for c in clauses if len(c.strip()) > 40]


HIGH_RISK = [
    "unilateral termination",
    "without prior notice",
    "sole discretion",
    "in perpetuity",
    "non-compete",
    "irrevocable"
]

MEDIUM_RISK = [
    "penalty",
    "indemnify",
    "auto-renew",
    "exclusive",
    "liability"
]

def detect_risk(clause):
    clause = clause.lower()

    for word in HIGH_RISK:
        if word in clause:
            return "High"

    for word in MEDIUM_RISK:
        if word in clause:
            return "Medium"

    return "Low"

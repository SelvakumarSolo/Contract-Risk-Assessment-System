def calculate_contract_risk(risk_list):
    score = 0

    for risk in risk_list:
        if risk == "High":
            score += 3
        elif risk == "Medium":
            score += 2
        else:
            score += 1

    if score >= 25:
        return "HIGH RISK"
    elif score >= 15:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


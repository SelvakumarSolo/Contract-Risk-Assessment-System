def suggest_alternative(risk):
    if risk == "High":
        return "Consider adding mutual termination rights and prior notice period."
    elif risk == "Medium":
        return "Clarify scope and limit liability duration."
    else:
        return "Clause appears balanced."

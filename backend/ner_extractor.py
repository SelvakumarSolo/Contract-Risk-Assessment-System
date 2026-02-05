import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "Parties": [],
        "Dates": [],
        "Amounts": [],
        "Jurisdiction": []
    }

    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities["Parties"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["Dates"].append(ent.text)
        elif ent.label_ == "MONEY":
            entities["Amounts"].append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            entities["Jurisdiction"].append(ent.text)

    return entities


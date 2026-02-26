import spacy
from dataclasses import dataclass

nlp = spacy.load("en_core_web_sm")

@dataclass
class Requirement:
    variable: str
    operateur: str
    valeur: float
    unite: str


def extract_variable(doc):
    for token in doc:
        if token.dep_ == "nsubj":
            subtree = [
                t.text for t in token.subtree
                if t.pos_ != "DET" and not t.is_punct
            ]
            return " ".join(subtree)
    return None


def extract_operator(doc):
    text = doc.text.lower()
    if "must be" in text or "shall be" in text or "is" in text:
        return "="
    if "greater than" in text or "more than" in text:
        return ">"
    if "less than" in text or "lower than" in text or "must not exceed":
        return "<"
    return None


def extract_value_and_unit(doc):
    for token in doc:

        if token.pos_ == "NUM" or token.like_num or token.ent_type_ == "CARDINAL":
            try:
                valeur = float(token.text)
            except ValueError:
                continue

            unite = None

            if token.head.pos_ in {"NOUN", "PROPN"}:
                unite = token.head.text

            elif token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if next_token.pos_ in {"NOUN", "PROPN"}:
                    unite = next_token.text

            return valeur, unite

def requirement_extraction(texte: str) -> Requirement:
    doc = nlp(texte)
    variable = extract_variable(doc)
    operateur = extract_operator(doc)
    valeur, unite = extract_value_and_unit(doc)

    return Requirement(
        variable=variable,
        operateur=operateur,
        valeur=valeur,
        unite=unite
    )


if __name__ == "__main__":
    texte = "Battery power must be 650 Watts."
    texte2 = "The average repair time must not exceed 45 minutes."
    print(requirement_extraction(texte))
    print(requirement_extraction(texte2))
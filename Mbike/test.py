import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp("The average repair time must not exceed 45 minutes..")
print([(w.text, w.pos_) for w in doc])
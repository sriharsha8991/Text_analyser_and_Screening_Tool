import spacy
import pandas as pd

nlp = spacy.load('en_core_web_sm')

def named_entity_recognition(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return pd.DataFrame(entities, columns=['Entity', 'Type'])

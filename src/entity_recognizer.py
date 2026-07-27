import spacy

nlp=spacy.load("en_core_web_sm")


def extract_entities(sentence):

    doc=nlp(sentence)

    entities=[]

    for entity in doc.ents:

        entities.append ({
            "text":entity.text,
            "label":entity.label_
        })

    
    return entities
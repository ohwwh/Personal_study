import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize(name):
    l = len(name)
    ret = 'X' * l
    return ret
    

def anonymize_text(sentences):
    ret = ""
    doc = nlp(sentences)
    l = len(doc)
    i = 0
    for e in doc:
        if e.ent_type_ == "PERSON":
            ret += anonymize(e)
            if e.head.ent_type_ == "PERSON":
                ret += "X"
            elif e.head.ent_type_ != "PERSON" and i < l - 1 and e.text_with_ws != e.text:
                ret += " "
        else:
            ret += e.text
            if i < l - 1 and e.text_with_ws != e.text:
                ret += " "
        i += 1
    return ret

print(anonymize_text("XXXX eats an...did something"))
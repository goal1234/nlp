import spacy
nlp = spacy.load("en_core_web_lg")
from collections import Counter

'''
    doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
    
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)    
'''

def label_ner(doc):
    if type(doc)!=spacy.tokens.doc.Doc:
        return "检查类型:spacy.tokens.doc.Doc!!"
    text = []
    label = []
    for ent in doc.ents:
        text.append(ent.text)
        label.append(ent.label_)

    res = list(zip(text, label))
    return res


def most_list(person):
	a = Counter(person)
	b = list(a.most_common(3))
	freq3 = [i[0] for i in b]
	return freq3



def person_location(t):
    doc = nlp(t)
    z = label_ner(doc)
    person = [i[0] for i in z if i[1] == 'PERSON']
    location = [i[0] for i in z if i[1] == 'LOC']
    person = most_list(person)
    location = most_list(location)
    return person, location


def per_Location(filtered2):
    test = [" ".join(i) for i in filtered2]
    res_person = []
    res_location = []
    for i in test:
        person, location = person_location(i)
        res_person.append(person)
        res_location.append(location)
    res_person = [" ".join(i) for i in res_person]
    res_location = [" ".join(i) for i in res_location]
    return res_person, res_location

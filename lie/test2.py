import nltk
import numpy as np
from prepare import removeStop
from prepare import removeNer
from sentiClassify import sentiment
from nltk.corpus import stopwords

from most_freq import rm_sword
# 对一篇文章中的每段进行相关的情感分析之后进行


from prepare import stopwordslist
from prepare import remove_stoplist
from most_freq import flatten_str

path = r'data/stop2.txt'


stop_word = stopwordslist(path)
rm1 = [flatten_str(i) for i in content]
tokens= [nltk.word_tokenize(i) for i in rm1]

def ff(tokens):
    a = ['``', '»', '«', '–', 'm', 'I', 'Ms.', 'the', 'of', 'Mr.','.','və','’'
         '•','I']
    a.extend(stop_word)
    a.extend(stopwords.words())
    filtered2 = []
    for i in tokens:
        fi = [j for j in i if j not in a]
        filtered2.append(fi)
    return filtered2



filtered2 = ff(tokens)

top5 = [most_freq(i) for i in filtered2]

def get_sent(rm_s):
    test = removeNer(rm_s)
    input_sent = test.remove_ner()
    res_sent = sentiment(input_sent)
    return res_sent


sent = [get_sent(i) for i in filtered2]
res_pos = [i['pos'] for i in sent]
res_neu = [i['neu'] for i in sent]
res_neg = [i['neg'] for i in sent]


'''
from sta import p_l_s
# 通过stanfordnlp进行实体识别
get_pls =[]
count = int(1)
for i in filtered2:
    print(count)
    z =" ".join(i)
    zz = nlp.ner(z)
    get_pls.append(zz)
    count +=1

person=[i[0] for i in get_pls]
location=[i[1] for i in get_pls]
state=[i[2] for i in get_pls]

'''

'''
res_person = []
res_location =[]
for i in filtered2:
    aaa = removeNer(i)
    person = aaa.get_person()
    location = aaa.get_loaction()
    res_person.append(person)
    res_location.append(location)

'''

# ---spacy版本
res_person = []
res_location = []






# ---
'''
# ---nltk中进行的人名，地点提取
res_person = []
res_location =[]
for i in filtered2:
    aaa = removeNer(i)
    person = aaa.get_person()
    location = aaa.get_loaction()
    res_person.append(person)
    res_location.append(location)
    # ---进行后面的鬼鬼，数据合并

def na_replace(list_np):
    rd2 = [round(i*100,2) for i in list_np]
    temp = np.array(rd2)
    index_nan = np.isnan(temp)
    index_inf = np.isinf(temp)
    temp[index_nan] = float(0)
    temp[index_inf] = float(0)
    out_list = [i.item() for i in temp]
    return out_list


res_pos1 = na_replace(res_pos)
res_neu1 = na_replace(res_neu)
res_neg1 = na_replace(res_neg)

'''


pos_neg = []
for i in range(res_pos.__len__()):
    if res_pos[i] > res_neg[i]:
        ispos = int(1)
    else:
        ispos = int(0)
    pos_neg.append(ispos)


res_person1 = [",".join(i) for i in res_person]
res_location1 = [",".join(i) for i in res_location]

tt = zip(res_pos, res_neu,res_neg, pos_neg, top5, res_person1, res_location1, id_find, article1)
to_sql = list(tt)


len(res_person)

import pickle
f = open('dump.txt', 'wb')
pickle.dump(to_sql,f)

f = open('content.txt', 'wb')
pickle.dump(content, f)
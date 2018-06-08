import nltk
import langid
import numpy as np
from prepare import removeStop
from prepare import removeNer
from sentiClassify import sentiment


path = r'data/stopwords.txt'

# 对一篇文章中的每段进行相关的情感分析之后进行
count = int(1)
res_pos = []
res_neg = []
res_neu = []
for i in nlp_data:
    print(count)
    str1 = flatten_str(i)
    tokens = nltk.word_tokenize(str1)
    rm = removeStop(tokens, path)
    rm_s = rm.remove_stoplist()

    test = removeNer(rm_s)
    input_sent = test.remove_ner()
    res_sent = sentiment(input_sent)
    res_pos.append(res_sent['pos'])
    res_neg.append(res_sent['neg'])
    res_neu.append(res_sent['neu'])
    count += 1



# ---nltk中进行的人名，地点提取
res_person = []
res_location =[]
for i in nlp_data:
    str1 = flatten_str(i)
    tokens = nltk.word_tokenize(str1)
    rm = removeStop(tokens, path)
    rm_s = rm.remove_stoplist()

    aaa = removeNer(rm_s)
    person = aaa.get_person()
    location = aaa.get_loaction()
    res_person.append(person)
    res_location.append(location)

from collections import Counter
# 去除重复值进行
def most_list(res_person):
    a =Counter(res_person)
    temp =a.most_common(3)
    person3 =[i[0] for i in temp]
    return person3

res_person1 = [most_list(i) for i in res_person]
res_location1 = [most_list(i) for i in res_location]

res_person1 = [",".join(list(set(i))) for i in res_person1]
res_location1 = [",".join(list(set(i))) for i in res_location1]



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

tt = zip(res_pos1, res_neu1, res_neg1, top5, res_person1, res_location1, sim_where, article)
to_sql = list(tt)




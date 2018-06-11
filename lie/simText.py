'''
文章相似度：
@:input: 传入一系列文章
@:return: 相似文章的数量，文章在第几个-通过id返回iid到数据库里面去
'''


from gensim import corpora, models, similarities
from most_freq import flatten_str
import nltk
from prepare import removeStop

def rm_stop_sim(test):
    '''

    :param test:
    :return:
    '''
    path = r'data/stopwords.txt'
    t = flatten_str(test)
    tokens = nltk.word_tokenize(t)
    rm = removeStop(tokens, path)
    rm_s = rm.remove_stoplist()
    return rm_s


def make_today(nlp_data):
    '''

    :param nlp_data:去除停词之后的[[a],[b],[c]]
    :return:
    '''
    dictionary = corpora.Dictionary(nlp_data)
    corpus = [dictionary.doc2bow(i) for i in nlp_data]
    tfidf = models.TfidfModel(corpus)

    tfidf_for_lsi = tfidf[corpus]
    lsi = models.LsiModel(tfidf_for_lsi, id2word=dictionary,num_topics=200)
    index = similarities.MatrixSimilarity(lsi[corpus])

    # 这个要封装在前面的公式里现在还没有进行
    out = []
    articled = []
    print("...")
    for i in range(tfidf_for_lsi.__len__()):
        sim = index[lsi[tfidf_for_lsi[i]]]
        position, art_count = get_(sim)
        out.append(position)
        articled.append(art_count)
    return out, articled



def get_(sim):
    '''

    :param sim:
    :return:
    '''
    # 0.25
    res = sorted(enumerate(sim), key=lambda item: -item[1])
    rule = res[1:]
    like = [i for i in rule if i[1] > 0.7]
    if like:
        count_sim = int(len(like))
        out = [i[0] for i in like]
    else:
        count_sim = int(0)
        out = int(0)
    return out, count_sim



out, article1 = make_today(filtered2)

def where_sim(out):
    res = []
    for i in out:
        if isinstance(i, list):
            temp = ",".join(map(str, i))
        else:
            temp = str(i)

        res.append(temp)
    return res

sim_where = where_sim(out)



where = list(zip(iid, content))


def find_iid(out):
    id_where = []
    for i in out:
        if i == 0:
            one_id = "have nothing"
        else:
            one_id = str()
            for j in i:
                print(j)
                iid2 = str(where[j][0])
                one_id += iid2 + ","
        id_where.append(one_id)
    return id_where


id_find = find_iid(out)
'''
文章相似度：
@:input: 传入一系列文章
@:return: 相似文章的数量，文章在第几个-通过id返回iid到数据库里面去
'''


from gensim import corpora,models,similarities
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

    :param nlp_data:
    :return:
    '''
    today_doc = [rm_stop_sim(i) for i in nlp_data]
    dictionary = corpora.Dictionary(today_doc)
    corpus = [dictionary.doc2bow(i) for i in today_doc]
    tfidf = models.TfidfModel(corpus)
    tfidf_cor = tfidf[corpus]
    return tfidf_cor, tfidf, corpus


def lsi_matrix(nlp_data):
    '''

    :param nlp_data:
    :return:
    '''
    tfidf_cor, tfidf, corpus = make_today(nlp_data)
    tfidf_for_lsi = tfidf[corpus]
    lsi = models.LsiModel(tfidf_for_lsi, num_topics=len(tfidf_cor))
    index = similarities.MatrixSimilarity(lsi[corpus])
    return index


def get_(sim):
    '''
    
    :param sim:
    :return:
    '''
    # 0.25
    res = sorted(enumerate(sim), key=lambda item: -item[1])
    rule = res[1:]
    like = [i for i in rule if i[1] > 0.3]
    if like:
        count_sim = int(len(like))
        out = [i[0] for i in like]
    else:
        count_sim = int(0)
        out = int(0)
    return out, count_sim


index = lsi_matrix(nlp_data=nlp_data)

# 这个要封装在前面的公式里现在还没有进行
out = []
article = []
print("...")
for i in range(tfidf_for_lsi.__len__()):
    sim = index[lsi[tfidf_for_lsi[i]]]
    position, art_count = get_(sim)
    out.append(position)
    article.append(art_count)


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
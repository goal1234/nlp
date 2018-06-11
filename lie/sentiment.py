'''

输入数据:
nlp_data   list

1.进行情感分析
    通过nktk进行的wordnent，韦德字典，这个已经自动实现了,无监督的情感打分
    1.1分词
    1.2实体命名识别
    1.3去除时间，地点等
    1.4停用词处理
    1.5进行打分
2.
'''

import nltk
from prepare import removeNer
from prepare import removeStop

from nltk.sentiment.vader import SentimentIntensityAnalyzer


nlp_data

# 测试数据
test = nlp_data[23]
tokens = nltk.word_tokenize(" ".join(test))
print(tokens)


path = r'data/stopwords.txt'

tokens = nltk.word_tokenize(" ".join(test))
rm = removeStop(tokens, path)
a = rm.remove_stoplist()

test = removeNer(a)
input_sent = test.remove_ner()



def sentiment(input_sent):
    '''

    :param input_sent:去除停词还有实体之后的list
    :return: 返回一个情感字典
    '''
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(" ".join(input_sent))
    return ss






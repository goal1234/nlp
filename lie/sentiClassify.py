
'''
    存放情感分析，目前在无监督的下,nltk提供了一个分类
    输出的是字典，同时有三个得分pos,neu,neg，还有文章复杂度这个没有进行
'''


from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(input_sent):
    '''

    :param input_sent:去除停词还有实体之后的list
    :return: 返回一个情感字典
    '''
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(" ".join(input_sent))
    return ss





## ---进行词频统计
import nltk
from prepare import removeStop


def flatten_str(test):
    '''
    :param test: [[a],[b],[c]]
    :return: 'abc'
    '''
    t = str()
    for i in test:
        t += " " + i
    return t


def rm_sword(test):
    '''
    :param test:['a','b','c']
    :return:[a,b,c]
    '''
    path = r'data/stopwords.txt'
    rm = removeStop(tokens, path)
    rm_s = rm.remove_stoplist()
    return  rm_s


def most_freq(rm_s):
    '''
    :param test: [str1,str2,str3]
    :return:
    '''

    words = nltk.FreqDist(rm_s)
    vocab = words.most_common(5)

    top5 = str()
    for i in vocab:
        top5+=i[0] + " "

    return top5


def every_top5(nlp_data):
    '''
    :param nlp_data: [[a],[b],[c]]
    :return: [[top5],[top5],[top5]]
    '''
    count = int(1)
    top5 = []
    for i in nlp_data:
        print(count)
        one = most_freq(i)
        top5.append(one)
        count+=1
    return top5



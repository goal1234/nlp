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
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nlp_data

# 测试数据
test = nlp_data[23]
tokens = nltk.word_tokenize(" ".join(test))
print(tokens)

# 停用词
def stopwordslist(filepath):
    '''
    各种标点符号
    :param filepath:文件路径
    :return:
    '''
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords

path = r'data/stopwords.txt'

filtered = [w for w in tokens if w not in stopwords.words('english')]
filtered = [w for w in filtered if w not in stopwordslist(path)]



# 词性标注
tokens = nltk.pos_tag(filtered)
print(tokens)


# 实体命名识别
entity = nltk.chunk.ne_chunk(tokens)
tidy = list(entity)

def get_ner(tidy, what):
    '''

    :param tidy:输入的一个实体命名树为nltk.tree格式
    :param what: 识别里面有神马：['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE', 'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']
    :return:
    '''
    gpe = []
    for i in tidy:
        i = str(i)
        if i.find(what) == 1:
            i = i.replace(what+" ","")
            i = i.replace("(", "")
            i = i.replace(")", "")
            i = i.replace("/", ",")
            gpe.append(i)
    return gpe

def tidy_ner(gpe):
    '''对上一步的进行清理'''
    res = []
    for i in gpe:
        if len(i.split(" ")) < 2:
            temp1 = i.split(",")[0]
        else:
            more = i.split(" ")
            for_store = []
            for j in more:
                first = j.split(",")[0]
                for_store.append(first)
                temp1 = " ".join(for_store)
        res.append(temp1)
    return res



remove = []
what = ['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE', 'CARDINAL',
        'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']
for i in what:
    for_tidy = get_ner(tidy, i)
    rm = tidy_ner(for_tidy)
    remove.extend(rm)

# 进行情感分析
input_sent = [w for w in filtered if w not in remove]




sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(" ".join(input_sent))
ss['neg']
ss['neu']
ss['pos']


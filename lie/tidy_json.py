import pandas as pd
import json

# 读入一个测试数据
temp = pd.read_csv('data/export2.csv')
content = temp[['content']]
test = content.iloc[2,]


'''
    var = test.content
    t = clearn_margin(var)
    res = clearn_prepare(t)
    store = clearn_get_content(res)
    
'''

def clearn_margin(var):
    # 去掉左 '[        右边]'
    str_len = len(var) - int(1)
    json_input = var[1:str_len]
    t = json_input.split("},")
    return t

def clearn_prepare(t):
    res = []
    for i in t:
        temp1 = i + "}"
        res.append(temp1)

    # 去掉最后一个的{
    len1 = len(res) - int(1)
    res[len1] = res[len1][:-1]
    return res

def clearn_get_content(res):
    # 返回一个list对象里面没有加入<br>进行相关的链接
    store = []
    for i in res:
        json_tidy = json.loads(i)
        cont = json_tidy['type']
        if cont =='paragraphs':
            store.append(json_tidy["content"])
    return store

def clearn(input):
    t = clearn_margin(input)
    res = clearn_prepare(t)
    store = clearn_get_content(res)
    return store

nlp_data = []

int11 = int(temp.__len__())
for i in range(300):
    test = content.iloc[i,]
    print(i)
    store = clearn(test.content)
    nlp_data.append(store)

def cl(test):
    out_clearn = str()
    for i in test:
        out_clearn += i + "<br>"
    return out_clearn


out_json = list(map(cl, nlp_data))



#temp['tidy_json'] = out_json
from stanfordcorenlp import StanfordCoreNLP
from collections import Counter


def flatten_str(test):
    '''
    :param test: [[a],[b],[c]]
    :return: 'abc'
    '''
    t = str()
    for i in test:
        t += " " + i
    return t

nlp = StanfordCoreNLP(r'F:\nlpdata\stanford-corenlp-full-2018-02-27', lang='en')
def ner(rm_s):
	'''
	
	:param rm_s: ['Anguillian', 'craftsman', 'swimming', 'pool', 'specialist']
	:return: [a,b,c]
	'''
	i = " ".join(rm_s)
	z = nlp.ner(i)
	person = [i[0] for i in z if i[1] == "PERSON"]
	location = [i[0] for i in z if i[1] == "LOCATION"]
	numer = [i[0] for i in z if i[1] == "NUMBER"]
	state = [i[0] for i in z if i[1] == "STATE_OR_PROVINCE"]
	return person, location, numer, state

p=[]
count = int(1)

def most_list(person):
	a = Counter(person)
	b = list(a.most_common(3))
	freq3 = [i[0] for i in b]
	return freq3



def p_l_s(rm_s):
	'''

	:param i: 输入一篇文章为多个嵌套的列表[[],[]]的形式
	:return:
	'''

	# 进行实体命名识别同时
	person, location, numer, state = ner(rm_s)
	person = most_list(person)
	location = most_list(location)
	state = most_list(state)

	return person,location,state



'''
get_pls = [p_l_s(i) for i in nlp_data]

person = [i[0] for i in get_pls]
location=[i[1] for i in get_pls]
state = [i[2] for i in get_pls]
'''





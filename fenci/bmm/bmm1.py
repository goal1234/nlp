'''
逆向
最大匹配算法

readDict,printResult公式少了两个
'''

def BMM(wordDict, maxWordLength, sentence):
    '''

    :param wordDict: 分词字典
    :param maxWordLength: 最大词长度
    :param sentence: 带分句子,不要标点符号
    :return: 分词结果
    '''

    result = []
    while len(sentence) != 0:
        # 最大词长大于待 分句子是，重置最大词长
        if len(sentence) < maxWordLength:
            maxWordLength = len(sentence)
        # 待分子句

        segWord = sentence[len(sentence) - maxWordLength:len(sentence)]

        while not(segWord in wordDict):
            # while 循环结束两种情况，1是segWord存在字典中
            # 2是 segWord为单字
            if len(segWord) > 1:
                segWord = segWord[1:]
            else:
                #result.append(segWord)
                #sentence = sentence[:len(sentence)-1]
                break

        result.append(segWord)
        sentence = sentence[:len(sentence)-len(segWord)]

    return result


def main():
    maxWordLength, sougoDict = readDict("sougoDict.txt")
    sentence1 = "今天天气怎么样"
    result1 = BMM(sougoDict, maxWordLength, sentence1)
    printResult(result1)


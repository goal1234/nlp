'''
经过相关的符号处理
同时需要依靠相关的字典进行
'''

import re

def PreProcess(sentence, edcode = "utf-8"):
    # sentence = sentence.decode(edcode)
    sentence = re.sub(u'[]。，【】{}《》：；！@#￥%…………&*（）——+|]', "",sentence)
    return sentence


def FMM(sentence, diction, result=[],
        maxwordLength=4, edcode="utf-8"):
    i = 0
    sentence = PreProcess(sentence, edcode)
    length = len(sentence)
    while i < length:
        # find the ascii word
        tempi = i
        tok = sentence[i:i + 1]
        while re.search("[0-9A-Za-z/-/+#@_/.]{1}", tok) != None:
            i = i + 1
            tok = sentence[i:i + 1]
        if i - tempi > 0:
            result.append(sentence[tempi:i].lower().encode(edcode))
            # find chinese word
        left = len(sentence[i:])
        if left == 1:
            """go to 4 step over the FMM"""
            """should we add the last one? Yes, if not blank"""
            if sentence[i:] != " ":
                result.append(sentence[i:].encode(edcode))
            return result
        m = min(left, maxwordLength)

        for j in range(m, 0, -1):
            leftword = sentence[i:j + i].encode(edcode)
            #   print leftword.decode(edcode)
            if LookUp(leftword, diction):
                # find the left word in dictionary
                # it's the right one
                i = j + i
                result.append(leftword)
                break
            elif j == 1:
                """only one word, add into result, if not blank"""
                if leftword.decode(edcode) != " ":
                    result.append(leftword)
                i = i + 1
            else:
                continue
    return result


def LookUp(word, dictionary):
    if dictionary.get(word):
        return True
    return False


def ConvertGBKtoUTF(sentence):
    # return sentence.decode('gbk').encode('utf-8')
    return sentence



def test():
    dictions = {}
    dictions["ab"] = 1
    dictions["cd"] = 2
    dictions["abc"] = 1
    dictions["ss"] = 1
    dictions[ConvertGBKtoUTF("好的")] = 1
    dictions[ConvertGBKtoUTF("真的")] = 1
    sentence = "asdfa好的是这样吗vasdiw呀真的daf dasfiw asid是吗？"
    s = FMM(ConvertGBKtoUTF(sentence),dictions)
    for i in s:
        print(i.decode("utf-8"))


with open("text.txt", 'r') as f:
    for line in f:
        s = FMM(ConvertGBKtoUTF(line), dictions)
        for i in s:
            print(i.decode("utf-8"))
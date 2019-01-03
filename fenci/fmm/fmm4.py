lexicon = ('共同','创造','美好','的','新','生活') # 为了方便，词典直接写在程序里。
wordSeg = []    # 新建列表存放切分好的词
maxWordLen = 3  # 最大词长设为3


with open('test.txt','r', encoding='utf-8') as src:
    sentence = src.read()
    sentenceLen = len(sentence)
    wordLen = min(maxWordLen, sentenceLen)
    startPoint = 0
    while startPoint < sentenceLen:  # 从第一个字符循环到最后一个字符
        matched = False  # 假设找不到匹配的词
        for i in range(maxWordLen, 0, -1):  # 从最大词长3递减到1
            string = sentence[startPoint:startPoint + i]  # 取startPoint开始到startPoint+i-1的切片
            if string in lexicon:
                wordSeg.append(string)
                matched = True
                break
            
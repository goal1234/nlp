import nltk
from nltk.corpus import stopwords


class removeStop():
    def __init__(self, str_input, path):
        self.path = path
        self.tokens = str_input

    # 停用词
    def __stopwordslist(self):
        '''
        各种标点符号
        :param filepath:文件路径
        :return:
        '''
        try:
            stopwords = [line.strip() for line in open(self.path, 'r').readlines()]
        except Exception as e:
            print("检查的的文件路径在path上")
        return stopwords


    def remove_stoplist(self):
        a = ['``','»', '«','–','m','I', 'Ms.']
        filtered = [w for w in self.tokens if w not in stopwords.words('english')]
        filtered = [w for w in filtered if w not in self.__stopwordslist()]
        filtered = [w for w in filtered if w not in a]
        return filtered


class removeNer():
    '''
        输入：['However', 'Ciech', 'Group', 'spokesman', 'Miroslaw']列表

    '''

    def __init__(self, rm_stop):
        self.rm_stop = rm_stop

    def ner(self):
        '''

        :return:词性标注的表，对于每一个元组有DATE,MONEY等这样的实体词在里面会被清楚了
        '''

        # 词性标注
        tokens = nltk.pos_tag(self.rm_stop)

        # 实体命名识别
        entity = nltk.chunk.ne_chunk(tokens)
        tidy = list(entity)
        return tidy


    def __get_ner(self, tidy, what):
        '''

        :param tidy:输入的一个实体命名树为nltk.tree格式
        :param what: 识别里面有神马：['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE', 'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']
        :return:一个被清理过的列表
        '''

        if isinstance(what, str)==False:
            return "请输入实体并且为字符型,选项在下面\n" \
                   "['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE', 'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']"

        ner_list = []
        for i in tidy:
            i = str(i)
            if i.find(what) == 1:
                i = i.replace(what+" ","")
                i = i.replace("(", "")
                i = i.replace(")", "")
                i = i.replace("/", ",")
                ner_list.append(i)
        return ner_list

    def tidy_ner(self, gpe):
        '''将输入的树形数据结构中，查找出实体
            可以在直接调用对于上面['LOCATION, PERSON...]
            test = RemoveNer(rm_stop)
            GPE = test.tidy_ner('GPE')

        '''
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

    def remove_ner(self):
        '''
        调用上面的方法进行为韦德字典进行后面的情感输出
        :return:
        '''
        rm_data = []
        tidy = self.ner()
        dd = ['LOCATION', 'ORGANIZATION', 'PERSON', 'DURATION','DATE',
              'CARDINAL', 'PERCENT', 'MONEY', 'MEASURE', 'FACILITY', 'GPE']

        for i in dd:
            for_tidy = self.__get_ner(tidy, i)  # for tidy 返回空
            tidy1 = self.tidy_ner(for_tidy)
            rm_data.extend(tidy1)

        # 清理完成后的list
        input_sent = [w for w in self.rm_stop if w not in rm_data]
        return input_sent

    def get_person(self):
        '''
        调用上面的方法进行为韦德字典进行后面的情感输出
        :return:
        '''
        tidy = self.ner()

        dd = 'PERSON'
        for_tidy = self.__get_ner(tidy, dd)  # for tidy 返回空
        tidy1 = self.tidy_ner(for_tidy)
        return tidy1

    def get_loaction(self):
        '''
        调用上面的方法进行为韦德字典进行后面的情感输出
        :return:
        '''
        rm_data = []
        tidy = self.ner()

        dd = 'LOCATION'
        for_tidy = self.__get_ner(tidy, dd)  # for tidy 返回空
        tidy1 = self.tidy_ner(for_tidy)
        return tidy1
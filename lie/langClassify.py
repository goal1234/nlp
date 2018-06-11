import langid

'''
    进入的的清理好了的str进行的，通过之模块得到的是输出的简称
    其中en， zh英文中文， 还有很多鬼鬼
'''

# ---test语言识别
s1 = '你好'
s2 = 'hello'
s3 = 'Flüssigkeiten zum Nassbehandeln von Wzenden Um mindestens die Geräusche zu reduzieren, ' \
     ' den Wärmeübergang. Die Erfindung sieht es vor, in die Düse (30) eine kleine Menge der aufzuheizenden Flüssigkeit einzusaugen und dadurch in der Düse (30) ' \
     'ein Kondensat-Dampfgemisch zu bilden. Alternativ oder zusätzlich kann hinter der Düse (30) ein Strömungsteiler vorgesehen sein, der die Strömungsgeschwindigkeit '

i = langid.classify(s1)
j = langid.classify(s2)
m = langid.classify(s3)

# ---进行语言识别
result = []
for i in nlp_data:
    print(i)
    res = langid.classify(str(i))
    result.append(res[0])



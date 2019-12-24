import json
import jieba.analyse
import numpy as np
import re
import docx
import jieba
import docx
from docx import Document

listhsh = []
listuden = []
listoutput = []

def calc_simhash(content):
    '''
    对一个文章，计算出他的simhash
    :param content:
    :return:
    '''
    # 结巴分词
    seg = jieba.cut(content)
    # 设置结巴的stopwords， 就是不需要进行处理或者是不重要的 string
    jieba.analyse.set_stop_words('./src/stopwords.txt')
    # 使用 extract 算法，计算出关键词和 关键词得分（权重）
    keyWord = jieba.analyse.extract_tags('|'.join(seg), topK=25, withWeight=True, allowPOS=())
    keyList = []
    for feature, weight in keyWord:
        weight = int(weight * 100)
        # 关键词hash化， 转化成 1和0
        feature = string_hash(feature)
        temp = []
        for i in feature:
            if(i == '1'):
                temp.append(weight)
            else:
                temp.append(-weight)
        # 计算每一个关键词的最终得分
        keyList.append(temp)

    # 计算整个文章中，找出的关键词（文中设置的是100），的得分相加
    list1 = np.sum(np.array(keyList), axis=0)

    if(keyList==[]): #编码读不出来
        return '00'
    simhash = ''
    for i in list1:
        if(i > 0):
            simhash = simhash + '1'
        else:
            simhash = simhash + '0'
    return simhash

def string_hash(source):  # 哈希算法的实现
    if source == "":
        return 0
    else:
        # ord()函数 return 字符的Unicode数值
        x = ord(source[0]) << 7
        m = 1000003  # 设置一个大的素数
        mask = 2 ** 128 - 1  # key值
        for c in source:  # 对每一个字符基于前面计算hash
            x = ((x * m) ^ ord(c)) & mask

        x ^= len(source)  #
        if x == -1:  # 证明超过精度
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]
    return str(x)

def hamming_dis(simhash1, simhash2):#计算汉明距离
    '''
    使用位运算，比较两个文章最终 关键hash
    :param simhash1:
    :param simhash2:
    :return:
    '''
    t1 = '0b' + simhash1
    t2 = '0b' + simhash2
    n=int(t1, 2) ^ int(t2, 2)
    i=0
    while n:
        n &= (n-1)
        i+=1
    return i

def similarity(diff_value):
    for i,item in enumerate(listoutput):
        if item == diff_value:
            index = i
    stdid = listuden[index]
    print('相似程度为',end = '')
    print(100 - diff_value,end = '')
    print('%')
    if diff_value < 10:
        print('与报告'+ stdid + '.docx'+'极度相似')
    elif diff_value < 30:
        print('与报告'+ stdid + '.docx'+'较为相似')
    elif diff_value < 100:
        print('与报告'+ stdid + '.docx'+'报告不像似')

def loadFont():
    f = open("contents.json", encoding='gbk')  #设置以gbk解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    cont = json.load(f)
    for num in cont:
         #注意多重结构的读取语法
        content = cont[num]['content']
        stdid = cont[num]['studentID']
        # print(content)
        # print(stdid)
        temhsh = calc_simhash(content)

        listhsh.append(temhsh)
        listuden.append(stdid)
        out = dict(zip(listuden,listhsh))
    return out

def aim2simhash():
    a = ''
    path = "D:\\cnm的实验报告\\实验1报告.docx" #可修改报告名
    document = Document(path)
    for paragraph in document.paragraphs:
        a = a + paragraph.text
    b = calc_simhash(a)
    return b

def compare(direc):
    b = aim2simhash()
    for key,value in direc.items():
        tem = hamming_dis(value,b)
        listoutput.append(tem)
        # print(key)
        # print(value)

a = loadFont()
# print(a)
# print(listhsh)
# print(listuden)

compare(a)
# print(listoutput)
similarity(min(listoutput))
# b = aim2simhash()
# print(b)


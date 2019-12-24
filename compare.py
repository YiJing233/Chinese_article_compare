import jieba
import jieba.analyse
import numpy as np
import re
import docx
import json

from ariticle_compare_in_simhash import calc_simhash
from ariticle_compare_in_simhash import hamming_dis
from ariticle_compare_in_simhash import string_hash

def similarity(diff_value):
    print('相似程度为',end = '')
    print(100 - diff_value)
    if diff_value < 10:
        print('报告极度相似')
    elif diff_value < 30:
        print('报告较为相似')
    elif diff_value < 100:
        print('报告不像似')

data = []
value = []

for line in open("data.txt","r"): #设置文件对象并读取每一行文件
    data.append(line)               #将每一行文件加入到list中

for line in data:
    line = line.split()
    value.append(hamming_dis(line(0),simhash2))

maximum = max(value)

similarity(maximum)
print("相似度最高文档：",end = '')
print(line(1))
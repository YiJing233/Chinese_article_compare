# -*- coding: utf-8 -*-
import time
import math
import os
import re
import sys
import os, os.path,shutil
 
txtPath = 'D:\\Code\\Leetcode\\Chinese_article_compare\\src\\'
txtPath = txtPath.encode('utf-8').decode('utf-8')
txtType = 'txt'
txtLists = os.listdir(txtPath) #列出文件夹下所有的目录与文件

txtFileRegex = re.compile( r'^.*\.(TXT|txt)$' )

for txt in txtLists:
    

# for txt in txtLists: 
#     f = open(txtPath + txt,'rb')  # 返回一个文件对象  
#     lines = f.readlines()  # 读取全部内容 ，并以列表方式返回    
#     print(txt) 
#     for row in range(5,len(lines)):
#         sqlfile = open('D:\\Code\\Leetcode\\Chinese_article_compare\\'+txt, "a") # 文件读写方式是追加
#         line_str = str(lines[row]).encode('gbk').decode('gbk')
#         lists = line_str.split(',')[0:1]+line_str.split(',')[6:16]        
#         sqlfile.writelines(str(' '.join(lists)) + "\n")
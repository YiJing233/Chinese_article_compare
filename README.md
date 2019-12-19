# Chinese_article_compare

## 环境配置

python 3.7.0及以上版本

第三方库:

jieba

numpy

python-docx

## 使用方法

- 将实验报告模板（docx文件）置入src文件夹中
- 将需要比对的目标docx文件置入与ariticle_compare_in_simhash.py相同的文件目录中

运行ariticle_compare_in_simhash.py

即可获得该篇实验报告与语料库中报告的相似度

## 实现流程：

1. 语料库（即src文件夹）中的docx文件全部转为txt文件，文本内容保存，图片、代码删除
2. 读取txt中的内容并计算其simhash值
3. 保存所有txt的simhash值和原文件名，便于后续索引
4. 将需要比对的docx文件进行1、2操作，得到simhash2值
5. 比对simhash2值和已经保存的simhash值库，输出比对结果

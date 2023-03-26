import os
import tkinter
import jieba
import zhon.hanzi
import collections
import nltk
from nltk.corpus import stopwords
import tkinter as tk
from tkinter import filedialog



#nltk.download('stopwords')
punc = zhon.hanzi.punctuation  #要去除的中文标点符号
baidu_stopwords = stopwords.words(os.path.abspath('.\dict\cn_stopwords.txt')) #导入停用词表
jieba.load_userdict('dict\教育论文分析字典.txt')    #导入自定义字典

root = tkinter.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()    #选择需要统计词频的文件
with open(file_path,encoding="utf-8") as fp:
    text = fp.read()

ls = jieba.lcut(text,cut_all=True)

newls = []
for i in ls:
    if len(i)>1:
        newls.append(i)

 #统计词频
counts = collections.Counter(newls)
for word in baidu_stopwords:  #去掉停用词
    counts.pop(word,0)

#需要输出前多少条？
print(counts.most_common(20))

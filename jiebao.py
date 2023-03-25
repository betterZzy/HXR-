import jieba
import zhon.hanzi
import collections
import nltk
from nltk.corpus import stopwords

#nltk.download('stopwords')
punc = zhon.hanzi.punctuation  #要去除的中文标点符号
baidu_stopwords = stopwords.words('D:\Soft\SoftInstall\Microsoft VS Code\pythonPack\cn_stopwords.txt') #导入停用词表

with open('D:\硕士毕业论文\新建文本文档.txt',encoding="utf-8") as fp:
    text = fp.read()

jieba.load_userdict('D:\Soft\SoftInstall\Microsoft VS Code\pythonPack\dict\教育论文分析字典.txt')
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

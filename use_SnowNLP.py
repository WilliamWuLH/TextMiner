from numpy.lib.arraysetops import in1d
from pandas.core.tools import numeric
import streamlit as st
import numpy as np
import pandas as pd

from snownlp import SnowNLP
import matplotlib.pyplot as plt
from PIL import Image
#
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

text_show = '这部电影真心棒，全程无尿点\$这部电影简直烂到爆\$这部电影真不错\$太差劲了吧这个\$我觉得不行啊\$这部电影我爱了\$这部电影不太行\$这部电影一般般吧'
text_example = '这部电影真心棒，全程无尿点$这部电影简直烂到爆$这部电影真不错$太差劲了吧这个$我觉得不行啊$这部电影我爱了$这部电影不太行$这部电影一般般吧'

def Emotion_Judgment(*text):
    # 情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
    st.write('## 情绪判断')
    n = len(text)
    s = list(range(n))
    for i in range(n):
        str = text[i]
        if str == '':
            str = ' '
        s[i] = SnowNLP(str)
    #
    df1 = pd.DataFrame(
        columns = ['正面情绪的概率', '负面情绪的概率']
    )
    for i in range(n):
        # print(text[i], s[i].sentiments)
        df1.loc[text[i]] = s[i].sentiments, 1-s[i].sentiments
    
    st.table(df1)
    st.write('### 数据可视化：')
    st.bar_chart(df1)

    # [0,1] 越接近1表示正面情绪，越接近0表示负面情绪
    #  大于0.6   正面情绪
    #  小于0.4   负面情绪
    #  0.4-0.6  中性
    positive = 0
    negative = 0
    neutral = 0
    df2 = pd.DataFrame(
        columns = ['情绪评价']
    )
    for i in range(n):
        if s[i].sentiments > 0.6:
            df2.loc[text[i]] = "正面评价"
            positive += 1
        elif s[i].sentiments < 0.4:
            df2.loc[text[i]] = "负面评价"
            negative += 1
        else :
            df2.loc[text[i]] = "中立评价"
            neutral += 1
    st.table(df2)
    labels = "positive", "negative", "neutral"
    sizes = [positive, negative, neutral]
    explode = (0, 0.1, 0.1) # only ”explode” the 2nd slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write('### 数据可视化：')
    plt.savefig('./images/Emotion_Judgment.jpg')
    image = Image.open('./images/Emotion_Judgment.jpg')
    st.image(image, caption='Emotion_Judgment', use_column_width=True)

def Text_Emotion_Judgment():
    st.title('情绪判断')
    st.write('### 请输入您要判断的所有句子，不同句子之间请用 $ 隔开！')
    st.write('### 输入样例（包含有 8 个句子）：')
    st.write(text_show)

    in_text1 = st.text_input('请输入您要判断的所有句子：', text_example)
    in_text2 = in_text1.split('$')

    st.write('### 您输入的所有句子如下：')
    st.table(in_text2)

    if in_text1 == '':
        st.write('## 对不起，你没有输入文本嗷！')
    else:
        Emotion_Judgment(*in_text2)

if __name__ == "__main__":
    Text_Emotion_Judgment()
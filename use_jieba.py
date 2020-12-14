import streamlit as st
import numpy as np
import pandas as pd

import jieba
from jieba import analyse

text1 = "新华社北京5月31日电6月1日出版的第11期《求是》杂志将发表中共中央总书记、国家主席、中央军委主席习近平的重要文章《关于全面建成小康社会补短板问题》。"
text2 = "XX在湖南大学新闻传播与影视艺术学院学习，擅长大数据、云计算，没事喜欢闲逛岳麓山、橘子洲，饿了喜欢去登高路吃帅哥烧饼！"
text3 = "线程是程序执行时的最小单位，它是进程的一个执行流，是CPU调度和分派的基本单位，一个进程可以由很多个线程组成，线程间共享进程的所有资源，每个线程有自己的堆栈和局部变量。线程由CPU独立调度执行，在多CPU环境下就允许多个线程同时运行。同样多线程也可以实现并发操作，每个请求分配一个线程来处理。"

def Base_TF_IDF(text = text3, k = 5):
    # 引入TF-IDF关键词抽取接口
    tfidf = analyse.extract_tags

    # 基于TF-IDF算法进行关键词抽取
    keywords = tfidf(text,topK = k, withWeight = True)

    st.write('## 基于TF-IDF算法进行关键词抽取')

    if len(keywords) == 0:
        st.write('### 对不起，暂时无法进行关键词抽取')
        return

    Keyword = list(i[0] for i in keywords)
    Weight = list(i[1] for i in keywords)

    # 输出抽取出的关键词
    df1 = pd.DataFrame(
        columns = ['Weight']
    )
    for keyword in keywords:
        df1.loc[keyword[0]] = keyword[1]
    # st.write(df1)
    #
    df2 = pd.DataFrame(
        columns = Keyword
    )
    df2.loc['Weight'] = Weight
    #
    st.table(df2)
    st.bar_chart(df1)
    # st.area_chart(df1)
    # st.line_chart(df1)

def Base_TextRank(text = text3, k = 5):
    # 引入TextRank关键词抽取接口
    textrank = analyse.textrank

    #基于TextRank算法进行关键词抽取
    keywords = textrank(text, topK = k, withWeight = True)

    st.write('## 基于TextRank算法进行关键词抽取')

    if len(keywords) == 0:
        st.write('### 对不起，暂时无法进行关键词抽取')
        return
    
    Keyword = list(i[0] for i in keywords)
    Weight = list(i[1] for i in keywords)

    # 输出抽取出的关键词
    df1 = pd.DataFrame(
        columns = ['Weight']
    )
    for keyword in keywords:
        df1.loc[keyword[0]] = keyword[1]
    # st.write(df1)
    #
    df2 = pd.DataFrame(
        columns = Keyword
    )
    df2.loc['Weight'] = Weight
    #
    st.table(df2)
    st.bar_chart(df1)
    # st.area_chart(df1)
    # st.line_chart(df1)

def Text_Keywords():
    st.title('关键词抽取')
    st.write('### 请输入您的原始文本')
    st.write('### 原始文本样例：')
    st.write(text3)
    in_text1 = st.text_input('请输入您的原始文本（最好是中文文本）：', text3)
    in_Number1 = st.number_input('请输入您要抽取出的关键词数量：', 4)

    Base_TF_IDF(in_text1, in_Number1)

    Base_TextRank(in_text1, in_Number1)

if __name__ == "__main__":
    Text_Keywords()
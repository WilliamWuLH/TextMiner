import streamlit as st
import numpy as np
import pandas as pd
from streamlit.proto.RootContainer_pb2 import MAIN

import wordcloud
import jieba
from PIL import Image

text1 = '在我看来,冬天是最不浪漫的季节,特别是南方的冬天,它看不到北方的银装素裹,冰天雪地;也看不到西部的万里荒漠,悄无人声.南方的冬天永远都只是一片萧条之色.天很冷很冷,却不带一丝湿润,浸入骨髓的冰凉仿佛要把身体的所有温暖都抽去,只留下如干絮般散漫的冷一团一团的塞在胸肺间.'
text2 = 'and that government of the people, by the people, for the people, shall not perish from the earth.'
text3 = '从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开'
text4 = 'Python is an interpreted, high-level and general-purpose programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.'

def Simple_generate(text = text1):
    # 创建词云对象，赋值给w，现在w就表示了一个词云对象
    #w = wordcloud.WordCloud()
    w = wordcloud.WordCloud(width=2000,
                            height=1500,
                            background_color='white',
                            font_path='msyh.ttc')

    # 调用jieba的lcut()方法对原始文本进行中文分词，得到string
    txtlist = jieba.cut(text)
    string = " ".join(txtlist)

    # 调用词云对象的generate方法，将文本传入
    w.generate(string)

    # 将生成的词云保存为output1.png图片文件，保存出到当前文件夹中
    w.to_file('./images/Simple_generate_wordcloud.png')

    st.write('## 生成词云')
    image = Image.open('./images/Simple_generate_wordcloud.png')
    st.image(image, caption='WordCloud', use_column_width=True)

def Text_Generate_WordCloud():
    st.title('生成词云')
    st.write('### 请输入您要生成词云的文本')
    st.write('### 输入样例：')
    st.write(text4)

    in_text1 = st.text_input('请输入您要生成词云的文本：', text4)

    if in_text1 == '':
        st.write('## 对不起，你没有输入文本嗷！')
    else:
        Simple_generate(in_text1)

if __name__ == "__main__":
    Text_Generate_WordCloud()
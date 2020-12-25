import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import use_jieba
import use_SnowNLP
import use_wordcloud

def Index_Text_Miner():
    st.title('Text Miner 文本矿工')
    image = Image.open('./images/TextMiner.png')
    st.image(image, caption='Text Miner')
    st.write('- developed by [WULH](http://www.wlhan.top/)\n- [Open Application](https://wulh-textminer.herokuapp.com/)\n- GitHub Repository : [WilliamWuLH/TextMiner](https://github.com/WilliamWuLH/TextMiner)')
    st.write('## What does Text Miner do?')
    st.write('- **对文本进行简单挖掘**\n- **进行数据可视化分析**')
    st.write('### 可进行的文本挖掘操作如下：\n- 关键词抽取\n- 情绪判断\n- 生成词云')
    st.write('## 请在左侧的选项栏选择你要进行的文本挖掘操作')

# --- index
st.sidebar.title('Text Miner 文本矿工')
st.sidebar.write('## 请选择你要进行的文本操作：')
option = st.sidebar.selectbox(
    '文本挖掘操作选择：',
    ['Text Miner', '关键词抽取', '情绪判断', '生成词云'])

if option == 'Text Miner':
    Index_Text_Miner()
elif option == '关键词抽取':
    use_jieba.Text_Keywords()
elif option == '情绪判断':
    use_SnowNLP.Text_Emotion_Judgment()
elif option == '生成词云':
    use_wordcloud.Text_Generate_WordCloud()

image = Image.open('./images/TextMiner.png')
st.sidebar.image(image)
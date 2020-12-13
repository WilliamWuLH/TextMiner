import streamlit as st
import numpy as np
import pandas as pd

import use_jieba
import use_SnowNLP

# --- index
st.sidebar.title('Text Miner 文本矿工')
st.sidebar.write('## 请选择你要进行的文本操作：')
option = st.sidebar.selectbox(
    '文本操作选择：',
    ['关键词抽取', '情绪判断'])

if option == '关键词抽取':
    use_jieba.Text_Keywords()
elif option == '情绪判断':
    use_SnowNLP.Text_Emotion_Judgment()
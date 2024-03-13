import streamlit as st
import pandas as pd
import urllib 
from urllib.request import urlopen

def app():
    def book():
        url="https://drive.google.com/file/d/1uadHhW5JpzFHKSZHXjVUcilq2XiHRDvm/view?usp=sharing"
        response = urllib.request.urlopen(url)
        df = pd.read_csv("도서정보3.csv","encoding=cp949")
        return df.set_index("책제목")

    try:
        urllib.request.urlopen("https://drive.google.com/file/d/1uadHhW5JpzFHKSZHXjVUcilq2XiHRDvm/view?usp=sharing")
        df = book()
        bookSelect = st.multiselect(
        label="책 이름을 입력하세요", options=list(df.index), default=["우리 집 늙은 고양이가 하는 말"]
        )
        if not bookSelect:
            st.error("책 이름을 선택해주세요")
        else:
            data = df.loc[bookSelect]
            st.write(bookSelect, data.sort_index())

            data = data.T.reset_index()

    except urllib.error.URLError as e:
        print ('Error code: ', e.code)

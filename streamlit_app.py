# Streamlitライブラリをインポート
import streamlit as st
import random

# タイトルを設定
st.title('おみくじアプリをつくってみたよ！のアプリ')

if st.button("おみくじを引く"):
    results = ["大吉","中吉","小吉","吉","凶","大凶"]
    result = random.choice(results)
    st.write(f"結果:{result}")
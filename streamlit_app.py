# Streamlitライブラリをインポート
import streamlit as st
import random

# タイトルを設定
st.title('おみくじアプリをつくってみたよ！のアプリ')

user_name = st.text_input("あなたの名前を入力してください。")

if st.button("おみくじを引く"):
    results = ["大吉","中吉","小吉","吉","凶","大凶"]
    result = random.choice(results)

    comments = {
        "大吉": "素晴らしい一日になるでしょう❣",
        "中吉": "良いことがあるかも！？"
        "小吉": "悪くないはず"
        "吉": "soso"
        "凶": "注意が大事！"
        "大凶": "おみくじを信じないのも一つの手です"
    }

    #結果を表示する
    if user_name:
        st.write(f"{user_name}さんの結果: {result}")
    else:
        st.write(f"結果: {result}")
    
    st.write(comments[result])

    
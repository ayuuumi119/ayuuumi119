import streamlit as st
import random
st.title("テンションアゲアゲアプリ")
if st.button("引く"):
    results = ["アゲアゲ～↑","大大吉だよ神","お疲れ♡","明日はいいことあるっしょ！","ファミチキ食べたくね？","テンション上げてこ！"]
    result =random.choice(results)
    st.write(f"結果:{result}")
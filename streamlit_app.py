import streamlit as st
import random
st.title("テンションアゲアゲアプリ")
if st.button("引く"):
    results = ["大吉","大大吉","お疲れ様！","きっといいことがあるよ","明日も頑張ってね","よく頑張ったね"]
    result =random.choice(results)
    st.write(f"結果:{result}")
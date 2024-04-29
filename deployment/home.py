import streamlit as st
import pandas as pd
from PIL import Image

def run():
    
    # Judul
    st.title("Suicidal Tweet Detection")
    
    # Subheader
    st.subheader("Home")

    # Problem statement
    image = Image.open('suicide.png')
    st.image(image)
    st.write("Suicidal Tweet Detection digunakan untuk mendeteksi tweet yang dibuat termasuk pada suicidal post atau normal post ")
    st.write("Detection akan dilakukan dengan menggunakan salah algoritma Deep Learning yaitu LSTM")
    st.markdown("---")

    # Dataset
    st.write("**Dataset**")
    st.write("Dataset diambil dari Kaggle Dataset, yang dapat diakses pada [link](https://www.kaggle.com/datasets/aunanya875/suicidal-tweet-detection-dataset/data).")
    st.write("Ada 1787 Data dengan 2 feature seperti terlihat di bawah :")
    df = pd.read_csv('Suicide_Ideation_Dataset(Twitter-based).csv')
    st.dataframe(df)
    
if __name__ == "__main__":
  run()
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
from wordcloud import WordCloud


def run() :
    st.title('Suicidal Tweet Detection')
    st.subheader('EDA untuk analisa dataset Suicidal Tweet Detection')
    #deskripsi
    st.write('**Created by Hafiz J**')

    st.markdown('-------')

    #Show dataframe
    df = pd.read_csv('Suicide_Ideation_Dataset(Twitter-based).csv')

    st.write("## Distribution of Suicide Post")
    fig = plt.figure(figsize=(10, 8))
    df.groupby('Suicide').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
    plt.gca().spines[['top', 'right',]].set_visible(False)
    st.pyplot(fig)

    st.write("## Distribution of Tweet Lenght")
    #menghapus missing value
    df.dropna(inplace=True)
    df['Tweet_length'] = df['Tweet'].apply(len)
    # Plotting Tweet Length Distribution by Suicide
    fig1 = plt.figure(figsize=(10, 8))
    sns.boxplot(x='Suicide', y='Tweet_length', data=df,  palette='husl')
    plt.title('Tweet Length Distribution by Suicide')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    st.pyplot(fig1)

    st.write("## Wordcloud")
    tweet_by = df.groupby('Suicide')['Tweet'].apply(lambda x: ' '.join(x)).to_dict()
    fig2, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 15))  # Adjust the size and layout as needed
    axes = axes.flatten()
    for i, (emotion, text) in enumerate(tweet_by.items()):
        wordcloud = WordCloud(width=800, height=600, background_color='white').generate(text)
        axes[i].imshow(wordcloud, interpolation='bilinear')
        axes[i].axis('off')
        axes[i].set_title(emotion.capitalize(), fontsize=25)
    plt.tight_layout()
    st.pyplot(fig2)
    
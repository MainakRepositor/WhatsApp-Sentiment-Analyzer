# Importing modules
import nltk
import streamlit as st
import re
import preprocessor,helper
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.sidebar.title("Whatsapp Chat  Sentiment Analyzer")

# VADER : is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments.
nltk.download('vader_lexicon')

# File upload button
uploaded_file = st.sidebar.file_uploader("Choose a file")

# Main heading
st. markdown("<h1 style='text-align: center; color: grey;'>Whatsapp Chat  Sentiment Analyzer</h1>", unsafe_allow_html=True)

if uploaded_file is not None:
    
    # Getting byte form & then decoding
    bytes_data = uploaded_file.getvalue()
    d = bytes_data.decode("utf-8")
    
    # Perform preprocessing
    data = preprocessor.preprocess(d)
    
    # Importing SentimentIntensityAnalyzer class from "nltk.sentiment.vader"
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    # Object
    sentiments = SentimentIntensityAnalyzer()
    
    # Creating different columns for (Positive/Negative/Neutral)
    data["po"] = [sentiments.polarity_scores(i)["pos"] for i in data["message"]] # Positive
    data["ne"] = [sentiments.polarity_scores(i)["neg"] for i in data["message"]] # Negative
    data["nu"] = [sentiments.polarity_scores(i)["neu"] for i in data["message"]] # Neutral
    
    # To indentify true sentiment per row in message column
    def sentiment(d):
        if d["po"] >= d["ne"] and d["po"] >= d["nu"]:
            return 1
        if d["ne"] >= d["po"] and d["ne"] >= d["nu"]:
            return -1
        if d["nu"] >= d["po"] and d["nu"] >= d["ne"]:
            return 0

    # Creating new column & Applying function
    data['value'] = data.apply(lambda row: sentiment(row), axis=1)
    
    # User names list
    user_list = data['user'].unique().tolist()
    
    # Sorting
    user_list.sort()
    
    # Insert "Overall" at index 0
    user_list.insert(0, "Overall")
    
    # Selectbox
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
    
    if st.sidebar.button("Show Analysis"):
        # Monthly activity map
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Activity map(Positive)</h3>",unsafe_allow_html=True)
            
            busy_month = helper.month_activity_map(selected_user, data,1)
            
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Activity map(Neutral)</h3>",unsafe_allow_html=True)
            
            busy_month = helper.month_activity_map(selected_user, data, 0)
            
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='grey')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Activity map(Negative)</h3>",unsafe_allow_html=True)
            
            busy_month = helper.month_activity_map(selected_user, data, -1)
            
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Daily activity map
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Activity map(Positive)</h3>",unsafe_allow_html=True)
            
            busy_day = helper.week_activity_map(selected_user, data,1)
            
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Activity map(Neutral)</h3>",unsafe_allow_html=True)
            
            busy_day = helper.week_activity_map(selected_user, data, 0)
            
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='grey')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Activity map(Negative)</h3>",unsafe_allow_html=True)
            
            busy_day = helper.week_activity_map(selected_user, data, -1)
            
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Weekly activity map
        col1, col2, col3 = st.columns(3)
        with col1:
            try:
                st.markdown("<h3 style='text-align: center; color: black;'>Weekly Activity Map(Positive)</h3>",unsafe_allow_html=True)
                
                user_heatmap = helper.activity_heatmap(selected_user, data, 1)
                
                fig, ax = plt.subplots()
                ax = sns.heatmap(user_heatmap)
                st.pyplot(fig)
            except:
                st.image('error.webp')
        with col2:
            try:
                st.markdown("<h3 style='text-align: center; color: black;'>Weekly Activity Map(Neutral)</h3>",unsafe_allow_html=True)
                
                user_heatmap = helper.activity_heatmap(selected_user, data, 0)
                
                fig, ax = plt.subplots()
                ax = sns.heatmap(user_heatmap)
                st.pyplot(fig)
            except:
                st.image('error.webp')
        with col3:
            try:
                st.markdown("<h3 style='text-align: center; color: black;'>Weekly Activity Map(Negative)</h3>",unsafe_allow_html=True)
                
                user_heatmap = helper.activity_heatmap(selected_user, data, -1)
                
                fig, ax = plt.subplots()
                ax = sns.heatmap(user_heatmap)
                st.pyplot(fig)
            except:
                st.image('error.webp')

        # Daily timeline
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Timeline(Positive)</h3>",unsafe_allow_html=True)
            
            daily_timeline = helper.daily_timeline(selected_user, data, 1)
            
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Timeline(Neutral)</h3>",unsafe_allow_html=True)
            
            daily_timeline = helper.daily_timeline(selected_user, data, 0)
            
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='grey')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>Daily Timeline(Negative)</h3>",unsafe_allow_html=True)
            
            daily_timeline = helper.daily_timeline(selected_user, data, -1)
            
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Monthly timeline
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Timeline(Positive)</h3>",unsafe_allow_html=True)
            
            timeline = helper.monthly_timeline(selected_user, data,1)
            
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Timeline(Neutral)</h3>",unsafe_allow_html=True)
            
            timeline = helper.monthly_timeline(selected_user, data,0)
            
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='grey')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>Monthly Timeline(Negative)</h3>",unsafe_allow_html=True)
            
            timeline = helper.monthly_timeline(selected_user, data,-1)
            
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Percentage contributed
        if selected_user == 'Overall':
            col1,col2,col3 = st.columns(3)
            with col1:
                st.markdown("<h3 style='text-align: center; color: black;'>Most Positive Contribution</h3>",unsafe_allow_html=True)
                x = helper.percentage(data, 1)
                
                # Displaying
                st.dataframe(x)
            with col2:
                st.markdown("<h3 style='text-align: center; color: black;'>Most Neutral Contribution</h3>",unsafe_allow_html=True)
                y = helper.percentage(data, 0)
                
                # Displaying
                st.dataframe(y)
            with col3:
                st.markdown("<h3 style='text-align: center; color: black;'>Most Negative Contribution</h3>",unsafe_allow_html=True)
                z = helper.percentage(data, -1)
                
                # Displaying
                st.dataframe(z)


        # Most Positive,Negative,Neutral User...
        if selected_user == 'Overall':
            
            # Getting names per sentiment
            x = data['user'][data['value'] == 1].value_counts().head(10)
            y = data['user'][data['value'] == -1].value_counts().head(10)
            z = data['user'][data['value'] == 0].value_counts().head(10)

            col1,col2,col3 = st.columns(3)
            with col1:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Most Positive Users</h3>",unsafe_allow_html=True)
                
                # Displaying
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Most Neutral Users</h3>",unsafe_allow_html=True)
                
                # Displaying
                fig, ax = plt.subplots()
                ax.bar(z.index, z.values, color='grey')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col3:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Most Negative Users</h3>",unsafe_allow_html=True)
                
                # Displaying
                fig, ax = plt.subplots()
                ax.bar(y.index, y.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

        # WORDCLOUD......
        col1,col2,col3 = st.columns(3)
        with col1:
            try:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Positive WordCloud</h3>",unsafe_allow_html=True)
                
                # Creating wordcloud of positive words
                df_wc = helper.create_wordcloud(selected_user, data,1)
                fig, ax = plt.subplots()
                ax.imshow(df_wc)
                st.pyplot(fig)
            except:
                # Display error message
                st.image('error.webp')
        with col2:
            try:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Neutral WordCloud</h3>",unsafe_allow_html=True)
                
                # Creating wordcloud of neutral words
                df_wc = helper.create_wordcloud(selected_user, data,0)
                fig, ax = plt.subplots()
                ax.imshow(df_wc)
                st.pyplot(fig)
            except:
                # Display error message
                st.image('error.webp')
        with col3:
            try:
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Negative WordCloud</h3>",unsafe_allow_html=True)
                
                # Creating wordcloud of negative words
                df_wc = helper.create_wordcloud(selected_user, data,-1)
                fig, ax = plt.subplots()
                ax.imshow(df_wc)
                st.pyplot(fig)
            except:
                # Display error message
                st.image('error.webp')

        # Most common positive words
        col1, col2, col3 = st.columns(3)
        with col1:
            try:
                # Data frame of most common positive words.
                most_common_df = helper.most_common_words(selected_user, data,1)
                
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Positive Words</h3>",unsafe_allow_html=True)
                fig, ax = plt.subplots()
                ax.barh(most_common_df[0], most_common_df[1],color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            except:
                # Disply error image
                st.image('error.webp')
        with col2:
            try:
                # Data frame of most common neutral words.
                most_common_df = helper.most_common_words(selected_user, data,0)
                
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Neutral Words</h3>",unsafe_allow_html=True)
                fig, ax = plt.subplots()
                ax.barh(most_common_df[0], most_common_df[1],color='grey')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            except:
                # Disply error image
                st.image('error.webp')
        with col3:
            try:
                # Data frame of most common negative words.
                most_common_df = helper.most_common_words(selected_user, data,-1)
                
                # heading
                st.markdown("<h3 style='text-align: center; color: black;'>Negative Words</h3>",unsafe_allow_html=True)
                fig, ax = plt.subplots()
                ax.barh(most_common_df[0], most_common_df[1], color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            except:
                # Disply error image
                st.image('error.webp')




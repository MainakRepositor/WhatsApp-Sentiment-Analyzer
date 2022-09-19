
# Whatsapp chat sentiment analyzer

After battling numerous errors, finally completed making Whatsapp Chat Sentiment analyzer, my first data analysis project. It is based on SentimentIntensityAnalyzer class from "nltk.sentiment.vader" module. If you ever wonder who is the most positive person in your whatsapp group of let say 200+ or less members then this is what you are looking for.
Not only posititve user, you can see the following results on overall group & individual as well :

- Monthly Activity map(Positive, Neutral, Negative)
- Daily Activity map(Positive, Neutral, Negative)
- Weekly Activity map(Positive, Neutral, Negative)
- Daily timeline(Positive, Neutral, Negative)
- Monthly timeline(Positive, Neutral, Negative)
- Percentage Contribution(Positive, Neutral, Negative)
- Word Cloud(Positive, Neutral, Negative)
- Most Common words(Positive, Neutral, Negative)
- Most user(Positive, Neutral, Negative)

You just have to perform the following task in order to get analysis.
- Export whatsapp chat (24 hour format).
- Browse the file.
- Click Show Analysis.

## Deployed link

[click here](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa19ucTE0WG9IdmFKNVhMSnlCNzJWVWxGV25NUXxBQ3Jtc0ttREhtME5RTzdNUFRQLXk0cl95SXQzR01wRHRfUHFjVmFoSEtJM21Nb0ZsU3lFdmVMTVV3cFhDSEhldFNSdDctUTl3S01kU3dOS3A0X1BONkhzUW5Pc1ZETi0xaFRQYUg2Y3BzM1poSTliNGE3RU5LMA&q=https%3A%2F%2Fwhatsapp-sentiment-analyzer.herokuapp.com%2F&v=M8AlfcW0M70)


## Run locally

Create new project in pycharm and add above files. After that open terminal and run the following command. This will install all the modules needed to run this app. 

```bash
pip install -r requirements.txt
```

To run the app, type following command in terminal. 
```bash
streamlit run app.py
```

## Libraries

- streamlit
- matplotlib
- seaborn
- nltk
- collection
- wordcloud
- urlextract
- emoji


## Screenshots

![app · Streamlit - Google Chrome 28-04-2022 20_35_52](https://user-images.githubusercontent.com/72250606/165783851-967737d9-6542-485a-ba75-9368d4905289.png)
![app · Streamlit - Google Chrome 28-04-2022 20_30_40](https://user-images.githubusercontent.com/72250606/165783574-142f8e37-2fec-4f4e-aa3c-8ebb07acc401.png)
![app · Streamlit - Google Chrome 28-04-2022 20_30_51](https://user-images.githubusercontent.com/72250606/165783590-93ac7ed7-e432-46aa-b424-c9cf7b1a8b0d.png)
![app · Streamlit - Google Chrome 28-04-2022 20_31_04](https://user-images.githubusercontent.com/72250606/165783594-e62f6776-b241-4ebd-8a7a-78e3a82f343f.png)
![app · Streamlit - Google Chrome 28-04-2022 20_31_23](https://user-images.githubusercontent.com/72250606/165783597-6f497c0f-01ef-42a5-be8a-5a67c7c2bc1f.png)
![app · Streamlit - Google Chrome 28-04-2022 20_31_34](https://user-images.githubusercontent.com/72250606/165783601-b7d553f4-8e7d-4ed0-9a2a-56d58e31cbcf.png)

## Demo video

[Whatsapp chat sentiment analyzer](https://www.youtube.com/watch?v=XCLCOA9BXVA)
 
## Author

- [Udhay Brahmi](https://github.com/Udhay-Brahmi)

## Support

For support, email udhaybrahmi786@gmail.com or udhaybrahmi@gmail.com.


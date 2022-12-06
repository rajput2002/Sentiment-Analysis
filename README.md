Sentiment Analysis is the process of determining whether a piece of text is positive, negative or neutral. Sentiment analysis or opinion mining is a simple task of understanding the emotions (feelings) of the writer of a particular text.
Sentiment analysis can help companies to study the customer sentiment towards a particular product.
Companies sometimes try to delete the content that has a negative sentiment.

I have used twitter datasets in this project. First, I have used CountVectorizer() to convert test into numbers because machine learning algorithms can only work on numbers. Then, I used Support Vector Machine to train the model. Then, I used joblib to save the model and used streamlit to make webapp. Then, I used ngrok to map the web app to port. At last, I used Heroku to make permanent web app.

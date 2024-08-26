import nltk
from textblob import TextBlob
from newspaper import Article
url = 'https://indianexpress.com/article/business/employment-growth-in-corporate-sector-declined-to-1-5-in-fy24-bob-report-9526368/?ref=business_hp'
article = Article(url)

article.download()
article.parse()
article.nlp()
text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)

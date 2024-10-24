from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')


app = Flask(__name__)

sa = SentimentIntensityAnalyzer()


@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text1']
    # Perform sentiment analysis here
    sentiment = analyze_sentiment(text)  # This should return a dictionary with results
    # Render result in HTML template or return a JSON response
    return render_template('result.html', sentiment=sentiment)  # Make sure 'result.html' displays the sentiment correctly


@app.route('/', methods=['POST'])
def my_form_post():

    stop_words = set(stopwords.words('english'))


    text1 = request.form['text1'].lower()
    text_final = re.sub(r'\d+', '', text1)
    processed_doc1 = ' '.join([word for word in text_final.split() if word not in stop_words])

    dd = sa.polarity_scores(text=processed_doc1)
    compound = round((1 + dd['compound']) / 2, 2)

    return render_template('form.html', final=compound, text1=text_final, text2=dd['pos'], text5=dd['neg'], text4=compound, text3=dd['neu'])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002, threaded=True)

from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from gensim.summarization import summarize, keywords

app = Flask(__name__)

# Function to scrape and summarize news
def get_news_summary(url):
    # Scrape content from the URL
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ''.join(map(lambda p: p.text, soup.find_all('p')))
    title = ''.join(soup.title.stripped_strings)

    # Summarize the news
    summary = summarize(text, ratio=0.1)
    key_words = keywords(text, ratio=0.1, lemmatize=True)

    return title, summary, key_words

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and summarize the news
@app.route('/summarize', methods=['POST'])
def summarize_news():
    url = request.form['url']
    try:
        title, summary, key_words = get_news_summary(url)
        return render_template('result.html', title=title, summary=summary, keywords=key_words.split('\n'))
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)

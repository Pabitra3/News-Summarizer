from bs4 import BeautifulSoup
from requests import get
import requests
def get_only_text(url):
    page= requests.get(url)
    soup= BeautifulSoup(page.content,"lxml")
    text=''.join(map(lambda p:p.text,soup.find_all('p')))
    #text=soup.text
    title=''.join(soup.title.stripped_strings)
    return title,text
# Calling the function with the desired News Url
text=get_only_text("https://www.vox.com/plink")
print(text)
# Number of words- original Text
len(str.split(text[1]))
# For Summarization
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
# Printing the summarized Text(Word Count)
print("Title:"+text[0])
print("Summary:")
print(summarize(repr(text[1]),word_count=100))
# (Number of word)
print("Title:"+text[0])
print("Summary:")
print(summarize(repr(text),ratio=0.1))
summarizied_text=summarize(repr(text[1]),ratio=0.1)
len(str.split(summarizied_text))
# Keywords
print('\n Keywords:')
print(keywords(text[1],ratio=0.1,lemmatize=True))

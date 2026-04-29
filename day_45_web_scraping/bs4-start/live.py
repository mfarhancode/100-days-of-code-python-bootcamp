from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

y_webpage = response.text

soup = BeautifulSoup(y_webpage, 'html.parser')

articles_text = soup.find_all(name='span', class_='titleline')

articles_anchor_tag = soup.select('.title .titleline a')
article_text = []
article_links = []

for article_tag in articles_text:
    text = article_tag.getText()
    article_text.append(text)


for anchor_tag in articles_anchor_tag:
    # print(anchor_tag)
    link = anchor_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]


largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)


print(article_text[largest_index])
print(article_links[largest_index])

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)
# print(soup.title.string)

article_tag = soup.select('.titleline a')
article_title = [article.getText() for article in article_tag]
print(article_title)
# article_dict = {}
# count = 0
# for article in article_tag:
#     if count % 2 == 0:
#         article_dict['title'] = article.getText()
#         article_dict['url'] = article.get('href')
#     count += 1
#
# # article_text = article_tag.getText()
# # print(article_text)
# # article_url = article_tag.get('href')
# # print(article_url)
# article_upvotes = [int(score.getText().split()[0]) for score in soup.select('.score')]



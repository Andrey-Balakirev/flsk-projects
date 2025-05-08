import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    

def get_python_news(html):
    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.find('ul', class_='list-recent-posts')
    print(news_list)


if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        get_python_news(html)


#published = news.find('time').text
#try:
 #   published = datetime.strptime(published, '%Y-%m-%d')
#except(ValueError):
    #published = datetime.now()

def save_news(title, url, published):
    new_news = News(title=title, url=url, published=published)
    db.session.add(new_news)
    db.session.commit()
    

if __name__ == "__main__":
    html = get_html("https://www.python.org/blogs/")
    if html:
        with open("python-org-news.html", "w", encoding="utf8") as f:
            f.write(html)

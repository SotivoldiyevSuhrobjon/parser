import requests
from bs4 import BeautifulSoup as bs

from test import create_news_post

url = "https://kun.uz/news/category/jahon"


async def download_img_by_url(url):
    r = requests.get(url)
    return r.content
    # with open("test.jpg", 'wb') as f:
    #     f.write(r.content)


async def get_posts():
    data = []
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    news = soup.find_all('div', attrs={'class': 'news'})
    for n in news:
        img = n.find_next('a').find('img')
        hour = n.find_next('div').find('span')
        title = n.find_next('a', attrs={'class': 'news__title'})
        if len(hour.text.split("/")) == 1:
            news_link = "https://kun.uz" + title['href']
            context = await get_news_detail(news_link)
            data.append(
                {
                    "img": img['src'],
                    "title": title.text,
                    "context": context,
                    "date": hour.text,
                    "news_link": news_link,
                }
            )
    return data


async def get_news_detail(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    single_content = soup.find('div', attrs={"class": "single-content"})
    subtitle = single_content.find("h4")
    context = ""
    for item in single_content.find_all("p"):
        context += f"{item}\n"

    result = await create_news_post(title=subtitle, body=context)
    return result

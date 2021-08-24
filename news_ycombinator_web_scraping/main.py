import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://news.ycombinator.com"

response = requests.get(url=WEBSITE_URL)

yc_html_website = response.text

yc_soup = BeautifulSoup(yc_html_website, "html.parser")

# articles_tags = yc_soup.select(selector=".storylink")

articles_tags = yc_soup.find_all(name="a", class_="storylink")

articles_titles = [article_tag.getText() for article_tag in articles_tags]

articles_urls = [article_url.get("href") for article_url in articles_tags]

subtext_tags = yc_soup.select(selector=".subtext")

scores = []

for subtext_tag in subtext_tags:

    score_tag = subtext_tag.select(selector=".score")

    score = 0

    if score_tag:
        score = int(score_tag[0].getText().split()[0])

    scores.append(score)

data = {}

for index in range(len(articles_titles)):

    piece_of_data = {
        "title": articles_titles[index],
        "url": articles_urls[index],
        "score": scores[index]
    }

    data[index + 1] = piece_of_data

website_with_max_points = data[scores.index(max(scores)) + 1]

print(website_with_max_points)
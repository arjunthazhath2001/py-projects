import requests
from bs4 import BeautifulSoup

response= requests.get("https://appbrewery.github.io/news.ycombinator.com/")


yc_pape= response.text

soup= BeautifulSoup(yc_pape,"html.parser")


print(soup.title)


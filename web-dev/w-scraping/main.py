from bs4 import BeautifulSoup

with open("website.html") as file:
    contents= file.read()
    


soup= BeautifulSoup(contents,'html.parser')

# print(soup.title.string)
# print(soup.prettify())

anchor_tags= soup.find_all(name='a')
# print(anchor_tags)

for tag in anchor_tags:
    # print(tag.get_text())
    print(tag.get('href'))
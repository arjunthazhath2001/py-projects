import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
import lxml

load_dotenv()

my_email= os.getenv("my_email")
password= os.getenv("password")

headers={
     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"

}

url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response=requests.get(url,headers=headers)
print(response)

web_page=response.text

soup= BeautifulSoup(web_page,"lxml")

title_tag= soup.find(name="span", id="productTitle")

price_tag=soup.find(name="span",class_="a-price-whole")

whole = soup.find("span", class_="a-price-whole")
fraction = soup.find("span", class_="a-price-fraction")

if whole and fraction:
    price = f"{whole.get_text()}{fraction.get_text()}"
    price= float(price)


if title_tag is None:
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())
    print("Element not found. Saved response to debug.html")

print(title_tag.get_text())

# title= title_tag.get_text(strip=True).replace('é', 'e')
# print(title)

# if price<100.00:
#     print("hi")
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()

#         connection.login(user=my_email,password=password)

#         connection.sendmail(from_addr=my_email, to_addrs="arjunta32@gmail.com", msg=f"Subject:Amazon Price Alert!\n\n{title}. Click on link below: {url}")

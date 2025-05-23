
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import datetime as dt
from newsapi import NewsApiClient
import requests
import os
from dotenv import load_dotenv

from twilio.rest import Client

load_dotenv()


account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_API_KEY= os.getenv('PRICE_API_KEY') 
NEWS_API_KEY= os.getenv('NEWS_API_KEY')
UPPER_LIMIT=1
LOWER_LIMIT=-1




url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=60min&apikey={PRICE_API_KEY}'


r = requests.get(url)
data = r.json()
print(data)    


today = dt.datetime.now()

yesterday = (today - dt.timedelta(days=1)).strftime('%Y-%m-%d')
day_before_yesterday = (today - dt.timedelta(days=2)).strftime('%Y-%m-%d')


yesterday_close=float(data["Time Series (Daily)"][yesterday]['4. close'])
day_before_yesterday= float(data["Time Series (Daily)"][day_before_yesterday]['4. close'])


percentage_change=((yesterday_close-day_before_yesterday)/day_before_yesterday)*100

print(round(percentage_change,2))






if percentage_change>=UPPER_LIMIT or percentage_change<=LOWER_LIMIT:
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    all_articles = newsapi.get_everything(q='tesla',
                                        language='en',
                                        sort_by='publishedAt',
                                        
                                        )

    three_articles=all_articles['articles'][0:3]
    # print(three_articles)
    
    formatted_article=[f"STOCK_NAME:{STOCK} -> {percentage_change}%. \nHeadline:{article['title']}.\nBrief:{article['description']}" for article in three_articles]


    for article in formatted_article:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body=f"{article}",
        from_="whatsapp:+14155238886",
        to="whatsapp:+918838630198")





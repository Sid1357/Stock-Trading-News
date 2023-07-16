import requests
from twilio.rest import Client
STOCK_NAME1 = "TSLA"
COMPANY_NAME1 = "Tesla Inc"

STOCKNAME2 ="RELIANCE.BSE"
COMPANY_NAME2 = "Reliance Industries Ltd"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "M8PQTFZ1GUVY2VUU"
NEWS_API_KEY = "df32660cc5db41c1a016bbe503f9653f"

ACCOUNT_SID = "AC262a20add91c735134eb49c2b73d30b0"
TWILIO_AUTH_TOKEN = "c7f9e83e1669354a19475e19ceb4e6aa"




response1 = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&interval=5min&apikey=M8PQTFZ1GUVY2VUU")
data = response1.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
difference = round(float(yesterday_closing_price) - float(day_before_yesterday_closing_price), 2)
up_down = None
if difference>0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)
diff_percent = round((difference/float(yesterday_closing_price))*100, 2)
print(diff_percent)
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": "df32660cc5db41c1a016bbe503f9653f",
        "qInTitle": "Reliance",
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = new_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_article_list = [f"{STOCKNAME2}: {up_down}{diff_percent}%\nHeadline: {articles['title']}. \nBreif: {articles['description']}" for articles in three_articles]
    client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_="+14178073408",
            to="+918976155380"
        )





"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


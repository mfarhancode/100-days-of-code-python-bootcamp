import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")
PHONE_NUMBER=os.getenv("PHONE_NUMBER")
TWILLIO_WA_NUMBER=os.getenv("TWILLIO_WA_NUMBER")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":API_KEY_STOCK
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()

# print(data)

close_data = []
for key in data['Time Series (Daily)']:
    temp = data['Time Series (Daily)'][key]["4. close"]
    # print(temp)
    close_data.append(float(temp))
    if len(close_data) == 2:
        break

happened = ''
if close_data[0] > close_data[1]:
    temp = close_data[0] - close_data[1]
    # print(temp)
    change = (temp/close_data[0]) * 100
    # print(change)
    happened = 'increase'
else:
    temp = close_data[1] - close_data[0]
    # print(temp)
    change = (temp / close_data[1]) * 100
    # print(change)
    happened = 'decrease'
# print(change)
# print(happened)


if change >= 3:
    print('Getting news')
    news_params = {
        "apiKey" : API_KEY_NEWS,
        "qInTitle":COMPANY_NAME
    }
    news_response_json = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response = news_response_json.json()
    # print(news_response['articles'][0])
    data = (news_response['articles'])
    full_message = ''
    for i in range(3):
        if happened == 'increase':
            full_message += f"🔺{int(change)}% \n"
        else:
            full_message += f"🔻{int(change)}% \n"
        full_message += f"Title: {data[i]['title']} \n"
        full_message += f"Description: {data[i]['description']} \n"
        full_message += f"URL: {data[i]['url']} \n\n"

    print(full_message)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=f"whatsapp:{TWILLIO_WA_NUMBER}",
        body=full_message,
        to=f"whatsapp:{PHONE_NUMBER}"
    )

    print(message.status)
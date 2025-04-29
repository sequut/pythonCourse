import requests
from datetime import datetime

def fetch_cbr_rates():
    today = datetime.now().strftime("%d/%m/%Y")
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}"
    response = requests.get(url)
    response.encoding = 'windows-1251'
    if response.status_code == 200:
        return response.text
    raise ConnectionError("Не удалось получить данные с сайта ЦБ РФ")

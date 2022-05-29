# char_crawling.py

from bs4 import BeautifulSoup
import requests
import datetime
import stock_code


def extract_info(tr):
    date = tr.find("td", {'align': 'center'}).find("span").text.replace('.', '-')
    date = datetime.date.fromisoformat(date)
    td_list = tr.find_all("td", {"class": "num"})
    row = [date]
    for td in td_list:
        n = int(td.find("span").text.strip().replace(",", ""))
        row.append(n)
    return row


def make_tr_list(code, page):
    url = f"https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}"
    response = requests.get(url)
    text = response.text
    html = BeautifulSoup(text, "html.parser")
    tr_list = html.find_all("tr", {"onmouseover": "mouseOver(this)"})
    return tr_list


code = stock_code.search_code()
for page in range(1, 11):
    print("page :", page)
    tr_list = make_tr_list(code, page)
    for tr in tr_list:
        row = extract_info(tr)
        print(row)
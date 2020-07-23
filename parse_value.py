import requests, os, string
from bs4 import BeautifulSoup
import date


def value_name_choose(value_name):
    if value_name == 'usd':
        value_link_end = '1.html'
        return value_link_end
    elif value_name == 'eur':
        value_link_end = '23.html'
        return value_link_end

def parse_data_value(value_name):

    url = 'https://yandex.ru/news/quotes/'
    r = requests.get(url + value_name_choose(value_name))

    with open('value.html', 'w', encoding="utf-8") as output_file:
        output_file.write(r.text)

    page = open('value.html', 'r', encoding="utf-8")
    # Beautiful Soup
    soup = BeautifulSoup(''.join(page), 'lxml')

    value_date = soup.find('td', {'class': 'quote__date'}).text
    value_cost = soup.find('td', {'class': 'quote__value'}).text

    date_value_str = 'По информации с ' + url + ' на ' + value_date + ' курс ' + value_name.upper() + ' = ' + value_cost

    return date_value_str

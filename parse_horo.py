import requests, os, string
from bs4 import BeautifulSoup
import date



def page_choose(sign_num):
    global url
    global zod_word
    url = 'https://orakul.com/horoscope/astrologic/more/' + html_endwords[sign_num-1]
    url_end = html_endwords[sign_num-1]
    slash_index = url_end.find("/")
    zod_word_list = url_end[0:slash_index]
    zod_word = "".join(zod_word_list)


def parse_data_html(zod_word):
    r = requests.get(url)

    with open('test.html', 'w', encoding="utf-8") as output_file:
        output_file.write(r.text)
    os.rename('test.html', zod_word + '.html')


def check_existance(zod_word):
    return os.path.exists(zod_word+'.html')





html_endwords = ['aries/today.html', 'taurus/today.html', 'gemini/today.html', 'cancer/today.html','lion/today.html',
                 'virgo/today.html','libra/today.html','scorpio/today.html', 'sagittarius/today.html',
                 'capricorn/today.html','aquarius/today.html','pisces/today.html']

def get_horoscope_text(sign_num):

    page_choose(sign_num)


    if check_existance(zod_word) is False:    #Проверка существования хтмл файла
        parse_data_html(zod_word)

    else:
        pass

    delete_file_bool = date.is_file_outdated(zod_word + '.html')

    if delete_file_bool is True:  # Проверка необходимости обновления спаршенных данных
        os.remove(zod_word+'.html')
        parse_data_html(zod_word)


    page = open(zod_word + '.html', 'r', encoding="utf-8")
    # Beautiful Soup
    soup = BeautifulSoup(''.join(page), 'lxml')


    horo_text_parsed = soup.find('div', {'class': 'horoBlock'}).find('p').text
    horo_text_list = horo_text_parsed.split(" ")
    horo_text = " ".join(horo_text_list)
    return horo_text

from bs4 import BeautifulSoup
from random import randrange
import requests
import time
from deep_translator import GoogleTranslator



def parse_html(url,keyword):
    # Отправляем GET-запрос к странице
    response = requests.get(url)
    
    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим все теги 'a' (ссылки)
        links = soup.find_all('a')
        
        # Выводим на экран ссылки и их подписи
        for link in links:
            href = link.get('href')
            text = link.text.strip()
            if href and href.startswith('http'):
                if text != "API":
                   if text != "Legal":
                      if text != "Apply to YC":
                         if keyword.lower() in text.lower() or keyword.lower() in href.lower():
                            translated = GoogleTranslator(source='en', target='ru').translate(text)
                            print(f"{translated}\n{href}\n")
                         #if keyword.lower() in href.lower():
                            #print(f"{text}\n{href}\n")
    else:
        time.sleep(randrange(7)+1)
        parse_html(url,keyword) 

parse_html('https://news.ycombinator.com', ' ')


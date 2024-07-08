import requests
from bs4 import BeautifulSoup

def parse_page(url,keyword):
    # Отправляем запрос на страницу
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при запросе страницы: {response.status_code}")
        return

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все блоки с указанным классом
    article_blocks = soup.find_all('h2', class_='tm-title tm-title_h2')

    # Извлекаем информацию из каждого блока
    for block in article_blocks:
        # Находим ссылку внутри блока
        link = block.find('a', class_='tm-title__link')['href']

        # Извлекаем текст подписи
        caption = block.find('span').text

        # Выводим результат
        if keyword.lower() in caption.lower():
            print(f"{caption}")
            print(f"https://habr.com{link}")
            print('')

# Использование
url = "https://habr.com/ru/hubs/business-laws/articles/"
parse_page(url,' ')
for i in range(2, 5):
    url = "https://habr.com/ru/hubs/business-laws/articles/page"+str(i)+"/"
    parse_page(url,' ')

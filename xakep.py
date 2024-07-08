import requests
from bs4 import BeautifulSoup

excluded_values = [
    "mailto:support@glc.ru",
    "support@glc.ru",
    "mailto:yakovleva.a@glc.ru",
    "yakovleva.a@glc.ru",
    "https://qrator.net/ru/",
    "/about/",
    "Подписка для физлиц",
    "/corporate/",
    "Подписка для юрлиц",
    "/advert/",
    "Реклама на «Хакере»",
    "/contact/",
    "Контакты",
    "https://xakep.ru/about-magazine/",
    "на годовую подписку",
    "https://xakep.ru/wp-login.php?redirect_to=https%3A%2F%2Fxakep.ru%2F",
    "Вход",
    "https://xakep.ru/",
    "https://xakep.ru/category/hack/",
    "Взлом",
    "https://xakep.ru/category/privacy/",
    "Приватность",
    "https://xakep.ru/category/tricks/",
    "Трюки",
    "https://xakep.ru/category/coding/",
    "Кодинг",
    "https://xakep.ru/category/admin/",
    "Админ",
    "https://xakep.ru/category/geek/",
    "Geek",
    "https://xakep.ru/pentest/",
    "Пентесты",
    "/wp-admin/users.php?page=paywall_subscribes&from=paywall_subscribe&subscribe=12_months",
    "Подписаться на материалы",
    "https://xakep.ru/tag/windows/",
    "Windows",
    "https://xakep.ru/tag/linux/",
    "Linux",
    "https://xakep.ru/tag/android/",
    "Android",
    "https://xakep.ru/tag/zhelezo/",
    "Железо",
    "https://xakep.ru/tag/hackthebox/",
    "Райтапы",
    "https://xakep.ru/tag/iskusstvennyj-intellekt/",
    "Нейросети",
    "https://xakep.ru/tag/python/",
    "Python",
    "https://xakep.ru/issues/xa/",
    "Все выпуски «Хакера»",
    "/issues",
    "https://xakep.ru/about",
    "ГодоваяподписканаХакер",
    "https://xakep.ru/issues/xa/301",
    "https://xakep.ru/issues/xa/300",
    "https://xakep.ru/issues/xa/299",
    "https://xakep.ru/issues/xa/298",
    "https://xakep.ru/issues/xa/297",
    "https://xakep.ru/wp-admin/users.php?page=paywall_subscribes",
    "Xakep #304",
    "https://xakep.ru/2024/07/08/htb-perfection/",
    "https://xakep.ru/category/hack/",
    "Взлом",
    "стикерпак для Telegram",
    "https://xakep.shop/paper2",
    "Бумажный спецвыпуск",
    "https://xakep.ru/2024/05/17/xakep-quest/",
    "Квест для читателей",
    "https://xakep.ru/advert/",
    "Заказать рекламу",
    "https://telegram.me/xakep_ru",
    "https://vk.com/xakep_mag",
    "https://twitter.com/XakepRU",
    "https://xakep.ru/2024/07/04/sysmon-attack-detection/",
    "https://xakep.ru/category/news/",
    "читателей",
    "авторов",
    "редакции"

]


response = requests.get('https://xakep.ru/')
if response.status_code != 200:
        print(f"Ошибка при запросе страницы: {response.status_code}")
        exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Находим тег <a> с классом 'bd-cat-link bd-cat-4927'
#a_tag = soup.find('a', class_='h3.entry-title a')
a_tags = soup.find_all('a')

# Извлекаем href (ссылку) и текст из каждого тега <a>
for a_tag in a_tags:
    href = a_tag.get('href')
    text = a_tag.get_text()
    text = text.replace('\n','')
    if href not in excluded_values and text not in excluded_values:
         if text:
              if "author/" not in href:
                   if "page/" not in href:
                        print(text)
                        print(href)
                        print('')


import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
def pars(url):
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

       "			Read More Â»		"

   ]


   response = requests.get(url)
   if response.status_code != 200:
           print(f"Ошибка при запросе страницы: {response.status_code}")
           exit()

   soup = BeautifulSoup(response.text, 'html.parser')

   a_tags = soup.find_all('a')

   for a_tag in a_tags:
       href = a_tag.get('href')
       text = a_tag.get_text()
       text = text.replace('\n','')
       if href not in excluded_values and text not in excluded_values:
            if text:
                 if "author/" not in href:
                      if "page/" not in href:
                          if text.startswith("	"):
                              text=text.replace('	','')
                              translated = GoogleTranslator(source='en', target='ru').translate(text)
                              href=href.replace('./','https://simplifiedprivacy.com/')
                              href=href.replace('https://simplifiedprivacy.com/.https://simplifiedprivacy.com/.','')
                              print(translated)
                              print(href)
                              print('')

pars('https://simplifiedprivacy.com')
pars('https://simplifiedprivacy.com/page/2/index.html')
pars('https://simplifiedprivacy.com/page/3/index.html')
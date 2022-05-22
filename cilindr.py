from bs4 import BeautifulSoup
import requests
import csv

list_smart = []
page = int(input('Сколько страниц спарсить: '))
def pagenation():
    for i in range(1, page + 1):
        PAGENATOR = f'https://www.sulpak.kg/Search/LoadProducts/4/~/~/~/~/~/PopularityDesc/tiles/15?query=iphone={i}'
        r = requests.get(PAGENATOR)


def get_content():
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('div', class_='goods-container')
    for item in items:
        list_smart.append({
            'Название продукта': item.find(
                'div', class_='goods-container').get_text(strip=True),

        })
    print(f'Страницв номер {i} готова')

def save():
    with open('laptops.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название ноутбука', 'Описание ноутбука', 'Цена ноутбука'])
    for item in list_laptop:
        writer.writerow([item['Название ноутбука'], item['Описание ноутбука'], item['Цена ноутбука']])


if __name__ == '__main__':
    pass
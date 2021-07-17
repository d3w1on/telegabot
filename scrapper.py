import os
import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.lapiec-pizza.com.ua/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.101 Safari/537.36'}


def discount_scrap():
    d_url = url + 'discount/'
    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/discount.html', 'w', encoding='utf-8') as f:
        f.write(requests.get(d_url, headers=headers).text)

    response = requests.get(d_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    links = soup.find_all('a', class_='imgWrapper')
    imgs = soup.find_all('a', class_='imgWrapper')
    texts = soup.find_all('h5', class_='h5')

    data_list = []
    for i in range(len(links)):
        data = {}
        link = links[i].get('href')
        data['link'] = link

        img = imgs[i].find('img').get('src')
        data['img'] = img

        text = texts[i].find('a').text.strip()
        data['text'] = str(text)
        data_list.append(data)

    with open('data/discount.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def pizza_scrap():
    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/pizza.html', 'w', encoding='utf-8') as f:
        f.write(requests.get(url, headers=headers).text)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    names = soup.find_all('div', class_='h5 as')
    links = soup.find_all('a', class_='productImage preview')
    imgs = soup.find_all('a', class_='productImage preview')
    prices = soup.find_all('div', class_='productPrice')
    descriptions = soup.find_all('div', class_='productDescription normall')
    sizes = soup.find_all('span', class_='size')
    weights = soup.find_all('span', class_='weight')

    data_list = []
    for i in range(len(names)):
        data = {}

        data['id'] = 'pizza'+str(i)

        name = names[i].text.strip()
        data['name'] = name

        price = prices[i].find('span').text.strip() + ' грн'
        data['price'] = price

        link = links[i].get('href')
        data['link'] = link

        img = imgs[i].get('data-preview')
        data['img'] = img

        desc = descriptions[i].find('p').text.strip()
        data['desc'] = desc

        size = sizes[i].text.strip() + ' см'
        data['size'] = size

        weight = weights[i].text.strip() + ' гр'
        data['weight'] = weight

        data_list.append(data)

    with open('data/pizza.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def salads_scrap():
    s_url = url + 'salaty/'
    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/salads.html', 'w', encoding='utf-8') as f:
        f.write(requests.get(s_url, headers=headers).text)

    response = requests.get(s_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    names = soup.find_all('div', class_='h5 as')
    imgs = soup.find_all('span', class_='productImage preview')
    prices = soup.find_all('div', class_='productPrice')
    descriptions = soup.find_all('div', class_='productDescription normall')
    weights = soup.find_all('span', class_='weight')

    data_list = []
    for i in range(len(names)):
        data = {}
        data['id'] = 'salad'+str(i)

        name = names[i].text.strip()
        data['name'] = name

        price = prices[i].find('span').text.strip() + ' грн'
        data['price'] = price

        img = imgs[i].get('data-preview')
        data['img'] = img

        desc = descriptions[i].find('p').text.strip()
        data['desc'] = desc

        weight = weights[i].text.strip()
        data['weight'] = weight

        data_list.append(data)

    with open('data/salads.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def dessert_scrap():
    new_url = url + 'desserts/'

    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/desserts.html', 'w', encoding='utf-8') as f:
        f.write(requests.get(new_url, headers=headers).text)

    response = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    names = soup.find_all('div', class_='h5 as')
    imgs = soup.find_all('span', class_='productImage preview')
    prices = soup.find_all('div', class_='productPrice')
    descriptions = soup.find_all('div', class_='productDescription normall')
    weights = soup.find_all('span', class_='weight')

    data_list = []
    for i in range(len(names)):
        data = {}
        data['id'] = 'dessert'+str(i)

        name = names[i].text.strip()
        data['name'] = name

        price = prices[i].find('span').text.strip() + ' грн'
        data['price'] = price

        img = imgs[i].get('data-preview')
        data['img'] = img

        desc = descriptions[i].find('p').text.strip()
        data['desc'] = desc

        weight = weights[i].text.strip()
        data['weight'] = weight

        data_list.append(data)

    with open('data/desserts.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def beverages_scrap():
    b_url = url + 'napoyi/'

    if not os.path.exists('data'):
        os.mkdir('data')
    with open('data/beverages.html', 'w', encoding='utf-8') as f:
        f.write(requests.get(b_url, headers=headers).text)

    response = requests.get(b_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    names = soup.find_all('div', class_='h5 as')
    imgs = soup.find_all('span', class_='productImage preview')
    prices = soup.find_all('div', class_='productPrice')

    data_list = []
    for i in range(len(names)):
        data = {}
        data['id'] = 'bev'+str(i)

        name = names[i].text.strip()
        data['name'] = name

        price = prices[i].find('span').text.strip() + ' грн'
        data['price'] = price

        img = imgs[i].get('data-preview')
        data['img'] = img


        data_list.append(data)

    with open('data/beverages.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)


def main():
    pizza_scrap()
    discount_scrap()
    salads_scrap()
    dessert_scrap()
    beverages_scrap()


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup
import csv
import argparse

parser = argparse.ArgumentParser(description='Parser')
parser.add_argument('url', type=str, help='URL to parse')
parser.add_argument('--num', type=int, default=10, help='Number of positions to parse')
args = parser.parse_args()

url = args.url
num = args.num

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
for i, item in enumerate(soup.find_all('a')[:num]):
    row = []
    row.append(i+1)
    row.append(item.get('href'))
    row.append(item.text)
    data.append(row)

# выводим результаты парсинга на страницу в виде таблицы
print('| Number | Link | Text |')
for row in data:
    print(f'| {row[0]} | {row[1]} | {row[2]} |')

# сохраняем результаты парсинга в текстовый файл
with open('results.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'Link', 'Text'])
    for row in data:
        writer.writerow(row)

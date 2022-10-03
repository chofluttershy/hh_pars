import requests
from bs4 import BeautifulSoup


url = "https://workius.ru/r/%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0/v/%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9_%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80/s/30000"

r = requests.get(url)
r.text

soup = BeautifulSoup(r.text, 'lxml')

vacancies = soup.findAll('div', class_='vacancy')
vacancies.pop(0)
vacancy = vacancies[0]

data = []

for vacancy in vacancies:
    name = vacancy.find('div', class_='vac_title').find('a').text
    salary = vacancy.find('div', class_='vac_title').find('span', class_='vac_salary').text
    location = vacancy.find('div', class_='vac_meta').find('span', class_='vac_location').text.replace('\n\n', '')
    employer = vacancy.find('div', class_='vac_meta').find('span', class_='vac_employer').text.replace(' ', '').replace(
        '\n', '').replace('\r', '')
    data.append([name, salary, location, employer])

#for i in data:
    #print(i)
print(vacancies)
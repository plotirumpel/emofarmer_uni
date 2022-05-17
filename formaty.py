import requests
from bs4 import BeautifulSoup

def courses (year,season):
    names_of_courses = []
    link = f'http://students.iposov.spb.ru/{str(year)}{season}/'
    response = requests.get(link).text
    html = BeautifulSoup(response, features="html.parser")
    section = html.find('section',{'class':'main-content'})
    ul = section.find('ul')
    ul2 = ul.find_all('ul')
    for i in range (len(ul2)):
        li = ul2[i].find_all('li')
        for j in range (len(li)):
            names_of_courses.append(li[j].find('a').text)
    return names_of_courses
#print(courses(19,'fall'))


def animals (name, part):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{name}').text
    html = BeautifulSoup(response, features="html.parser")
    all = html.find('table')
    div = all.find_all('div', {'class': 'ts-Taxonomy-rang-row'})
    for i in range(len(div)):
        div_deeper = div[i].find('div', {'class':'ts-Taxonomy-rang-label'})
        if div_deeper.text.replace(':','') == part:
            ans = div[i].find('div', {'class':'ts-Taxonomy-rang-name'})
            return ans.text.replace(':','')

def animals_1 (name):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{name}').text
    html = BeautifulSoup(response, features="html.parser")
    all = html.find('table')
    tb = all.find('tbody')
    td = tb.find('td', {'class':'plainlist'})
    div = td.find_all('div', {'class':'ts-Taxonomy-rang-row'})
    ans = {}
    for i in div:
        animal_class = i.find('div', {'class': 'ts-Taxonomy-rang-label'})
        animal_name = i.find('div', {'class': 'ts-Taxonomy-rang-name'})
        ans[animal_class.text.replace(':','')]=animal_name.text.replace(':','')
    return ans

#print(animals('Осьминоги', 'Домен'))
#print(animals_1('Осьминоги'))

import re
def wiki (link, ans):
    #print(ans)
    if len(ans) > 100 or link in ans:
        return (ans)
    ans.append(link)
    response = requests.get(link).text
    html = BeautifulSoup(response, features='html.parser')
    div = html.find('div', {'class': 'mw-parser-output'})
    p = div.find_all('p')
    p_n = re.sub(r'\(.+\)', '', str(p))
    hh = re.search(r'\/wiki\/(.*?)\"', p_n)
    next_link = f'https://ru.wikipedia.org/{hh.group(0)[:-1]}'
    #print(ans)
    return wiki(next_link, ans)

print(wiki('https://ru.wikipedia.org/wiki/%D0%A2%D0%B0%D0%BD%D0%B5%D1%86_%D0%94%D1%83%D0%BD%D1%8C%D1%85%D1%83%D0%B0%D0%BD%D0%B0', []))


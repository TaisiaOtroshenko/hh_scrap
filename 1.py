from lxml import html
import requests

headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
page = requests.get('https://kaluga.hh.ru/search/vacancy?text=&salary=&schedule=remote&professional_role=124&ored_clusters=true&items_on_page=100&order_by=publication_time&label=accredited_it&industry=7&excluded_text=&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'
                    , headers=headers)
tree = html.fromstring(page.content)
data = tree.xpath('/html/body/noindex/template//text()')[0]

with open ('file.json', 'w', encoding='utf-8') as file:
    file.write(data) 



import requests
from bs4 import BeautifulSoup

url = 'https://jisho.org/search/%23noun %23words?page='

def request_amount(x):
    total_count = 0
    for i in range(1,3):
        if total_count == x:
            break
        page = url + i
        next_page = requests.get(page)
        next_parse = BeautifulSoup(next_page.content, 'html.parser')

        word = next_parse.find('text').string
        print(word)
        total_count = total_count + 1
        

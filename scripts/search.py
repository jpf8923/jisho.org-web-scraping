import requests
from bs4 import BeautifulSoup
from jisho_api.kanji import Kanji
import pandas as pd

url = 'https://jisho.org/search/%23{} %23words?page='
df = pd.DataFrame([['kanji', 'hiragana', 'definitions']])

def request_type(search,x):
    for i in range(1,x+1):
        block = data(i, search)
        for section in block:
            kanji = section.find("span", class_="text")
            hiragana = section.find("span", class_="furigana").text.strip()
            if kanji.find("span") != None:
                hiragana = hiragana + kanji.find("span").text.strip()
            kanji = kanji.text.strip()
            definitions = Kanji.request(kanji).data.main_meanings
            append_dataFrame(kanji, hiragana, definitions)
    df.to_csv('cache/example.csv', index=False)
        
    
def append_dataFrame(kanji, hiragana, definitions):
    global df
    temp_df = pd.DataFrame([[kanji, hiragana, definitions]])
    df = pd.concat([df,temp_df])

def data(page_index, search):
    global url
    page = (url + str(page_index)).format(search)
    page_parse = BeautifulSoup(requests.get(page).content, 'html.parser')
    block = page_parse.find_all("div", class_ ="concept_light clearfix")
    return block
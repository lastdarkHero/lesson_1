import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")
    

def get_dollor_course():
    return soup.find("Valute", ID="R01235").Value.text

def get_evro_course():
    return soup.find("Valute", ID="R01239").Value.text



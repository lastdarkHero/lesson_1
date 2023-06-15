import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "xml")
    

def get_course(course_name):
    valutes_list = soup.find_all("Valute")

    for valute in valutes_list:
        if valute.Name.text.lower() == course_name.lower():
            return valute.Value.text
    



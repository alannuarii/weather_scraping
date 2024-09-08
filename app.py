import requests
from bs4 import BeautifulSoup as bs
from weather_code import code


def read_weather():
    url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiUtara.xml"
    response = requests.get(url, verify=True)
    r = response.text
    location = bs(r, 'xml')
    result = int(location.find(id="501536").find(id="weather").find(h="12").value.string)
    for index, item in enumerate(code):
        if item["code"] == result:
            return code[index]["weather"]
            


print(read_weather())
    



    
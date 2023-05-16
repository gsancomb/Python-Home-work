import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime

results = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.2988&lon=-76.9529')
soup = BeautifulSoup(results.text, "html.parser")

month = []
day = []
latitude = []
temp = []
relativehumid = []
windspeed = []
dewpoint = []

latitude = soup.find('span', class_='smallTxt').text
# temp
temp = soup.find('p', class_='myforecast-current-lrg').text

for tr in soup.find('div', id="current_conditions_detail").find_all('tr'):
    if tr.find('td').text == 'Humidity':
        relativehumid = tr.findAll('td')[1].text

    if tr.find('td').text == 'Wind Speed':
        windspeed = tr.findAll('td')[1].text

    if tr.find('td').text == 'Dewpoint':
        dewpoint = tr.findAll('td')[1].text

print(temp, relativehumid, windspeed, dewpoint)

today = datetime.datetime.now()

month = today.strftime("%m")
day = today.strftime("%d")


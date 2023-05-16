import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import re
from math import *

from pysolar.solar import *
import datetime

results = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.2988&lon=-76.9529')
soup = BeautifulSoup(results.text, "html.parser")

month = []
day = []
latitude = []
longitude = []
temp = []
relativehumid = []
windspeed = []
dewpoint = []
barometer = []

latitude = 39.17
longitude = -77.17
Zenith 
datetime.datetime()
# temp
temp = soup.find('p', class_='myforecast-current-lrg').text

for tr in soup.find('div', id="current_conditions_detail").find_all('tr'):
    if tr.find('td').text == 'Humidity':
        relativehumid = tr.findAll('td')[1].text

    if tr.find('td').text == 'Wind Speed':
        windspeed = tr.findAll('td')[1].text

    if tr.find('td').text == 'Dewpoint':
        dewpoint = tr.findAll('td')[1].text
    if tr.find('td').text == 'Barometer':
        barometer = tr.findAll('td')[1].text

print(temp, relativehumid, windspeed, dewpoint)

today = datetime.datetime.now()

month = today.strftime("%m")
day = today.strftime("%d")

temp = int(re.sub("[^0-9]", "", temp))
relativehumid = int(re.sub("[^0-9]", "", relativehumid))
windspeed = int(re.sub("[^0-9]", "", windspeed))
dewpoint = dewpoint.split(" ")
dewpoint = int(re.sub("[^0-9]", "", dewpoint[0]))
barometer = barometer.split("(")
barometer = int(re.sub("[^0-9]", "", barometer[1]))


#temp as a float
T = float(temp)
#humidity as decimal
rh = float(relativehumid) /100
#AMBEINT temp in C
ta = (float(temp) - 32) * .5556
Ta = (float(temp) - 32) * .5556
print(day, month, temp, relativehumid, windspeed, dewpoint, latitude)
#Wetbulbtemp = (-5.806 + 0.672 * ta - 0.006 * ta**2 + (0.061 + 0.004 * ta + 99 * 10 - 6 * ta ** 2) * RH + (-33 * 10 - 6 - 5 * 10 - 6 * ta - 1 * 10 - 7 * ta ** 2) * RH ** 2)
Wetbulbtemp = T * atan(0.151977 * (rh + 8.313659)**(1/2)) + atan(T + rh) - \
              atan(rh - 1.676331) + 0.00391838 * (rh)**(3/2) * atan(0.023101 * rh) - 4.686035
print (Wetbulbtemp)
globetemp = 1

WBGT = 0.7 * float(Wetbulbtemp) + 0.2 * globetemp + 0.1 * ta
sigma = 5.67*10**-8
Td = (float(dewpoint)- 32) * .5556

P = barometer
#Ea = exp(((17.67(Td-Ta))/(Td+243.5))) * (1.0007 + 0.00000346 * P) * 6.112 * exp((17.502* Ta) / (240.97+ Ta))

#epsilon_a = 0.575* Ea **(1/7)
#Z =
#B = S((Fdb)/4 * sigma * cos(Z)) + (1.2/sigma) * Fdif) + (epsilon_a) * Ta**4
#H = .315
#C = (H*U**0.58) / (5.3865*10**-8)

#globetemp = (B + CTa + 7680000)/ (C + 256000)




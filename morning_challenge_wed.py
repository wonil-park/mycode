#!/usr/bin/env python3

from requests import get
from requests.exceptions import RequestException
from wget import download

from api_key import key


def input_handler(question):
    valid_input_entered = False
    while not valid_input_entered:
        date = input(question)
        date_list = date.split("-")
        if int(date_list[0]) >= 1995:
            valid_input_entered = True
            return date
        else:
            print('Date must be between Jun 16, 1995 and today\'s date')


url = 'https://api.nasa.gov/planetary/apod?'
date = input_handler('Please enter the date of the APOD(YYYY-MM-DD): ')
hd = input('Would you like to download HD image or SD image? ')
url = f'{url}api_key={key}&date={date}'
try:
    res = get(url).json()

except RequestException as e:
    print(f'Request error: {e}')

criteria = ['date', 'title', 'explanation']
try:
    for el in criteria:
        print(f'{el.title()}: {res[el]}')
except:
    print('Error while fetching info from result')

if hd.lower() == 'hd':
    download(res['hdurl'])
else:
    download(res['url'])
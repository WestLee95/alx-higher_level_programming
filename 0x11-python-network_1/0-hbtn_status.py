#!/usr/bin/python3
from urllib.request import urlopen

def fetch_url(url):
    with urlopen(url) as response:
        data = response.read().decode()
    print(data.replace("\n", "\t- "))

fetch_url('https://alx-intranet.hbtn.io/status')

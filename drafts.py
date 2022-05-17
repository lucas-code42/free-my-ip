"""
###############################################
# LISTA DE SITES QUE CONTEM PROXIES GRATUITAS #
###############################################

http://free-proxy.cz/en/proxylist/country/BR/http/ping/all
https://www.sslproxies.org/
https://geonode.com/free-proxy-list/
https://hidemy.name/en/proxy-list/
http://httpbin.org/ip


###################################################
MODELO DE IMPLEMENTAÇÃO PARA SELENIUM E REQUESTS #
###################################################

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def selenium():
    proxy = '186.233.186.60:8080'

    chrome_op = webdriver.ChromeOptions()
    chrome_op.add_argument(f'--proxy-server={proxy}')
    # service = Service('/home/lucas-code42/Documents/developer/projects/qyon/cnd/Qyon.CND.Backend.Worker/selenium_bin/chromedriver_')
    driver = webdriver.Chrome(executable_path='/home/lcs-42/Documents/qyon/RPA/Qyon.CND.Backend.Worker/selenium_bin/chromedriver', options=chrome_op)

    driver.get('https://httpbin.org/ip')
    sleep(1000)

selenium()

########################################
MODELO DE IMPLEMENTAÇÃO PARA REQUESTS #
########################################

import requests

def requests_():
    url = 'http://httpbin.org/ip'
    session = requests.session()
    session.proxies = {
        'http': '189.126.72.97:20183',
        'https': '189.126.72.97:20183'
    }
    r = session.get(url=url)
    print(r.text)

requests_()
"""
import requests
from bs4 import BeautifulSoup as BSHTML

class FreeMyIp:

    def __init__(self) -> None:
        pass

    def get_random_proxies(self):
        random = []
        call_1 = self.get_proxies()
        random.append(call_1)
        call_2 = self.get_socks_proxies()
        random.append(call_2)
        call_3 = self.get_us_proxies()
        random.append(call_3)
        call_4 = self.get_uk_proxies()
        random.append(call_4)
        random = random[0]
        return random

    def get_proxies(self):
        try:
            url = 'https://free-proxy-list.net/'
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                html = response.text
                proxies = []
                soup = BSHTML(html, 'html.parser')
                for row in soup.find('table', attrs={'class': 'table table-striped table-bordered'}).find_all('tr')[1:]:
                    td = row.find_all('td')
                    try:
                        ip = td[0].text.strip()
                        port = td[1].text.strip()
                        proxies.append(str(ip) + ':' + str(port))
                    except IndexError:
                        continue
                return proxies
        except:
            return False
    
    def get_socks_proxies(self):
        try:
            url = 'https://www.socks-proxy.net/'
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                html = response.text
                proxies = []
                soup = BSHTML(html, 'html.parser')
                for row in soup.find('table', attrs={'class': 'table table-striped table-bordered'}).find_all('tr')[1:]:
                    td = row.find_all('td')
                    try:
                        ip = td[0].text.strip()
                        port = td[1].text.strip()
                        proxies.append(str(ip) + ':' + str(port))
                    except IndexError:
                        continue
                return proxies
        except:
            return False

    def get_us_proxies(self):
        try:
            url = 'https://www.us-proxy.org/'
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                html = response.text
                proxies = []
                soup = BSHTML(html, 'html.parser')
                for row in soup.find('table', attrs={'class': 'table table-striped table-bordered'}).find_all('tr')[1:]:
                    td = row.find_all('td')
                    try:
                        ip = td[0].text.strip()
                        port = td[1].text.strip()
                        proxies.append(str(ip) + ':' + str(port))
                    except IndexError:
                        continue
                return proxies
        except:
            return False

    def get_uk_proxies(self):
        try:
            url = 'https://free-proxy-list.net/uk-proxy.html'
            session = requests.session()
            response = session.get(url)
            if response.status_code == 200:
                html = response.text
                proxies = []
                soup = BSHTML(html, 'html.parser')
                for row in soup.find('table', attrs={'class': 'table table-striped table-bordered'}).find_all('tr')[1:]:
                    td = row.find_all('td')
                    try:
                        ip = td[0].text.strip()
                        port = td[1].text.strip()
                        proxies.append(str(ip) + ':' + str(port))
                    except IndexError:
                        continue
                return proxies
        except:
            return False



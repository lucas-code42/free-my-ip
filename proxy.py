import requests
from bs4 import BeautifulSoup as BSHTML

class FreeMyIp:

    def get_proxies(self, ):
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
    
    def get_socks_proxies(self, ):
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

    def get_us_proxies(self, ):
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

    def get_uk_proxies(self, ):
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
import time
import os
import http.cookiejar
import urllib.request

from bs4 import BeautifulSoup
import requests

## Login with building cookies
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
AUTH_URL = 'https://mbasic.facebook.com/login.php'
payload = {
    'email': 'alexparryleon@gmail.com',
    # 'pass': os.environ['AlexPass']
}
print(os.environ.get('USER'))
print(dir(os.environ))
print(type(os.environ))
auth_encode_data = urllib.parse.urlencode(payload).encode('utf-8')
_req = urllib.request.Request(AUTH_URL, auth_encode_data)
_resp = urllib.request.urlopen(_req)
auth_content = _resp.read()

## Scraping 
URL = 'https://mbasic.facebook.com/browse/group/members/?id=867105006641269&start=0&listType=list_nonfriend_nonadmin&refid=18'

source = requests.get(URL , cookies=cj).text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
user = soup.find('table', id="member_100007389550978")
# print(user)


def simple_sleep():
    print("Printed immediately.")
    time.sleep(1.4)
    print("Printed after 1.4 seconds.")

simple_sleep()



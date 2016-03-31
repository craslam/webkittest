import requests
import sys
# web login and requests

with requests.Session() as c:
    URL = 'http://192.168.127.144/bWAPP/htmli_get.php'
    USERNAME = 'bee'
    PASSWORD = 'box'
    SECLVL = 0
    c.get(URL)

    #The next paramenter is used incase the URL dosn't work
    login_data = dict(login=USERNAME, password=PASSWORD, security_level=0, next='/')
    #Login, first argument to post is the url to post, then the argument for data is the dict created above
    c.post(URL, data=login_data, headers={"Referer": "http://192.168.127.144/"}, cookies=c.cookies)
    #alot of websites reject posts with out headers, so Referer is the website we visited to get to the login screen
    page = c.get('http://192.168.127.144/bWAPP/portal.php')
    print page.content

    print login_data




    ##p = requests.post('http://192.168.127.144/bWAPP/htmli_get.php', payload)

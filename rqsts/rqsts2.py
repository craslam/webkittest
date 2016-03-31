import requests

with requests.Session() as s:
    USERNAME = 'bee'
    PASSWORD = 'box'
    URL1 = 'http://192.168.127.144/bWAPP/htmli_get.php'
    URL2 = 'http://192.168.127.144/bWAPP/portal.php'
    login_data = dict(login=USERNAME, password=PASSWORD, next='/')
    r = s.get(URL1)
    # r = s.post(URL2, data=login_data, cookies=)
    page = s.get(URL2)
    print page.content

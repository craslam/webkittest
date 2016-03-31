from browsermobproxy import Server
server = Server("/root/Desktop/browsermob-proxy-2.1.0-beta-4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://www.google.co.uk")
test = proxy.har # returns a HAR JSON blob

print test

server.stop()
driver.quit()
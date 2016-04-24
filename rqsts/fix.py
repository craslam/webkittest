from browsermobproxy import Server
import re, sys, json,pprint, base64, binascii
import argparse

# Proxy server
server = Server("/root/Desktop/browsermob-proxy-2.1.0-beta-5/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select


# Fetch username, password input boxes and submit button

def fsbmt():
    '''
    locate sumit button
    '''
    try:
        try:
            fsbmt.submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            fsbmt.submit = driver.find_element_by_xpath("//input[@type='submit']")
    except:
        print "could not locate submit button \n"
        submit_name = raw_input("What is the submit box HTML name? ")
        fsbmt.submit = driver.find_element_by_name(submit_name)


def auth(auth1):
    '''
    Asks the user if the site to be scanned has authentication
    '''
    looper = True
    while looper == True:
        login_url = raw_input("What is the URL of the login page you want to access? ")
        if login_url.startswith("http://"):
            try:
                driver.get(login_url)
                looper = False

            except:
                print "Something went wrong trying to load the URL please re-enter the URL \n"
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

    args = parser.parse_args()
    my_opt.URL = args.url
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
proxy.new_har("DanW")  # proxy name

# #uncomment to reparse args
# my_opt()
# #args-url location
# driver.get(my_opt.URL)
#

#Testing Delete later
#Testing Auth____ Comment IN TO autologin Bwap
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

target_url = 'http://192.168.127.144/bWAPP/xss_get.php?'
#BWAPP TEST Start
#XXS GET TEST
driver.get(target_url)
#
#driver.get('''http://192.168.127.144/bWAPP/xss_get.php?firstname="><script>alert("l33thax")</script>&lastname="><script>alert("l33thax")</script>&form=submit ''')
# exit(0)

# # Testing Auth____ Comment IN TO autologin DVWA
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
# driver.get("http://192.168.127.178/dvwa/vulnerabilities/xss_r/")

# # attack ulr test
# driver.get("http://192.168.127.178/dvwa/vulnerabilities/xss_r/?name=%22%3E%3Cscript%3Ealert%28%22l33thax%22%29%3C%2Fscript%3E")
# exit(1)

#token = "document.cookie"
token = "l33thax"

# Payload Variables


def PAYLOAD():
    '''
    XSS Payloads
    '''
    PAYLOAD.PLD1 = "<script>alert(" + token + ")</script>"
    PAYLOAD.PLD2 = """'';!--"<b>b</bhttps://www.youtube.com/watch?v=nYeHCXHBskI><""" + token + """>=&{()}"""
    PAYLOAD.PLD3 = "><script>alert(document.cookie)</script>"

    PAYLOAD.PLDA = '''"><x>AppCheck</x>'''
    PAYLOAD.PLDB = '''"><script>AppCheck</script>'''
    PAYLOAD.PLDC = '''"><script>alert("''' + token + '''")</script>'''

# def PAYLOAD():
#     '''
#     XSS Payloads
#     '''
#     PAYLOAD.PLD1 = '''"><x>''' + token+ '''</x>'''
#     PAYLOAD.PLD2 = '''"><script>''' + token + '''</script>'''
#     PAYLOAD.PLD3 = '''"><script>alert("''' + token + '''")</script>'''
#     PAYLOAD.PLD4 = """'';!--"<b>b</b><""" + token + """>=&{()}"""


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
            ('"', '%93'),
            (">", '%3E'),
            ("<", '%3C'),
            ("&", "%26"),
            ("(", '%28'),
            (")", '%29')

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

def construct_url(target,nmlst,vllst):
    '''
    construct URL from HAR
    :param target:
    :param nmlst:
    :param vllst:
    :return:
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

    else:
        print "somthing went wrong aquiring name and value pairs"
        exit(1)

    #replace with custom attack strings
    # cycle2 = 0
    #
    # for i in vllst:
    #     if token in i:
    #         vllst[cycle2] = pload
    #         cycle2 += 1

    # Construst Payload url
    list_value = 0
    while nv_len >0:
        for nm in nmlst:
            payload_url.append(nm)
            payload_url.append('=')
            payload_url.append(vllst[list_value])
            payload_url.append('&')
            list_value += 1
            nv_len -= 1
    payload_url

    at = ''.join(payload_url)
    construct_url.attack_string = at[:-1]

def alert_dection(inum):
    # --------- Try to switch to dialogue screen, wait three seconds if no there,
    global alerts_detected
    for num in range(inum):
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' + 'confirmation popup to appear.')

            driver.switch_to.alert

            a = Alert(driver).text
            if a == token:
                print "a %s has been detected \n" % a
                alerts_detected += 1
            else:
                print "An unexpected alert box was accepted"
            Alert(driver).accept()

            # print check
        except TimeoutException:
            print "no alert"


def XSS_ref():
    # locate submit
    global alerts_detected
    try:
        try:
            submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            submit = driver.find_element_by_xpath("//input[@type='submit']")
    except:
        print "could not locate submit button \n"
        submit_name = raw_input("What is the submit box HTML name? ")
        submit = driver.find_element_by_name(submit_name)

    INPUT = driver.find_elements_by_tag_name('input')
    input_num = 0

    # attempt payload1
    for i in INPUT:
        i.send_keys(PAYLOAD.PLDC)
        input_num += 1
        # print "Number of tokens detected in Reflected Get " + tokencount
        # print json.dumps(HAR)
    submit.click()
    HAR = proxy.har
    # #HarDepug print in format
    # print HAR
    #print json.dumps(HAR, sort_keys=True, indent=4)
    #reg_slice(str(HAR))
    # construct Payload URL based on target URL, name list from HAR,
    #PLD_URL1 = construct_url(target_url, reg_slice.nm_lst, reg_slice.vl_lst)
    #print PLD_URL1
    alert_dection(input_num)


    # if nothing is detected cycle through payloads
    # if alerts_detected == 0:
    #     try:
    #         # Decoded payload URL = 192.168.127.144/bWAPP/xss_get.php?firstname="><script>alert("l33thax")</script>&lastname="><script>alert("l33thax")</script>&form=submit
    #         # construct payload string
    #         driver.get()

    #detect = re.findall(r"%s" % token, str(HAR))
    #tokencount = len(detect)
    XSS_refToken = alerts_detected

    if XSS_refToken > 0:
        print "Number of XSS_Ref tokens detected %s " % XSS_refToken
        alerts_detected += XSS_refToken
    else:
        print "No injection points were detected on the selected site"
        print XSS_refToken
        # print HAR
        # json_parsed = json.lo(str(HAR))
        # print json.dumps(json_parsed, indenpt=4, sort_keys=True)

XSS_ref()

# DVWA input
# submit = driver.find_element_by_xpath('//*[@id="main_body"]/div/div/form/input[2]')


# #Bwap input
# submit = driver.find_element_by_name("form")
# submit.click()

def ref_get():
    HAR = proxy.har
    alerts_detected = 0
    # print HAR
    detect = re.findall(r"<%s>" % token, str(HAR))
    tokencount = str(len(detect))
    print "Number of tokens detected in Reflected Get " + tokencount
    print json.dumps(HAR)


def main():
    return True

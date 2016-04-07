import base64
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
            ('"','%93'),
            (">",'%3E'),
            ("<",'%3C'),
            ("&","%26"),
            ("(",'%28'),
            (")",'%29')

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

# fudgepacker = url_encode(PLOAD2)
# fudge = html_encode(PLOAD2)
# print PLOAD2 + "\n"
# print fudge + "\n"
# print fudgepacker + "\n"


%3Cscript%3Ealert%28%271%27%29%3C/script%3E
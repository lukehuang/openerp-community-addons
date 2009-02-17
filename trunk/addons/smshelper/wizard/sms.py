# -*- coding: UTF-8 -*-

import urllib
import urllib2

ENCODING = 'gb2312'
URL = 'http://www.smshelper.com:8090/sendsms'

def send_sms(username, password, phone, text):
    url = URL
    args = {    'user' : username,
                'pwd' : password,
                'phone' : phone,
                'msg' : text.decode('utf-8').encode(ENCODING) }
    data = urllib.urlencode(args) 
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    the_page = response.read()

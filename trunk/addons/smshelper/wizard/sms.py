# -*- coding: UTF-8 -*-

#    Copyright (C) 2009-TODAY 李维 <oldrev@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


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

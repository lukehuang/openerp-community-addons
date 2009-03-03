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


from osv import osv, fields

class smshelper_message_template(osv.osv):
    _name = 'smshelper.message_template'
    _description = '消息模板'
    _columns = {
            'name': fields.char('名称', required=True, size=50),
            'content': fields.text('内容', required=True),
        }
    _order = 'name'
smshelper_message_template()


class smshelper_account(osv.osv):
    _name = 'smshelper.account'
    _description = '短信服务商帐号'
    _columns = { 
            'name': fields.char('名称', required=True, size=50),
            'username': fields.char('用户名', required=True, size=64),
            'password': fields.char('密码', required=True, size=64),
        }
    _order = 'name'
smshelper_account()

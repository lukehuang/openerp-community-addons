# -*- coding: UTF-8 -*-
##############################################################################
# 作者：oldrev <oldrev@gmail.com>
##############################################################################

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

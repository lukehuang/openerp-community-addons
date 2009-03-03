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


import wizard
import netsvc
import pooler
import sms

sms_send_form = '''<?xml version="1.0"?>
<form string="%s">
    <separator string="%s" colspan="4"/>
    <newline/>
    <field name="template_id" colspan="4"/>
    <field name="account_id" colspan="4"/>
</form>''' % ('短信服务','短信')


def _sms_send(self, cr, uid, data, context):
    service = netsvc.LocalService("object_proxy")

    account = service.execute(cr.dbname, uid, 'smshelper.account', 'read', data['form']['account_id'])
    template = service.execute(cr.dbname, uid, 'smshelper.message_template', 'read', data['form']['template_id'])
    text = template['content']

    res_ids = service.execute(cr.dbname, uid, 'res.partner.address', 'search', [('partner_id','in',data['ids'])])
    res = service.execute(cr.dbname, uid, 'res.partner.address', 'read', res_ids, ['mobile'])

    nbr = 0
    for r in res:
        to = r['mobile']
        if to:
            sms.send_sms(account['username'], account['password'], to, text)
            nbr += 1
    return {'sms_sent': nbr}

def _get_templates(self, cr, uid, context):
    module_obj=pooler.get_pool(cr.dbname).get('smshelper.message_template')
    ids=module_obj.search(cr, uid, [])
    res=[(m.id, m.name) for m in module_obj.browse(cr, uid, ids)]
    res.sort()
    return res

def _get_accounts(self, cr, uid, context):
    module_obj=pooler.get_pool(cr.dbname).get('smshelper.account')
    ids=module_obj.search(cr, uid, [])
    res=[(m.id, m.name) for m in module_obj.browse(cr, uid, ids)]
    res.sort()
    return res

sms_send_fields = {
    #'text': {'string':'短信内容', 'type':'text', 'required':True}

    'template_id': {
        'string':'短信模板',
        'type':'selection',
        'selection':_get_templates,
        'default': -1,
        'required': True,
        },

    'account_id': {
        'string':'帐号',
        'type':'selection',
        'selection':_get_accounts,
        'default': -1,
        'required': True,
        },
}

class part_sms(wizard.interface):


    states = {
        'init': {
            'actions': [],
            'result': {'type': 'form', 'arch':sms_send_form, 'fields': sms_send_fields, 'state':[('end','取消'), ('send','发送')]}
        },
        'send': {
            'actions': [_sms_send],
            'result': {'type': 'state', 'state':'end'}
        }
    }
part_sms('smshelper.sms_send')



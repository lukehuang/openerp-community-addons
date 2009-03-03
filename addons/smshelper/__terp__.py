##############################################################################
#    作者：oldrev <oldrev@gmail.com>

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

##############################################################################


{
	"name": "SMSHelper 批量短信发送工具",
	"version": "0.1",
	"description": "SMSHelper 批量短信发送工具。\n采用 smshelper.com 提供的 URL 方式接口批量发送短信。",
	"author" : "李维 <oldrev@gmail.com>",
	"depends": ['base',],
	"category": "Generic Modules/Tire",
	"init_xml": [],
	"update_xml": [
        "smshelper_view.xml", 
        "smshelper_wizard.xml", 
    ],
	"demo_xml": [],
	"active": False,
	"installable": True,
}

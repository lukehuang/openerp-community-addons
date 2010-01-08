# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2009 Gábor Dukai
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Chinese Unicode Reports with TrueType fonts",
    "version" : "1.1",
    "author" : "oldrev/digitalsatori",
    "description": """
    此模块用于为 OpenERP 的基础系统提供汉化，仅依赖内置的 base 模块。\n\n
    
    此模块包含如下功能：\n
    1.  为 OpenERP 的 RML/PDF 报表提供中文字体支持\n
    2.  为 OpenERP 添加中文省份数据\n
    \n

    使用文泉驿正黑体和 AR PL SungtiL GB 宋体替换系统原来不支持 Unicode 的英文字体，安装此模块可以自动使内置的报表自动支持中文字体。 \n
    NOTE: 直接解压复制到 addons 目录. 不用导入!\n
    原始 base_report_unicode 模块作者：Gábor Dukai
        
    """,
    "depends" : ["base"],
    "category" : "Generic Modules/Base",
    'init_xml': [
        'data/base_data.xml',
    ],
    "demo_xml" : [],
    "update_xml" : [],
    "license": "GPL-3",
    "active": True, #这选项让此模块自动安装
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


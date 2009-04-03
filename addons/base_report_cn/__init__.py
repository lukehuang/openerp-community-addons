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

from tools.config import config
import report
import os

def wrap_trml2pdf(method):
    """We have to wrap the original parseString() to modify the rml data
    before it generates the pdf."""
    def convert2TrueType(*args, **argv):
        """This function replaces the type1 font names with their truetype
        substitutes and puts a font registration section at the beginning
        of the rml file. The rml file is acually a string (data)."""
        odata = args[0]
        fontmap = {
            'Times-Roman':                   'SimSun',
            'Times-BoldItalic':              'SimSun',
            'Times-Bold':                    'SimSun',
            'Times-Italic':                  'SimSun',

            'Helvetica':                     'SimHei',
            'Helvetica-BoldItalic':          'SimHei',
            'Helvetica-Bold':                'SimHei',
            'Helvetica-Italic':              'SimHei',

            'Courier':                       'SimSun',
            'Courier-Bold':                  'SimSun',
            'Courier-BoldItalic':            'SimSun',
            'Courier-Italic':                'SimSun',

            'Helvetica-ExtraLight':          'SimHei',

            'TimesCondensed-Roman':          'SimSun',
            'TimesCondensed-BoldItalic':     'SimSun',
            'TimesCondensed-Bold':           'SimSun',
            'TimesCondensed-Italic':         'SimSun',

            'HelveticaCondensed':            'SimHei',
            'HelveticaCondensed-BoldItalic': 'SimHei',
            'HelveticaCondensed-Bold':       'SimHei',
            'HelveticaCondensed-Italic':     'SimHei',
        }
        i = odata.find('<docinit>')
        if i == -1:
            i = odata.find('<document')
            i = odata.find('>', i)
            i += 1
            starttag = '\n<docinit>\n'
            endtag = '</docinit>'
        else:
            i = i + len('<docinit>')
            starttag = ''
            endtag = ''
        data = odata[:i] + starttag
        adp = os.path.normcase(os.path.abspath(config['addons_path']))
        for new in fontmap.itervalues():
            data += '    <registerFont fontName="' + new + '" fontFile="' + adp + '/base_report_cn/fonts/' + new + '.ttf"/>\n'
        data += endtag + odata[i:]
        for  old, new in fontmap.iteritems():
            data = data.replace(old, new)
        return method(data, args[1:], **argv)
    return convert2TrueType

report.render.rml2pdf.parseString = wrap_trml2pdf(report.render.rml2pdf.parseString)

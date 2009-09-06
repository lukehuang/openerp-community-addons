import os

from relatorio.templates.opendocument import Template

import report
from report.report_sxw import *
from osv import osv,fields

import relatorio_report


def create_single_odt(self, cr, uid, ids, data, report_xml, context=None):
    if not context:
        context={}
    context = context.copy()
    report_type = report_xml.report_type
    context['parents'] = sxw_parents

    sxw_path = os.path.realpath("bin/addons/" + report_xml.report_sxw)
    odt_template = Template(source=None, filepath=sxw_path)
    openerp_objects = self.getObjects(cr, uid, ids, context)
    odt_generated = odt_template.generate(objects=openerp_objects).render()
    final_op = odt_generated.getvalue() 
    return (final_op, report_type)

report_sxw.create_single_odt=create_single_odt

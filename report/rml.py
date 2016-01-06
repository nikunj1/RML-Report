import time

from openerp.report import report_sxw

class order(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(order, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time, 
        })

report_sxw.report_sxw('report.sale.order.school', 'sale.order', 'addons/school/report/report.rml', parser=order, header="False")

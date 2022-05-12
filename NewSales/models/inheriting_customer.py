from odoo import models, fields, api


class InheritCustomer(models.Model):
    _inherit = 'customer.detail'
    _description = 'Inheriting customer in new model'

    customer_description = fields.Many2one('product.template', string='Customer Description')


class SalesInherit(models.Model):
    _inherit = 'sales.order'
    _description = 'Inheriting in sales'

    customer_desc = fields.Char(string='Sales Description')

    @api.onchange('customer_desc')
    def _desc_change(self):
        for rec in self:
            if rec.customer_desc:
                rec.sales_ids.desc = rec.customer_desc
                print(rec.sales_ids.desc)

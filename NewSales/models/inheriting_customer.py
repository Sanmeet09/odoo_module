from odoo import models,fields,api


class InheritCustomer(models.Model):
    _inherit = 'customer.detail'
    _description = 'Inheriting customer in new model'


    customer_description = fields.Many2one('product.template', string='Customer Description')


class SalesInherit(models.Model):
    _inherit = 'sales.order'
    _description = 'Inheriting in sales'


    customer_desc = fields.Char(string='Sales Description')
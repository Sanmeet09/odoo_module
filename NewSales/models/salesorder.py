from odoo import models,fields,api


class SalesOrder(models.Model):
    _name = 'sales.order'
    _description = 'My Sales App'

    # logic
    sales_id = fields.Many2one('customer.detail', String='Sales List')
    gender = fields.Selection(selection=[('m','Male'),('f','Female')], default='m', String='Gender')
    mobile = fields.Char(string='Mobile', size=10)
    date = fields.Date(string='Date')






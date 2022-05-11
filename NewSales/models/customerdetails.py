from odoo import models,fields,api


class CustomerDetails(models.Model):
    _name = 'customer.detail'
    _description = 'new module'

    name = fields.Many2one('res.partner', 'Customer Name')
    age = fields.Integer('Age')
    mobile = fields.Char('Mobile No')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female')], default='m', String='Gender')
from odoo import models,fields,api


class CustomerDetails(models.Model):
    _name = 'customer.detail'
    _description = 'new module'

    name = fields.Many2one('res.partner', 'Customer Name')
    age = fields.Integer('Age')
    mobile = fields.Char('Mobile No')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female')], default='m', String='Gender')

    product_ids = fields.One2many('customerdetail.line', 'product_id', 'Product line')


class CustomerDetailLine(models.Model):
    _name = 'customerdetail.line'
    _description = 'one2many field in customer'

    product = fields.Char('Product')
    quantity = fields.Integer('Quantity')
    price = fields.Integer('Price')

    product_id = fields.Many2one('customer.detail','Product Id')
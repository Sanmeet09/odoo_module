from odoo import models,fields,api, _
from odoo.exceptions import ValidationError, UserError
from datetime import date
from dateutil.relativedelta import relativedelta


class CustomerDetails(models.Model):
    _name = 'customer.detail'
    _description = 'new module'

    name = fields.Many2one('res.partner', 'Customer Name')
    age = fields.Integer('Age', compute='_cal_age')
    comment = fields.Char('Comments')
    mobile = fields.Char('Mobile No')
    dob = fields.Date('Date of birth', default=date.today())
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female')], default='m', String='Gender')

    product_ids = fields.One2many('customerdetail.line', 'product_id', 'Product line')

    @api.onchange('name')
    def compute_desc(self):
        for rec in self:
            rec.comment = rec.name.name

    @api.constrains('age')
    def check_dat(self):
        for rec in self:
            if rec.age >=100:
                raise ValidationError('You are too old')


    @api.depends('dob')
    def _cal_age(self):
        for i in self:
            if i.dob:
                today = date.today()
                age = relativedelta(today, i.dob).years
                i.age = age





class CustomerDetailLine(models.Model):
    _name = 'customerdetail.line'
    _description = 'one2many field in customer'

    product = fields.Char('Product')
    quantity = fields.Integer('Quantity')
    price = fields.Integer('Price')

    product_id = fields.Many2one('customer.detail','Product Id')




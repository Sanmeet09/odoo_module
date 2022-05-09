from odoo import fields,api,models

class DemoModel(models.Model):
    _name = "demo.new"

    _description = 'Demo Module'

    #logic
    name = fields.Char(String='Name')
    dob =fields.Date(String='Date of Birth')
    gender = fields.Selection(selection=[('m', 'Male'),('f','Female')] ,default='m', String='Gender')
    address =fields.Char(String='Address')
    mobile = fields.Char(string='Mobile', size=10)
    add = fields.Binary(string='Add a File')

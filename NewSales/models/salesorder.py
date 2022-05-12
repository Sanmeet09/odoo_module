from odoo import models,fields,api


class SalesOrder(models.Model):
    _name = 'sales.order'
    _rec_name='tname'
    _description = 'My Sales App'

    # logic
    sales_id = fields.Many2one('customer.detail', String='Sales List')
    gender = fields.Selection(selection=[('m','Male'),('f','Female')], default='m', String='Gender')
    mobile = fields.Char(string='Mobile', size=10)
    date = fields.Date(string='Date')
    fname = fields.Char('First Name')
    lname = fields.Char('Last Name')
    # tname = fields.Char('Full Name',compute='_full_name')
    tname = fields.Char('Full Name')


    # sales One2many field id
    sales_ids = fields.One2many('salesorder.line','sales_id','Sales Line')

    # @api.depends('fname','lname')
    # def _full_name(self):
    #     for rec in self:
    #         rec.tname = rec.fname+rec.lname

    @api.onchange('fname','lname')
    def _full_name(self):
        for rec in self:
            if rec.fname and rec.lname:
                rec.tname = rec.fname+" "+rec.lname






class SalesOrderLine(models.Model):
    _name='salesorder.line'
    _description = 'one2many field in sales'


    sales_id = fields.Many2one('sales.order', 'Sales Id')
    sales_name = fields.Char('Name')
    products = fields.Char('Products')
    quantity = fields.Integer('Quantity')
    desc= fields.Char('Description')








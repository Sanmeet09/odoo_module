from odoo import models,api,fields, _

class DoctorDetails(models.Model):
    _name= 'doctor.details'
    _rec_name = 'doctor_name'
    _description= 'details of all the Docotrs'


    doctor_name = fields.Char('Doctor Name')
    age = fields.Integer('Age')
    desc = fields.Char('Description')
    salary = fields.Integer('Salary')
    exp = fields.Integer('Experience')
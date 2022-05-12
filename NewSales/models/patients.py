from odoo import models, fields, api, _


class PatientDetails(models.Model):
    _name = 'patient.details'
    _rec_name='patient_name'
    _description = 'Details of all the patients'

    patient_name = fields.Char('Name')
    gender = fields.Selection(selection=[('m', 'Male'), ('f', 'Female')], default='m', string='Gender')
    age = fields.Integer('Age')
    description = fields.Char('Description')
    doctor_name = fields.Many2one('doctor.details', 'Doctor Name')

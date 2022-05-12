from odoo import models,fields,api, _


class WardDetails(models.Model):
    _name = 'ward.details'
    _rec_name = 'ward_no'
    _description = 'details of ward and doctor'

    ward_no = fields.Integer('Ward No')
    doctor = fields.Many2one('doctor.details', 'Doctor Name')


    def search_patient(self):
        pass

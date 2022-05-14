from odoo import models, fields, api, _


class WardDetails(models.Model):
    _name = 'ward.details'
    _rec_name = 'ward_no'
    _description = 'details of ward and doctor'

    ward_no = fields.Integer('Ward No')
    doctor = fields.Many2one('doctor.details', 'Doctor Name')
    ward_ids = fields.One2many('detailsward.line','ward_id', 'Ward Line')

    # def search_patient(self):
    #     patient_id =  self.env['patient.details'].create({
    #         'patient_name': 'Sanjeev',
    #         'gender':'m',
    #         'age':18,
    #         'description':'Created from ward'
    #     })

    def search_patient(self):
        for rec in self:
            # patient_id_search = self.env['patient.details'].search_count([('doctor_name', '=', rec.doctor.id)])
            patient_id_search = self.env['patient.details'].search([('doctor_name', '=', rec.doctor.id)])
            print(patient_id_search)

            patient_id_search.unlink()

            # patient_id = patient_id_search.write({
            #     'patient_name': 'Sanjeev',
            #     'gender': 'm',
            #     'age': 18,
            #     'description': 'Created from ward'
            # })
            # print(patient_id)


class CreateWizardLine(models.Model):
    _name = 'detailsward.line'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    disease = fields.Char('Disease')
    doctor = fields.Char('Doctor Name')

    ward_id = fields.Many2one('ward.details', 'wizard Id')


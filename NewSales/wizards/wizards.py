from odoo import models, fields, api, _


class CreateDetailsWizard(models.TransientModel):
    _name = 'create.details.wizard'
    _description = 'starting Wizard'

    name = fields.Char('Name')
    age = fields.Integer('Age')
    disease = fields.Char('Disease')
    doctor_id = fields.Many2one('doctor.details', 'Doctor Name')


    def save_record(self):
        return self.env['patient.details'].create({
            'patient_name': self.name,
            'age': self.age,
            'doctor_name': self.doctor_id.id
        })


    def save_down(self):
        return self.env['detailsward.line'].create({
            'name': self.name,
            'age': self.age,
            'disease': self.disease,
            'doctor': self.doctor_id.id
        })








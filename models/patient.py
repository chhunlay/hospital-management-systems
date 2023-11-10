from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Management Systems"

    name = fields.Char(string="Patient Name", tracking=True, required=True)
    reference = fields.Char(string="Reference", tracking=True, required=True)
    age = fields.Integer(sgring="Age", tracking=True, required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")



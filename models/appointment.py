from odoo import api, models, fields, _

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Management Systems"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    patient_id = fields.Many2one(
        comodel_name="hospital.patient", 
        string="Patient")

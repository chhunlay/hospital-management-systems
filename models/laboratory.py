from odoo import api, models, fields, _

class HospitalLabTest(models.Model):
    _name = "hospital.lab.test"
    _description = "Lab Tests"

    name = fields.Char(string="Test Name", required=True)
    result = fields.Char(string="Test Result")
    appointment_id = fields.Many2one(
        comodel_name="hospital.appointment",
        string="Appointment"
    )

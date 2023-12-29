from odoo import api, models, fields, _

class HospitalPharmacyOrder(models.Model):
    _name = "hospital.pharmacy.order"
    _description = "Pharmacy Orders"

    # Add relevant fields for pharmacy orders
    name = fields.Char(string="Order Reference", required=True)
    appointment_id = fields.Many2one(
        comodel_name="hospital.appointment",
        string="Appointment"
    )
    # Add more fields as needed
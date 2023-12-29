from odoo import api, models, fields, _

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Management Systems"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Appointment Reference', 
        required=True, 
        copy=False, 
        readonly=True, 
        index=True, 
        default=lambda self: _('New'))

    patient_id = fields.Many2one(
        comodel_name="res.partner",
        string="Patient")
    
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")

    doctor_id = fields.Many2one(
        comodel_name="res.partner",
        string="Doctor",
        # domain="[('is_doctor', '=', True)]",  # Assuming you have a field is_doctor in res.partner model
        required=True
    )

    appointment_date = fields.Datetime(
        string="Appointment Date and Time",
        required=True
    )

    appointment_duration = fields.Float(
        string="Appointment Duration (in hours)",
        help="Specify the duration of the appointment in hours"
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', track_visibility='onchange')

    contact_number = fields.Char(string="Contact Number")
    address = fields.Text(string="Address")
    medical_history = fields.Text(string="Medical History")

    specialization = fields.Char(string="Specialization")
    qualification = fields.Char(string="Qualification")
    doctor_contact_number = fields.Char(string="Doctor Contact Number")
    doctor_address = fields.Text(string="Doctor Address")

    insurance_provider = fields.Char(string="Insurance Provider")
    policy_number = fields.Char(string="Policy Number")
    insurance_validity = fields.Date(string="Insurance Validity")

    total_cost = fields.Float(string="Total Cost")
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid')
    ], string="Payment Status", default='unpaid')
    payment_date = fields.Date(string="Payment Date")

    appointment_notes = fields.Text(string="Appointment Notes")
    lab_test_requests = fields.One2many(
        comodel_name="hospital.lab.test",
        inverse_name="appointment_id",
        string="Lab Test Requests"
    )

    reminder_date = fields.Datetime(string="Reminder Date")

    bed_allocated = fields.Boolean(string="Bed Allocated")
    bed_number = fields.Char(string="Bed Number")

    pharmacy_order_ids = fields.One2many(
        comodel_name="hospital.pharmacy.order",
        inverse_name="appointment_id",
        string="Pharmacy Orders"
    )

    # sequence 
    @api.model  
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or 'New'
        return super(HospitalAppointment, self).create(vals)

    # Additional fields for patient history tracking
    symptoms = fields.Text(string="Symptoms")
    diagnosis = fields.Text(string="Diagnosis")
    prescription = fields.Text(string="Prescription")

    # action button
    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

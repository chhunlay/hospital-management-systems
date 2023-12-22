from odoo import api, models, fields, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Management Systems"
    _inherit = ["mail.thread", "mail.activity.mixin"]
 
    patient_id = fields.Many2one(
        comodel_name="res.partner", 
        string="Patient", 
        required=True, 
        tracking=True)
    age = fields.Integer(string="Age", tracking=True, required=True, compute="_compute_age")
    gender = fields.Selection(
        [('male', 'Male'), 
         ('female', 'Female')], 
         string="Gender")
    phone = fields.Char(string='Phone')
    dob = fields.Date(string="Date of Birth", required=True)
    img = fields.Image(string="Image", help="Select patient profile.")
    # reference
    name = fields.Char(string="Reference",
        readonly=True, 
        copy=False, 
        tracking=True,
        default=lambda self: _('New'))

    # sequence 
    @api.model  
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'
        return super(HospitalPatient, self).create(vals)
    
    # get name
    def name_get(self):
        result = []
        for request in self:
            result.append((request.id, "%s" % (request.name)))
        return result
    
    @api.depends('dob')
    def _compute_age(self):
        for patient in self:
            if patient.dob:
                today = fields.Date.today()
                dob = fields.Date.from_string(patient.dob)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                patient.age = age
            else:
                patient.age = 0



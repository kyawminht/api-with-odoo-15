from importlib.metadata import files

from odoo import models, fields

class StandardCV(models.Model):
    _name = "standard.cv"
    _description = "Standard CV"
    _table = "standard_cv"

    name=fields.Char(string="Career Name",required=True)
    address=fields.Char(string="Address",required=True)
    nationality=fields.Char(string="Nationality",required=True)
    phone=fields.Char(string="Phone Number",required=True)
    dob=fields.Date(string="Date Of Birth",required=True)
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender")
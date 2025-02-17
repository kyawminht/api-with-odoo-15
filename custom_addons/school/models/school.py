from odoo import models,fields

class School(models.Model):
    _name = "school.school"
    _description = "school management"

    name=fields.Char(string="name")
    address=fields.Char(string="description")
from odoo import models,fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'student for the school'

    name=fields.Char(string="Student Name")
    age=fields.Integer(string="Age")
    attend=fields.Boolean(string="Attend")
    grade=fields.Char(string="Grade")
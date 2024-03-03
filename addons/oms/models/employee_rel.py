# -*- coding: utf-8 -*-

from odoo import models, fields


class EmployeeRel(models.Model):
    _name = 'employee_rel'
    _description = 'Employee Relation model'

    employee_id = fields.Many2one('hr.employee.public')
    role = fields.Selection([ ('worker', 'Worker'),('kolonne', 'Kolonne'),],'Role', default='worker', required=True)
    task_id = fields.Many2one('task', string='Task')

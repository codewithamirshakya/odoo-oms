# -*- coding: utf-8 -*-

from odoo import models, fields


class employee(models.Model):
    _name = 'employee'
    _description = 'Employee model'

    name = fields.Char(string="Name", required=True)
    role = fields.Selection([ ('worker', 'Worker'),('kolonne', 'Kolonne'),],'Role', default='worker', required=True)
    remarks = fields.Text(string="Remarks")
    task_id = fields.Many2one('task', string='Task')



    



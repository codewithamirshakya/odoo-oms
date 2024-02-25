# -*- coding: utf-8 -*-

from odoo import models, fields


class employee(models.Model):
    _name = 'employee'
    _description = 'Employee model'

    name = fields.Char()
    role = fields.Selection([ ('worker', 'Worker'),('kolonne', 'Kolonne'),],'Role', default='worker')


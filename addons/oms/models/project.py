# -*- coding: utf-8 -*-

from odoo import models, fields


class employee(models.Model):
    _name = 'project'
    _description = 'Project model'

    name = fields.Char()
    description = fields.Text()
    status = fields.Boolean(string="Status", default=False)


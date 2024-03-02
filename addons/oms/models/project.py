# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'project'
    _description = 'Project model'

    project_no = fields.Char(string="Project Number", required=True)
    name = fields.Char(string="Project name", required=True)
    description = fields.Text()
    isActive = fields.Boolean(string="Is Active", default=False)


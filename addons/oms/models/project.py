# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'project'
    _rec_name = 'project_name'
    _description = 'Project model'

    project_index = fields.Integer(string="Project Index", required=True)
    project_category = fields.Char(string="Project category", required=True)
    ww_updated_on = fields.Datetime(string="Ww updated on")
    project_status = fields.Char(string="Project Status", default=0)
    alternative_project_number = fields.Char(string="Alternate Project Number",)
    is_active = fields.Boolean(string="Is Active", default=False)
    project_number = fields.Char(string="Project Number")
    project_name = fields.Char(string="Project Name", required=True)
    client_id = fields.Many2one('client',string="Client ID", required=True)

    _sql_constraints = [
        ('project_index', 'unique(project_index)', 'Product index. should be unique.'),
    ]


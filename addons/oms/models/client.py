# -*- coding: utf-8 -*-

from odoo import models, fields


class client(models.Model):
    _name = 'client'
    _description = 'Client model'

    name = fields.Char()
    description = fields.Text()
    status = fields.Boolean(string="Status", default=False)


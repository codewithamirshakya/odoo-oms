# -*- coding: utf-8 -*-

from odoo import models, fields


class Client(models.Model):
    _name = 'client'
    _description = 'Client model'

    # attributes
    client_index = fields.Integer(string="Client index", required=True)
    name = fields.Char(string="Client", required=True)
    client_office = fields.Char(string="Client office", required=True)
    street_and_number = fields.Char(string="Street and number")
    zip_and_city = fields.Char(string="Zip and city", required=True)

    _sql_constraints = [
        ('client_index', 'unique(client_index)', 'Client index. should be unique.'),
    ]

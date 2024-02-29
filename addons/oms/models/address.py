# -*- coding: utf-8 -*-

from odoo import models, fields


class Address(models.Model):
    _name = 'address'
    _description = 'Address model'

    name = fields.Text()

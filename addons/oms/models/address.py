# -*- coding: utf-8 -*-

from odoo import models, fields


class Address(models.Model):
    _name = 'address'
    _description = 'Address model'

    address = fields.Text()

    task_ids = fields.One2many('task', 'address_id', string='Task')



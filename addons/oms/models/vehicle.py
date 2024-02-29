# -*- coding: utf-8 -*-

from odoo import models, fields


class Vehicle(models.Model):
    _name = 'vehicle'
    _description = 'Vehicle model'

    # attributes
    license_plate_no = fields.Char(string="License plate number", required=True)
    driver_name = fields.Char(string="Driver name", required=True)

    task_id = fields.Many2one('task', string='Task')

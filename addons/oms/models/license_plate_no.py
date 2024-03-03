# -*- coding: utf-8 -*-

from odoo import models, fields


class LicensePlateNo(models.Model):
    _name = 'license_plate_no'
    _description = 'License plate model'
    _rec_name = 'license_plate_no'

    # attributes
    license_plate_no = fields.Char(string="License plate number", required=True)

    _sql_constraints = [
        ('license_plate_no', 'unique(license_plate_no)', 'License number. should be unique.'),
    ]

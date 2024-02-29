# -*- coding: utf-8 -*-

from odoo import models, fields


class Task(models.Model):
    _name = 'task'
    _description = 'Task model'

    # attributes
    project_id = fields.Many2one("project",string="Project", required=True)

    partner_id = fields.Many2one('res.partner', string='Customer', auto_join=True, tracking=True, required=True)

    vehicle_ids = fields.One2many('vehicle', 'task_id', string='Vehicles')

    employee_ids = fields.One2many('employee', 'task_id', string='Employees', required=True)


    date = fields.Date(string="Date", required=True)
    # type = fields.Selection([ ('permanent', 'Permanent'),('temporary', 'Temporary'),],'Type', default='permanent', string="Art", )

    type = fields.Selection([
        ('permanent', 'Permanent'),
        ('temporary', 'Temporary'),
        # Add more options as needed
    ], string='Art', default="temporary")
    
    address_id = fields.Many2one('address',string="Object Description", required=True)
    work_description = fields.Text(string="Work description", required=True)
    # additional_description = fields.Selection([ ('aufbau', 'Aufbau'),('demontage', 'Demontage'),('regie', 'Regie'),('sonstiges', 'Sonstiges')],'Role', default='aufbau', required=True)
    # additional_description = fields.Text()
    additional_description = fields.Selection([
        ('aufbau', 'Aufbau'),
        ('demontage', 'Demontage'),
        ('regie', 'Regie'),
        ('sonstiges', 'Sonstiges')
        # Add more options as needed
    ], string='Art', default="aufbau")

    client_id = fields.Integer(string="Client")

    time = fields.Char(string='Time', required=True)

    ap = fields.Char(string="Work Load")
    vws = fields.Boolean(string="Delivery")


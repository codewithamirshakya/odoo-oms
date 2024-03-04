# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'task'
    _description = 'Task model'

    # attributes
    project_id = fields.Many2one("project",string="Project", required=True)
    client_id = fields.Many2one("client",string="Client", required=True)


    # partner_id = fields.Many2one('res.partner', string='Customer', auto_join=True, tracking=True, required=True)

    vehicle_ids = fields.One2many('vehicle', 'task_id', string='Vehicles')

    manager_id = fields.Many2one('hr.employee.public', string='Manager')

    employee_ids = fields.One2many('employee_rel', 'task_id', string='Employees', required=True)
    employee_ids_count = fields.Integer(string='Employees', compute='_compute_m2m_count')


    date = fields.Datetime(string="Date", required=True)

    type = fields.Selection([
        ('permanent', 'Fest'),
        ('temporary', 'Temporär'),        
    ], string='Art', default=None, required=False)
    
    work_description = fields.Text(string="Work description", required=True)
    
    work_category = fields.Selection([
        ('aufbau', 'Aufbau'),
        ('demontage', 'Demontage'),
        ('regie', 'Regie'),        
        ('lagern', 'Lagern'),
        ('transport', 'Transport'),
        ('sonstiges', 'Sonstiges'),
        ('fehlzeiten', 'Fehlzeiten')
    ], string='Work Category', default="aufbau")

    # client_id = fields.Integer(string="Client")

    bericht = fields.Boolean(string="Bericht")


    @api.onchange('client_id')
    def _onchange_client_id(self):
        for rec in self:
            return {'domain': {'project_id': [('client_id','=', rec.client_id.id)]}}
        
    def _compute_m2m_count(self):
        for record in self:
            record.employee_ids_count = len(record.employee_ids) 


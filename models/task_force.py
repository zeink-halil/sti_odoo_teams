# -*- coding: utf-8 -*-

from odoo import fields, models


class TaskForce(models.Model):
    _name = "task.force"
    _description = "Task Force for projects"

    name = fields.Char(string='Name', help='Task Force Name')
    manager_id = fields.Many2one('hr.employee', 'Manager')
    members_ids = fields.Many2many('hr.employee', 'task_force_member', 'task_force_id', 'emp_id', string='Members')
    project_id = fields.One2many(
        'project.project',
        'task_force_id',
        string='Project',
        store='True'
    )

    def action_get_project_record(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Project',
            'view_mode': 'form',
            'res_model': 'project.project',
            'domain': [('task_force_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def open_project(self):
        self.ensure_one()
        return {
            'name': 'Project',
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': self.project_id.id,
            'target': 'current',
        }

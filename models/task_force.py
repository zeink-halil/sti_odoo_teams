# -*- coding: utf-8 -*-

from odoo import fields, models


class TaskForce(models.Model):
    _name = "task.force"
    _description = "Task Force for projects"

    name = fields.Char(string='Name', help='Task Force Name')
    manager_id = fields.Many2one('hr.employee', 'Manager')
    members_ids = fields.Many2many('hr.employee', 'task_force_member', 'task_force_id', 'emp_id', string='Members')

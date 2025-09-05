# -*- coding: utf-8 -*-

from odoo import models, fields
class ProjectProject(models.Model):
    _inherit = "project.project"

    task_force_ids = fields.Many2many('task.force', 'active_task_force', 'project_id', 'task_force_ids')
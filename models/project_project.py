# -*- coding: utf-8 -*-

from odoo import models, fields
class ProjectProject(models.Model):
    _inherit = "project.project"

    task_force_id = fields.Many2one('task.force', string='Task Force', readonly=False   )

    _sql_constraints = [
        ('unique_task_force', 'unique(task_force_id)', 'Each task force can be assigned to only one project.')
    ]
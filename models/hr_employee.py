# -*- coding: utf-8 -*-

from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    team_ids = fields.Many2many(
        'hr.department', 'team_ids', 'emp_id', 'team_id',
        string="Team",
        groups="hr_attendance.group_hr_attendance_officer,hr.group_hr_user")

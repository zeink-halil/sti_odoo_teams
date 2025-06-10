# -*- coding: utf-8 -*-


{
    'name': "sti_odoo_team",

    'summary': "Enhances HR by allowing employees to belong to multiple teams instead of a single department.",

    'description': """<h3>STI HR Teams</h3> <p> This module enhances the HR system by introducing a 
    <strong>team-based structure</strong> instead of relying on the traditional single-department setup. </p> <ul> 
    <li>Allows employees to belong to multiple teams (Many2many relationship)</li></li> <li>Customizes the employee 
    form to display teams instead of departments</li></ul> <p> Ideal for initiatives and organizations where cross-functional
     teams are more relevant than hierarchical departments. </p> """,

    'author': "Zein Al-Abideen",
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/hr_employee_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [

        ],
    }
}

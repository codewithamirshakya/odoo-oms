# -*- coding: utf-8 -*-
{
    'name': "Work Order Management",

    'summary': "Effizientes Management von Arbeitsaufträgen und Teamkoordination.",

    'description': """Effizientes Management von Arbeitsaufträgen und Teamkoordination""",

    'author': "Nextly Solutions GmbH",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tasks.xml',
        'views/client.xml',
        'views/projects.xml',
        'views/vehicles.xml',
        'views/menu.xml',
        'views/report_task_details.xml',
        'views/report_task_subcontractor_details.xml',
        'reports/report_action.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}


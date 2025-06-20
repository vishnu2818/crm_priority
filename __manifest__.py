# -*- coding: utf-8 -*-
{
    'name': "CRM Lead Priority",
    'description': """
        Adds priority to CRM leads and auto-sets based on revenue.
    """,
    'author': "Vishnu B",
    'website': "https://github.com/vishnu2818",
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm', 'base_automation'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'data/server_action.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

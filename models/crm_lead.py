# -*- coding: utf-8 -*-
from odoo import models, fields, api

PRIORITY = [
    ('0', 'Low'),
    ('1', 'Medium'),
    ('2', 'High'),
]


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    priority = fields.Selection(PRIORITY, string='Priority')

# -*- coding: utf-8 -*-
# from odoo import http


# class CrmPriority(http.Controller):
#     @http.route('/crm_priority/crm_priority', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_priority/crm_priority/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_priority.listing', {
#             'root': '/crm_priority/crm_priority',
#             'objects': http.request.env['crm_priority.crm_priority'].search([]),
#         })

#     @http.route('/crm_priority/crm_priority/objects/<model("crm_priority.crm_priority"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_priority.object', {
#             'object': obj
#         })

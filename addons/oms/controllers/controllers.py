# -*- coding: utf-8 -*-
# from odoo import http


# class Oms(http.Controller):
#     @http.route('/oms/oms', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oms/oms/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('oms.listing', {
#             'root': '/oms/oms',
#             'objects': http.request.env['oms.oms'].search([]),
#         })

#     @http.route('/oms/oms/objects/<model("oms.oms"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oms.object', {
#             'object': obj
#         })


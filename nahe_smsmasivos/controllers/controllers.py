# -*- coding: utf-8 -*-
# from odoo import http


# class NaheSmsmasivos(http.Controller):
#     @http.route('/nahe_smsmasivos/nahe_smsmasivos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_smsmasivos/nahe_smsmasivos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_smsmasivos.listing', {
#             'root': '/nahe_smsmasivos/nahe_smsmasivos',
#             'objects': http.request.env['nahe_smsmasivos.nahe_smsmasivos'].search([]),
#         })

#     @http.route('/nahe_smsmasivos/nahe_smsmasivos/objects/<model("nahe_smsmasivos.nahe_smsmasivos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_smsmasivos.object', {
#             'object': obj
#         })

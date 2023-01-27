# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo.tools import pdf
from datetime import datetime
from odoo.exceptions import ValidationError
from datetime import datetime
from odoo.exceptions import ValidationError

class Vehicles(models.Model):
    _inherit = 'fleet.vehicle'

    orders_count = fields.Integer(compute='compute_count')
    future_orders_count = fields.Integer(compute='future_orders_counts')
    delivery_orders = fields.One2many('stock.picking', 'partner_id',
                                      'Delivery Orders')

    def get_future_orders(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Orders',
            'view_mode': 'tree',
            'res_model': 'stock.picking',
            'domain': ['&',('partner_id', '=', self.driver_id.id),('scheduled_date', '>=', datetime.today())],
            'context': "{'create': False}"
        }

    def future_orders_counts(self):
        for record in self:
            record.future_orders_count = self.env['stock.picking'].search_count(
                [('partner_id', '=', self.driver_id.id),('scheduled_date', '>=', datetime.today())])

    def get_orders(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Orders',
            'view_mode': 'tree',
            'res_model': 'stock.picking',
            'domain': [('partner_id', '=', self.driver_id.id)],
            'context': "{'create': False}"
        }

    def compute_count(self):
        for record in self:
            record.orders_count = self.env['stock.picking'].search_count(
                [('partner_id', '=', self.driver_id.id)])

    @api.model
    def odoo_button_click_send_notifications(self):
        drivers = self.env['res.partner'].search([('is_driver', '=', True)])
        data = self.env['mail.message'].create({
            'message_type': "notification",
            'body': "Please Take a Order From Pending Order",
            'subject': "Pending Orders",
            'partner_ids': [(4, user.id) for user in drivers],
            'model': self._name,
            'res_id': self.id,
            'author_id': self.env.user.partner_id and self.env.user.partner_id.id
        })
        return True
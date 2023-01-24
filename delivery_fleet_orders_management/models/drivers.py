# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo.tools import pdf


class Drivers(models.Model):
    _inherit = 'res.partner'
    is_driver = fields.Boolean(string="Is Driver?", help="Is Driver?", default=False)
    # vehicle_id = fields.Many2many('fleet.vehicle', 'fleet_vehicle_rel', 'vehicle_id', 'driver_id',
    #                               'Vehicles')
    vehicle_id = fields.One2many('fleet.vehicle','driver_id','Vehicles')

    delivery_orders = fields.One2many('stock.picking','partner_id',
                                  'Delivery Orders')
    vehicle_count = fields.Integer(compute='compute_count')

    def get_vehicles(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Vehicles',
            'view_mode': 'tree',
            'res_model': 'fleet.vehicle',
            'domain': [('driver_id', '=', self.id)],
            'context': "{'create': True}"
        }

    def compute_count(self):
        for record in self:
            record.vehicle_count = self.env['fleet.vehicle'].search_count(
                [('driver_id', '=', self.id)])
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo.tools import pdf
from datetime import datetime
from odoo.exceptions import ValidationError

class Orders(models.Model):
    _inherit = 'stock.picking'

    def write(self, vals):
        if 'scheduled_date' in vals:
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            if self.picking_type_id.code == "outgoing" and vals['scheduled_date'] < date:
                raise ValidationError('Scheduled Date/Picking Date must be >= today')

        result = super(Orders, self).write(vals)
        return result

    @api.model
    def create(self, vals):
        picking_type_id = int(vals['picking_type_id'])
        if picking_type_id:
            picking_type = self.env['stock.picking.type'].browse(vals['picking_type_id'])
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            if 'scheduled_date' in vals:
                if picking_type.code == "outgoing" and vals['scheduled_date'] < date:
                    raise ValidationError('Scheduled Date/Picking Date must be >= today')
        records = super(Orders, self).create(vals)
        return records

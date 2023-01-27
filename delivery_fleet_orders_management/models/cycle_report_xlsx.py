# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo.tools import pdf


class PartnerXlsx(models.AbstractModel):
    _name = 'report.fleet.vehicle.report_fleet_vehicle_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, obj.name, bold)
            sheet.write(1, 0, "Vehicle Model:", bold)
            sheet.write(1, 1, obj.brand_id.name + '/' + obj.model_id.name, )
            sheet.write(2, 0, "Driver Name", bold)
            sheet.write(2, 1, obj.driver_id.name, )
            sheet.write(3, 0, "Future Orders", bold)
            sheet.write(3, 1, obj.future_orders_count, )
            sheet.write(4, 0, "All Orders", bold)
            sheet.write(4, 1, obj.orders_count, )

            sheet.write(6, 0, "Scheduled Date", bold)
            sheet.write(6, 1, "Shipping Policy", bold)
            row = 7
            for line in obj.driver_id.delivery_orders_data:
                col = 0
                sheet.write(row, col, line.scheduled_date, )
                col = 1
                sheet.write(row, col, line.move_type, )
                row += 1




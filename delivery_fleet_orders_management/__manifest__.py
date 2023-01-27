# -*- coding: utf-8 -*-
{
    'name': "Delivery Fleet Orders Management",
    'author': "Mahmoud El-Badry",
    'summary': """
        Delivery Fleet Orders Management""",
    'description': """
        Delivery Fleet Orders Management
    """,
    'depends': ['sale', 'account', 'point_of_sale','fleet','report_xlsx'],

    'data': [
        'views/delivery_menu.xml',
        'views/drivers_views.xml',
        'views/vehicle_views.xml',
        'views/cycle_report.xml',
        'views/report_fleet_vehicle.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'delivery_fleet_orders_management/static/src/js/vehicle.js',
        ],
        'web.assets_qweb': [
            'delivery_fleet_orders_management/static/src/xml/vehicle_button.xml',
        ],
    },
}

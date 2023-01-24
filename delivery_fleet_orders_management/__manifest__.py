# -*- coding: utf-8 -*-
{
    'name': "Delivery Fleet Orders Management",
    'author': "Delivery Fleet Orders Management",
    'summary': """
        Delivery Fleet Orders Management""",
    'description': """
        Delivery Fleet Orders Management
    """,
    'depends': ['sale', 'account', 'point_of_sale'],

    'data': [
        'views/delivery_menu.xml',
        'views/drivers_views.xml',
        'views/vehicle_views.xml',
    ],
    # 'web.assets_backend': [
    #     'static/src/js/vehicle.js',
    # ],
    # 'web.assets_qweb': [
    #     'static/src/xml/pos.xml',
    # ],
    'assets': {
        'web.assets_backend': [
            'delivery_fleet_orders_management/static/src/js/vehicle.js',
        ],
        'web.assets_qweb': [
            'delivery_fleet_orders_management/static/src/xml/pos.xml',
        ],
    },
}

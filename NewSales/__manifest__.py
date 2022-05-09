{
    'name': 'New Sales',
    'version': '1.1',
    'author': 'Planet Odoo',
    'description': """ module of Sanmeet""",
    'category': '',
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_order_view.xml',
        'views/customer_details_view.xml',


    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

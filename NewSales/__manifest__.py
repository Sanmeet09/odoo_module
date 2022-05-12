{
    'name': 'New Sale',
    'version': '1.1',
    'author': 'Planet Odoo',
    'description': """ module of Sanmeet""",
    'category': '',
    'website': '',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_order_view.xml',
        'views/customer_details_view.xml',
        'views/sale.xml',
        'views/inherit_customer.xml',
        'views/sales_inherit_view.xml',
        'views/patients_view.xml',
        'views/doctor_view.xml',
        'views/ward_view.xml',

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

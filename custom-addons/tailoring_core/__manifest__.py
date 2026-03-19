{
    'name': 'Tailoring Management',
    'version': '19.0.1.0.0',
    'category': 'Industries',
    'summary': 'Complete tailoring and garment management system',
    'description': """
        Tailoring Management System
        ===========================
        - Customer body measurements tracking
        - Tailoring orders with workflow states
        - Garment types catalog
        - Integration with Sales and Invoicing
        - Dashboard and reports
    """,
    'author': 'Tailoring Consult',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale',
        'contacts',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/garment_type_views.xml',
        'views/customer_measurement_views.xml',
        'views/tailoring_order_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

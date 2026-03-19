{
    'name': 'Tailoring Consult ERP - Branding',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Custom branding for Tailoring Consult ERP',
    'description': """
        Tailoring Consult ERP Branding
        ==============================
        - Replaces default branding with Tailoring Consult ERP
        - Custom colors and styling
        - Removes third-party references
    """,
    'author': 'Tailoring Consult',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['web', 'tailoring_core'],
    'data': [
        'views/webclient_templates.xml',
        'views/login_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tailoring_branding/static/src/css/branding.css',
            'tailoring_branding/static/src/xml/systray.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

{
    'name': 'Tailoring Consult ERP - Branding',
    'version': '19.0.3.0.0',
    'category': 'Tools',
    'summary': 'Enterprise-style home menu and theme for Tailoring Consult ERP',
    'description': """
        Tailoring Consult ERP Branding
        ==============================
        - Enterprise-style full screen home menu with app grid
        - Gradient background like Odoo Enterprise
        - Custom brand colors and navbar
        - Removes third-party references
    """,
    'author': 'Tailoring Consult',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
        'views/login_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # SCSS
            'tailoring_branding/static/src/scss/home_menu.scss',
            'tailoring_branding/static/src/scss/theme.scss',
            # JS
            'tailoring_branding/static/src/js/home_menu.js',
            'tailoring_branding/static/src/js/webclient.js',
            'tailoring_branding/static/src/js/navbar.js',
            # OWL XML
            'tailoring_branding/static/src/xml/home_menu.xml',
            'tailoring_branding/static/src/xml/webclient.xml',
            'tailoring_branding/static/src/xml/systray.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

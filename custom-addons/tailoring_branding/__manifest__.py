{
    'name': 'Tailoring Consult ERP - Branding',
    'version': '19.0.2.0.0',
    'category': 'Tools',
    'summary': 'Enterprise-style theme with sidebar navigation for Tailoring Consult ERP',
    'description': """
        Tailoring Consult ERP Branding
        ==============================
        - Enterprise-style sidebar navigation with app icons
        - Modern color scheme and typography
        - White navbar with dark sidebar
        - Custom branding throughout the UI
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
            # SCSS (load sidebar first since it changes layout)
            'tailoring_branding/static/src/scss/sidebar.scss',
            'tailoring_branding/static/src/scss/theme.scss',
            # JS components
            'tailoring_branding/static/src/js/sidebar.js',
            'tailoring_branding/static/src/js/webclient.js',
            # OWL XML templates
            'tailoring_branding/static/src/xml/sidebar.xml',
            'tailoring_branding/static/src/xml/webclient.xml',
            'tailoring_branding/static/src/xml/systray.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

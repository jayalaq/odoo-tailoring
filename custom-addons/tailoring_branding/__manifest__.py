{
    'name': 'Tailoring Consult ERP - Branding',
    'version': '19.0.2.0.0',
    'category': 'Tools',
    'summary': 'Enterprise-style theme with sidebar navigation for Tailoring Consult ERP',
    'description': """
        Tailoring Consult ERP Branding
        ==============================
        - Enterprise-style sidebar navigation
        - Modern color scheme and typography
        - Custom branding throughout the UI
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
            # SCSS theme
            'tailoring_branding/static/src/scss/sidebar.scss',
            'tailoring_branding/static/src/scss/theme.scss',
            # JS components
            'tailoring_branding/static/src/js/sidebar.js',
            'tailoring_branding/static/src/js/webclient.js',
            # XML templates
            'tailoring_branding/static/src/xml/sidebar.xml',
            'tailoring_branding/static/src/xml/webclient.xml',
            'tailoring_branding/static/src/xml/systray.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

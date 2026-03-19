from odoo import models, fields


class GarmentType(models.Model):
    _name = 'tailoring.garment.type'
    _description = 'Garment Type'
    _order = 'name'

    name = fields.Char(string='Garment Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    base_price = fields.Float(string='Base Price', digits=(10, 2))
    estimated_days = fields.Integer(
        string='Estimated Days',
        default=7,
        help='Estimated production time in days',
    )
    active = fields.Boolean(default=True)
    measurement_ids = fields.Many2many(
        'tailoring.measurement.type',
        string='Required Measurements',
        help='Measurements needed for this garment type',
    )

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Garment code must be unique!'),
    ]

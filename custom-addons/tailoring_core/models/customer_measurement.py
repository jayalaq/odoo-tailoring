from odoo import models, fields, api


class MeasurementType(models.Model):
    _name = 'tailoring.measurement.type'
    _description = 'Measurement Type'
    _order = 'sequence, name'

    name = fields.Char(string='Measurement Name', required=True)
    code = fields.Char(string='Code', required=True)
    sequence = fields.Integer(default=10)
    unit = fields.Selection([
        ('cm', 'Centimeters'),
        ('in', 'Inches'),
    ], string='Unit', default='cm', required=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Measurement code must be unique!'),
    ]


class CustomerMeasurement(models.Model):
    _name = 'tailoring.customer.measurement'
    _description = 'Customer Measurement'
    _order = 'partner_id, date desc'

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        ondelete='cascade',
    )
    date = fields.Date(
        string='Measurement Date',
        default=fields.Date.today,
        required=True,
    )
    notes = fields.Text(string='Notes')
    line_ids = fields.One2many(
        'tailoring.customer.measurement.line',
        'measurement_id',
        string='Measurements',
    )

    def name_get(self):
        return [
            (rec.id, f"{rec.partner_id.name} - {rec.date}")
            for rec in self
        ]


class CustomerMeasurementLine(models.Model):
    _name = 'tailoring.customer.measurement.line'
    _description = 'Customer Measurement Line'

    measurement_id = fields.Many2one(
        'tailoring.customer.measurement',
        string='Measurement',
        required=True,
        ondelete='cascade',
    )
    measurement_type_id = fields.Many2one(
        'tailoring.measurement.type',
        string='Measurement Type',
        required=True,
    )
    value = fields.Float(string='Value', digits=(10, 2), required=True)
    unit = fields.Selection(
        related='measurement_type_id.unit',
        string='Unit',
        readonly=True,
    )

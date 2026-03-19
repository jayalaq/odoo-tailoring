from odoo import models, fields, api
from datetime import timedelta


class TailoringOrder(models.Model):
    _name = 'tailoring.order'
    _description = 'Tailoring Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_order desc, id desc'

    name = fields.Char(
        string='Order Reference',
        required=True,
        copy=False,
        readonly=True,
        default='New',
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        tracking=True,
    )
    date_order = fields.Date(
        string='Order Date',
        default=fields.Date.today,
        required=True,
        tracking=True,
    )
    date_deadline = fields.Date(
        string='Delivery Date',
        tracking=True,
    )
    measurement_id = fields.Many2one(
        'tailoring.customer.measurement',
        string='Customer Measurements',
        domain="[('partner_id', '=', partner_id)]",
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cutting', 'Cutting'),
        ('sewing', 'Sewing'),
        ('fitting', 'Fitting'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True, required=True)
    line_ids = fields.One2many(
        'tailoring.order.line',
        'order_id',
        string='Order Lines',
    )
    notes = fields.Text(string='Internal Notes')
    customer_notes = fields.Text(string='Customer Notes')
    total_amount = fields.Float(
        string='Total Amount',
        compute='_compute_total_amount',
        store=True,
        digits=(10, 2),
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        readonly=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )

    @api.depends('line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.line_ids.mapped('subtotal'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'tailoring.order'
                ) or 'New'
        return super().create(vals_list)

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_cutting(self):
        self.write({'state': 'cutting'})

    def action_sewing(self):
        self.write({'state': 'sewing'})

    def action_fitting(self):
        self.write({'state': 'fitting'})

    def action_ready(self):
        self.write({'state': 'ready'})

    def action_deliver(self):
        self.write({'state': 'delivered'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})


class TailoringOrderLine(models.Model):
    _name = 'tailoring.order.line'
    _description = 'Tailoring Order Line'

    order_id = fields.Many2one(
        'tailoring.order',
        string='Order',
        required=True,
        ondelete='cascade',
    )
    garment_type_id = fields.Many2one(
        'tailoring.garment.type',
        string='Garment Type',
        required=True,
    )
    fabric_description = fields.Char(string='Fabric / Material')
    quantity = fields.Integer(string='Quantity', default=1, required=True)
    unit_price = fields.Float(
        string='Unit Price',
        digits=(10, 2),
        required=True,
    )
    subtotal = fields.Float(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True,
        digits=(10, 2),
    )
    notes = fields.Text(string='Special Instructions')

    @api.depends('quantity', 'unit_price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.unit_price

    @api.onchange('garment_type_id')
    def _onchange_garment_type(self):
        if self.garment_type_id:
            self.unit_price = self.garment_type_id.base_price

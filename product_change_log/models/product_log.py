from odoo import models, fields

class ProductChangeLog(models.Model):
    _name = 'product.change.log'
    _description = 'Historial de cambios del producto'
    _order = 'change_date desc'

    product_id = fields.Many2one('product.template', string='Producto', required=True)
    user_id = fields.Many2one('res.users', string='Usuario', default=lambda self: self.env.user)
    change_date = fields.Datetime(string='Fecha', default=fields.Datetime.now)

    field_name = fields.Char(string='Campo')
    old_value = fields.Text(string='Valor anterior')
    new_value = fields.Text(string='Valor nuevo')

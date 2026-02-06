from odoo import models
from odoo import fields

change_log_ids = fields.One2many(
    'product.change.log',
    'product_id',
    string='Historial'
)


TRACK_FIELDS = [
    'name',
    'default_code',
    'list_price',
    'standard_price',
    'barcode',
    'categ_id',
    'type',
]

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        for record in self:
            for field in TRACK_FIELDS:
                if field in vals:
                    old_value = record[field]
                    new_value = vals[field]

                    if old_value != new_value:
                        self.env['product.change.log'].create({
                            'product_id': record.id,
                            'field_name': field,
                            'old_value': str(old_value),
                            'new_value': str(new_value),
                        })

        return super(ProductTemplate, self).write(vals)

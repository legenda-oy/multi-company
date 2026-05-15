from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _check_company_auto = True

    categ_id = fields.Many2one(
        check_company=True,
    )

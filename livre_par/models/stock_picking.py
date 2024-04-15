from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    livre_par = fields.Char(string='Livré par' , required=True , inverse='_inverse_project_type_id')

    def _inverse_project_type_id(self):
        for picking in self:
            sale_order = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
            if sale_order:
                sale_order.livre_par = picking.livre_par
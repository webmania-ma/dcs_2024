from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    livre_par = fields.Char(string='Livré par', required=True)



    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.picking_ids:
                for picking in order.picking_ids:
                    picking.write({'livre_par': order.livre_par})
        return res

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['livry_par'] = self.livre_par
        return invoice_vals

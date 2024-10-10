from odoo import models, fields, api , _

from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    livre_par = fields.Selection(
        selection='_get_livre_par_selection',  # Dynamic selection method
        help='Livré par'
    )

    @api.model
    def _get_livre_par_selection(self):
        livre_par_options = []

        chauffeur_partners = self.env['res.partner'].search([('est_un_chauffeur', '=', True)])
        for partner in chauffeur_partners:
            livre_par_options.append((str(partner.id), partner.name))

        return livre_par_options

    def action_confirm(self):
        # Call the super method to handle the core confirmation process
        res = super(SaleOrder, self).action_confirm()

        # Ensure that the picking is updated with livre_par
        for order in self:
            if not order.livre_par:
                raise UserError(_("You must select a delivery method (Livre par) before confirming the sale order."))

            if order.picking_ids:
                for picking in order.picking_ids:
                    picking.write({'livre_par': order.livre_par})

        return res

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['livry_par'] = self.livre_par
        return invoice_vals
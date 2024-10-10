from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    livre_par = fields.Selection(
        selection='_get_livre_par_selection',
        help='Livré par',
        inverse='_inverse_project_type_id')

    @api.model
    def _get_livre_par_selection(self):
        livre_par_options = []

        chauffeur_partners = self.env['res.partner'].search([('est_un_chauffeur', '=', True)])

        for partner in chauffeur_partners:
            livre_par_options.append((str(partner.id), partner.name))

        return livre_par_options

    def _inverse_project_type_id(self):
        for picking in self:
            sale_order = self.env['sale.order'].search([('name', '=', picking.origin)], limit=1)
            if sale_order:
                sale_order.livre_par = picking.livre_par
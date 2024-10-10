from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    livry_par = fields.Selection(
        selection='_get_livre_par_selection',
        help='Livré par',)

    @api.model
    def _get_livre_par_selection(self):
        livre_par_options = []

        # Get partners marked as "est_un_chauffeur"
        chauffeur_partners = self.env['res.partner'].search([('est_un_chauffeur', '=', True)])

        # Add each chauffeur to the selection list
        for partner in chauffeur_partners:
            livre_par_options.append((str(partner.id), partner.name))
        return livre_par_options

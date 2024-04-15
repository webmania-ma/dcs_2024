from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    livry_par = fields.Char(string='Livré par' , required=True)

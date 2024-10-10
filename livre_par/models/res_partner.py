from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    est_un_chauffeur = fields.Boolean(string="Est un chauffeur")

from odoo import fields, models, api, _

class SaleOrderPaymentInherit(models.TransientModel):
    _inherit = "sale.order.payment"
    _description = "Sale Order Payment Inherit"

    cheq_num = fields.Char(string="Number")
    cheq_img = fields.Binary(string="Image")

    def payment_validate(self):
        # Call the parent method
        res = super(SaleOrderPaymentInherit, self).payment_validate()
        # Update the payment with the cheque details
        self.write({
            'cheq_num': self.cheq_num,
            'cheq_img': self.cheq_img,
        })
        return res

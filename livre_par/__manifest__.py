# -*- coding: utf-8 -*-
{
    'name': "Ajouter le champe livré par ",
    'description':
        """
        Ce module ajoute un champ 'Livré par' dans les documents Devis, Inventaires et Factures. 
        Ce champ permet de spécifier la personne responsable de la livraison des produits ou services mentionnés dans ces documents.
        De plus, cette information est également incluse dans les rapports (Devis , Bon de Livraison , Facture)
        """,
    'author': "WEBMANIA",
    'website': "https://www.webmania.ma",
    'category': 'Sales Management',
    'version': '0.1',
    'depends': ['base', 'sale', 'stock', 'account', 'eloapps_sale_order_payment'],
    'data': [
        'views/view_sale_order.xml',
        'views/view_stock_picking.xml',
        'views/view_account_move.xml',
        'views/view_res_partner.xml',
        'report/account_move_report.xml',
        'report/livre_par_sale_order.xml',
        'report/livre_par_stock_picking.xml',
        'report/bon_de_livraison_valo.xml',

    ],
}

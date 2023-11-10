# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management Systems',
    'version' : '1.0',
    'summary': 'Simplify your ',
    'sequence': 1,
    'description': "Hospital Management Systems",
    'category': 'Hospital',
    'website': 'https://shorturl.at/juBR0',
    'depends' : [],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patients.xml",
    ],
        
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}

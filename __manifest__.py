# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management Systems',
    'version' : '16.0.0.0',
    'summary': 'Simplify your ',
    'sequence': 1,
    'description': "Hospital Management Systems",
    'category': 'Hospital',
    'website': 'https://shorturl.at/juBR0',
    'depends' : ['mail'],
    'data': [
        "security/ir.model.access.csv",
        "data/patient_sequence.xml",
        "data/appointment_sequence.xml",
        "views/menu.xml",
        "views/patient_view.xml",
        "views/appointment_view.xml",
        
    ],
        
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}

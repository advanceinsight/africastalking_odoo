# -*- coding: utf-8 -*-
{
    'name':                     "Africa's Talking Odoo module",

    'summary':                  """Module to easily integrate Africa's Talking with odoo""",

    'description':              """This module enables you to integrate
                                Africa's Talking API in Odoo""",

    'author':                   "Douwe van Loenen / Advance Insight",
    'website':                  "http://www.advanceinsight.dev",

    'application':              False,

    'category':                 'Productivity',
    'version':                  '0.01',

    'depends':                  [
                                'base',
                                'contacts',
                                ],

    'data':                     [
                                'security/ir.model.access.csv',
                                'security/security.xml',
                                'views/Views.xml',
                                'views/Settings.xml',
                                ],
}

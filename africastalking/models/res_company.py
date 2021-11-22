# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
	_inherit = 'res.company'

	username = fields.Char(
		string="Username")

	api_key = fields.Char(
		string="API Key")

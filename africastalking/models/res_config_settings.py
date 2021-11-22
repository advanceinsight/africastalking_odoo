# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	username = fields.Char(
		related='company_id.username',
		string="Username",
		readonly=False)

	api_key = fields.Char(
		related='company_id.api_key',
		string="API Key",
		readonly=False)

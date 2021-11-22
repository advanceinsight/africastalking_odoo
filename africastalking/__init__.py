# -*- coding: utf-8 -*-

from . import controllers
from . import models
from odoo.exceptions import ValidationError, UserError

try:
	import africastalking
except:
	raise UserError(
		"The Africa's Talking python package is missing."\
		"Please first install the Africa's Talking python package on your"\
		"database. To install Africa's Talking python module, open a"\
		"shell/terminal and enter 'pip3 install africastalking'."
	)

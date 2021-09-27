# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests

class NaheSmsMasivosSaleOrder(models.Model):
	_inherit = 'sale.order'

	sms_listo_enviado = fields.Boolean(string='SMS LISTO ENVIADO')
	sms_cancelado_enviado = fields.Boolean(string='SMS CANCELADO ENVIADO')

	def action_sendsmslisto(self, default=None):
		API_URL = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_URL','')
		API_USER = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_USER','')
		API_PWD = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_PWD','')
		SMS_MESSAGE = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_MESSAGE_LISTO','')
		#EL SMS_MESSAGE_LISTO POR DEFECTO LO METO EN EL PARAMETRO VA A SER: "Hola, #CLIENTE su pedido #ORDEN esta listo para retirar. Total: #MONTO"
		#https://servicio.smsmasivos.com.ar/enviar_sms.asp?api=1&usuario=#API_USER&clave=#API_PWD&tos=#NUMERO&texto=#SMS_MESSAGE
		for rec in self:
			message = SMS_MESSAGE.replace('#CLIENTE',rec.partner_id.display_name)
			message = message.replace('#MONTO',str(round(rec.amount_total,0)))
			message = message.replace('#ORDEN',rec.name)
			result = ''
			num_cel = rec.partner_id.mobile
			if num_cel:
				num_cel = num_cel.replace('+54','')
				num_cel = num_cel.replace('+','')
				num_cel = num_cel.replace('-','')
				num_cel = num_cel.replace(' ','')
				if len(num_cel) == 10:
					datos = {'usuario': API_USER, 'clave': API_PWD, 'tos': num_cel, 'texto': message}
					if len(message) > 159:
						raise ValidationError('El mensaje tiene que ser de menos de 160 caracteres')
					else:
						req = requests.post('https://servicio.smsmasivos.com.ar/enviar_sms.asp?api=1', data=datos)
						raise ValidationError('El mensaje se envió correctamente (si no llegan revisar parametros del sistema valores de usuario y clave del servicio de smsmasivos)')
				else:
					raise ValidationError('Nro de telefono mal formateado %s'%(rec.partner_id.mobile))
			else:
				raise ValidationError('El cliente no tiene numero de celular agendado')
		return True

	def action_sendsmscancelado(self, default=None):
		API_URL = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_URL','')
		API_USER = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_USER','')
		API_PWD = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_API_PWD','')
		SMS_MESSAGE = self.env['ir.config_parameter'].get_param('nahe_smsmasivos.SMSMASIVOS_MESSAGE_CANCELADO','')
		#EL SMS_MESSAGE_LISTO POR DEFECTO LO METO EN EL PARAMETRO VA A SER: "Hola, #CLIENTE su pedido #ORDEN fue cancelada. Comuniquese con la empresa"
		#ESTA SERIA LA API URL GENERICA https://servicio.smsmasivos.com.ar/enviar_sms.asp?api=1&usuario=#API_USER&clave=#API_PWD&tos=#NUMERO&texto=#SMS_MESSAGE
		for rec in self:
			message = SMS_MESSAGE.replace('#CLIENTE',rec.partner_id.display_name)
			message = message.replace('#ORDEN',rec.name)
			result = ''
			num_cel = rec.partner_id.mobile
			if num_cel:
				num_cel = num_cel.replace('+54','')
				num_cel = num_cel.replace('+','')
				num_cel = num_cel.replace('-','')
				num_cel = num_cel.replace(' ','')
				if len(num_cel) == 10:
					datos = {'usuario': API_USER, 'clave': API_PWD, 'tos': num_cel, 'texto': message}
					if len(message) > 159:
						raise ValidationError('El mensaje tiene que ser de menos de 160 caracteres')
					else:
						req = requests.post('https://servicio.smsmasivos.com.ar/enviar_sms.asp?api=1', data=datos)
						raise ValidationError('El mensaje se envió correctamente (si no llegan revisar parametros del sistema valores de usuario y clave del servicio de smsmasivos)')
				else:
					raise ValidationError('Nro de telefono mal formateado %s'%(rec.partner_id.mobile))
			else:
				raise ValidationError('El cliente no tiene numero de celular agendado')
		return True


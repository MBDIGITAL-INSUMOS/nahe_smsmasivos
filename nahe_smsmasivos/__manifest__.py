# -*- coding: utf-8 -*-
{
    'name': "nahe_smsmasivos",

    'summary': """
        Ingegracion con smsmasivos.com.ar para enviar SMS desde los pedidos de ventas.""",

    'description': """
        El boton que se agrega es enviar SMS al cliente cuando este listo para retirar su pedido.
        En parametros de sistema es necesario ajustar los datos de usuario y clave del servicio de la API de smsmasivos.com.ar
        Se puede cambiar el mensaje siempre y cuando se respete los datos como #ORDEN #CLIENTE 
        Para mas customizaciones contactarse con Nähe Consulting Group
        TODO: lograr que la URL quede bien puesta desde el modulo tengo problemas con el '&' en las vistas
    """,

    'author': "Nähe Consulting Group",
    'website': "http://www.nahe.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '13.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

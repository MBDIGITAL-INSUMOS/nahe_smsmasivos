# nahe_smsmasivos
integra smsmasivos con odoo 13  y las sale.order
(testeado en odoo 13 pero debería andar en mas versiones)

Es necesario registrarse en el servicio de www.smsmasivos.com.ar De ahi obtener el usuario y contraseña para la API.
Se colocan los datos en Ajustes > Tecnico > parámetros del sistema
Cabe aclarar que tienen 25 mensajes gratis para testeo. 

Resumen del modulo de SMS: 
1º se puede enviar SMS haciendo click en el odoo en las ordenes de pedidos. 
2º Al cliente le llega el mensaje si esta bien anotado su numero 
3º si no esta bien anotado el numero se intenta "limpiar" y enviar. Si sigue mal no se manda y sale cartel de error.
4º si no tiene numero puesto en celular sale cartel de error.
5º cada SMS tiene un costo no es gratis pero vale la pena usarlos.

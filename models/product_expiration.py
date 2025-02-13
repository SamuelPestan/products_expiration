from datetime import timedelta
from odoo import models, fields, api

class ProductExpiration(models.Model):
    _name = 'product.expiration'
    _description = 'Registro de Expiración de Productos'

    product_id = fields.Many2one('product.product', string='Producto', required=True)
    expiration_date = fields.Date(string='Fecha de Expiración', required=True)
    quantity = fields.Float(string='Cantidad', required=True)
    notification_sent = fields.Boolean(string='Notificación Enviada', default=False)
    
    @api.model
    def create(self, vals):
        record = super(ProductExpiration, self).create(vals)
        record._check_expiration()
        return record

    def _check_expiration(self):
        """ Verifica si la fecha de expiración está próxima y envía una alerta. """
        for record in self:
            if record.expiration_date and not record.notification_sent:
                today = fields.Date.today()
                expiration_warning_date = today + timedelta(days=7)
                if record.expiration_date <= expiration_warning_date:
                    # Llamar a la función que envía la notificación
                    self._send_expiration_notification(record)

    def check_expiration_in_cron(self):
        """ Método llamado por el cron job para verificar expiraciones. """
        self._check_expiration()

    def _send_expiration_notification(self, record):
        """ Enviar notificación de expiración a los responsables. """
        # Aquí puedes enviar un correo o crear un mensaje interno
        record.notification_sent = True
        # Notificación por correo o recordatorio
        template = self.env.ref('mail.email_template_data_warning_product_expiry')
        template.send_mail(record.id, force_send=True)

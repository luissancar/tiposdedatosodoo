
from odoo import models, fields
from datetime import datetime

class Tdatos(models.Model):
    _name = 'tiposdatos.tdatos'

    def month_selection(self):
        return [(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril')]

    char = fields.Char('Char',size=20, required=True)
    texto = fields.Text('texto')
    boolean = fields.Boolean('boolean')
    html = fields.Html('html')
    float_field = fields.Float(digits=lambda cr: (32, 2))
    #parte entera, parte decimal
    date = fields.Date('date')
    datetime_field = fields.Datetime('datetime')
    fecha_actual = fields.Date(string='Fecha actual', default=lambda s: fields.Date.context_today(s))
    selection = fields.Selection(selection=month_selection, string='Mes',default=datetime.now().month, required=True)
    imagen = fields.Binary("Imagen",Help="Seleccionar Imagen")








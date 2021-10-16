from odoo import models,fields

class Calculator(models.Model):
    _name = 'mas_cal'
    
    status = fields.Selection(selection=[('borrador','Borrador'),('finalizado','Finalizado'),('en proceso','En Proceso')])
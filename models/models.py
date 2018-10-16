# -*- coding: utf-8 -*-

from odoo import models, fields, api


class city(models.Model):
    _name = 'papito.city'

    name = fields.Char()
    description = fields.Text()
    ubication = fields.Char(String="Ubication")
    country = fields.Many2one("res.country", "Pais")
    hotelList = fields.Many2one("papito.hotel","Hotel")

    class hotel(models.Model):
        _name = 'papito.hotel'
        name = fields.Char()
        galeriaFotos = fields.Char()
        description=fields.Text()
        listaHabitaciones=fields.Char()
        valoraciones=fields.Integer()
        listaServicios=fields.Char()

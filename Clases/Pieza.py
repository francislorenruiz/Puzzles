"""
Copyright 2020 Francisco Lorente Ruiz.
    This file is part of Puzzles.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>. 
"""


class Pieza:
	"""La clase Pieza se define por un diccionario que representa
	los 4 lados de una pieza de puzzle. Dos piezas pueden unirse si
	tienen el mismo número en alguno de sus lados."""
	lados = {}
	colocada = False
	pos_en_lista = 0

	def __init__(self, lado_sup, lado_der, lado_inf, lado_izq):
		self.lados = {
			'sup': lado_sup,
			'der': lado_der,
			'inf': lado_inf,
			'izq': lado_izq
		}

	def rotar_horario(self):
		aux = {
			'sup': self.lados['izq'],
			'der': self.lados['sup'],
			'inf': self.lados['der'],
			'izq': self.lados['inf']
		}
		self.lados = aux

	def rotar_antihorario(self):
		aux = {
			'sup': self.lados['der'],
			'der': self.lados['inf'],
			'inf': self.lados['izq'],
			'izq': self.lados['sup']
		}
		self.lados = aux

	def print(self):
		print(self.lados.values())

	def lados_en_cadena(self):
		cadena = str(self.lados['sup']) + ' ' + str(self.lados['der']) + ' ' + str(self.lados['inf']) + ' ' + str(self.lados['izq'])
		return cadena

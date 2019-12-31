"""
Copyright 2019 Francisco Lorente Ruiz.
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


from .Pieza import Pieza

class Hueco:
	"""Hueco se define por un diccionario de 4 elementos al igual que la clase
	Pieza. En cada hueco se puede encajar una pieza, siempre que los
	números de los lados de uno y otro coincidan.
	En el caso especial de que un lado del hueco valga -1 significa que 
	no hay información sobre ese lado y vale cualquier otro número; es
	decir que en ese lado no hay una pieza colocada."""

	lados = {}
	pieza_encajada = None
	
	def __init__(self, lado_sup, lado_der, lado_inf, lado_izq):
		self.lados = {
			'sup': lado_sup,
			'der': lado_der,
			'inf': lado_inf,
			'izq': lado_izq
		}

	def encajar_pieza(self, pieza):
		for i in range(4):
			for lado in self.lados:
				if self.lados[lado] != -1 and self.lados[lado] != pieza.lados[lado]:
					break
			else:
				pieza.colocada = True
				self.pieza_encajada = pieza
				self.lados = pieza.lados
				return True
			pieza.rotar_horario()
		else:
			return False

	def vaciar(self):
		pieza_encajada.colocada = False
		pieza_encajada = None

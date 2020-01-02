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
				self.lados = dict(pieza.lados)
				self.pieza_encajada = pieza
				return True
			pieza.rotar_horario()
		else:
			return False

	def vaciar(self):
		self.pieza_encajada.colocada = False
		self.pieza_encajada = None
		#Al vaciar un hueco los lados inferior y derecho ya no se conocen, pero
		#los otros aún sí, mientras no se quiten las piezas correspondientes.
		if self.lados['der'] != 0: #Sólo se cambia si no son el borde del puzzle
			self.lados['der'] = -1
		if self.lados['inf'] != 0:
			self.lados['inf'] = -1


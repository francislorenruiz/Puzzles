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
from .Hueco import Hueco

class Tablero:

	huecos = []
	piezas = []
	n_filas = int()
	n_columnas = int()

	def __init__(self, ancho, alto):
		self.huecos = [[Hueco(-1, -1, -1, -1)] * ancho] * alto
		self.n_filas = alto
		self.n_columnas = ancho
		for i in range(alto):
			self.huecos[i][0].lados['izq'] = 0
			self.huecos[i][ancho - 1].lados['der'] = 0
		for i in range(ancho):
			self.huecos[0][i].lados['sup'] = 0
			self.huecos[alto-1][i].lados['inf'] = 0


	def cargar_piezas(self, fichero):
		fichero = open(fichero,'r')
		
		for i in range(self.n_filas * self.n_columnas):
			texto = fichero.readline()
			lados = texto.split()
			self.piezas.append(Pieza(int(lados[0]), int(lados[1]), int(lados[2]), int(lados[3])))

		fichero.close()


	def resolver(self):
		pass


	def guardar_resultado(self, fichero):
		fichero = open(fichero,'w')
		
		for i in range(self.n_filas):
			for j in range(self.n_columnas):
				if self.huecos[i][j].pieza_encajada != None:
					fichero.write(self.huecos[i][j].pieza_encajada.lados_en_cadena() + '\n')
				else:
					fichero.write('0 0 0 0\n')

		fichero.close()

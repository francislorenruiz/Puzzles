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

from Clases.Tablero import Tablero

puzzle = Tablero(2, 2)
puzzle.cargar_piezas('Piezas.dat')
puzzle.resolver()
puzzle.guardar_resultado('Resultado.dat')

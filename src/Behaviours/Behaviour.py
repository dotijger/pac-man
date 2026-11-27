from abc import ABC, abstractmethod
from pydantic import BaseModel
from pygame import Vector2
import numpy as np

class Behaviour(ABC):
    coords: Vector2
    map: list[list[str]]

    def pathfinding(self, dest: Vector2) -> Vector2:
        direction: Vector2 = Vector2(0, 0)
        neighbours = self.get_accesible_neighbours(self.coords)
        
        return direction

    def get_accesible_neighbours(self, cell_coords: Vector2) -> list[Vector2]:
        neighbours: list[Vector2] = []
        cell_value = int(self.map[int(cell_coords.y)][int(cell_coords.x)], 16)
        if not cell_value >> 0 & 1:
            neighbours.append(Vector2(cell_coords.x, cell_coords.y - 1))
        if not cell_value >> 1 & 1:
            neighbours.append(Vector2(cell_coords.x + 1, cell_coords.y))
        if not cell_value >> 2 & 1:
            neighbours.append(Vector2(cell_coords.x, cell_coords.y + 1))
        if not cell_value >> 3 & 1:
            neighbours.append(Vector2(cell_coords.x - 1, cell_coords.y))
        return neighbours
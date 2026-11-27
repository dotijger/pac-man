from abc import ABC, abstractmethod
from typing import Any, Optional
from pydantic import BaseModel
from pygame import Vector2
import numpy as np


class Weighted_Cell(BaseModel):
    coords: Vector2
    weight: int = 0
    est_dist: float = 0
    parent: Optional['Weighted_Cell'] = None

class Behaviour(ABC):
    coords: Vector2
    map: list[list[str]]
    weighted_coords: list[str] = []
    mapped_coords: list[str] = []
    weighted_cells: dict[str, Weighted_Cell] = {}

    def pathfinding(self, dest: Vector2) -> Vector2:
        direction: Vector2 = Vector2(0, 0)

        origin = Weighted_Cell(coords=self.coords)
        self.mapped_coords.append(f"{self.coords.xy}")
        weighted_cells: dict[str, Weighted_Cell] = {}
        weighted_cells = self.get_accesible_neighbours(origin, dest)
        # for neighbour in neighbours:
        #     dis_to_dest = dest.distance_to(neighbour)
        #     dis_to_cur = 1
        #     weighted_cells.append(Weighted_Cell(
        #         coords=neighbour,
        #         weight=1,
        #         est_dist=dest.distance_to(neighbour),
        #         parent=origin
        #     ))
        while True:
            weighted_cells = sorted(weighted_cells.values(), key=lambda cell: cell.weight + cell.est_dist)
            cell = weighted_cells.pop(0)
            new_weighted_cells = self.get_accesible_neighbours(cell, dest)
            for new_cell in new_weighted_cells:
                if new_cell.coords:
                    pass
                    # check if we've been here before, don't forget three different types of node/cell
                    # unknown, weighted, mapped
            
        return direction

    def check_and_store_weighted_cell(self, cell: Weighted_Cell,
                                      dest: Vector2, coords: Vector2):
        coord_str = f"{coords.xy}"
        if not coord_str in self.mapped_coords:
            if coord_str in self.weighted_cells.keys():
                if self.weighted_cells[coord_str].weight <= cell.weight:
                    return
            self.weighted_cells[coord_str] = (Weighted_Cell(
                coords=coords,
                weight=cell.weight + 1,
                est_dist=dest.distance_to(coords),
                parent=cell
                ))
            

    def get_accesible_neighbours(self, cell: Weighted_Cell, dest: Vector2) -> dict[str, Weighted_Cell]:
        neighbours: dict[str, Weighted_Cell] = []
        cell_coords = cell.coords
        cell_value = int(self.map[int(cell_coords.y)][int(cell_coords.x)], 16)
        if not cell_value >> 0 & 1:
            new_coords = Vector2(cell_coords.x, cell_coords.y - 1)
            self.check_and_store_weighted_cell(cell, dest, new_coords)
        if not cell_value >> 1 & 1:
            new_coords = Vector2(cell_coords.x + 1, cell_coords.y)
            self.check_and_store_weighted_cell(cell, dest, new_coords)
        if not cell_value >> 2 & 1:
            new_coords = Vector2(cell_coords.x, cell_coords.y + 1)
            self.check_and_store_weighted_cell(cell, dest, new_coords)
        if not cell_value >> 3 & 1:
            new_coords = Vector2(cell_coords.x - 1, cell_coords.y)
            self.check_and_store_weighted_cell(cell, dest, new_coords)
        return neighbours

    # def get_accesible_neighbours(self, cell_coords: Vector2) -> list[Vector2]:
    #     neighbours: list[Vector2] = []
    #     cell_value = int(self.map[int(cell_coords.y)][int(cell_coords.x)], 16)
    #     if not cell_value >> 0 & 1:
    #         neighbours.append(Vector2(cell_coords.x, cell_coords.y - 1))
    #     if not cell_value >> 1 & 1:
    #         neighbours.append(Vector2(cell_coords.x + 1, cell_coords.y))
    #     if not cell_value >> 2 & 1:
    #         neighbours.append(Vector2(cell_coords.x, cell_coords.y + 1))
    #     if not cell_value >> 3 & 1:
    #         neighbours.append(Vector2(cell_coords.x - 1, cell_coords.y))
    #     return neighbours
from typing import Any, Optional

import pygame
import pygame.math as math
import pygame.image as image
import pygame.surface as surface
import pygame.sprite as sprite
from pygame import Surface, sprite, Rect
import numpy as np
from pydantic import BaseModel
from abc import ABC, abstractmethod

HEIGHT = 640
WIDTH = 480
SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)


class Behaviour(ABC):
    pass


class Entity(sprite.Sprite, ABC):
    coords: math.Vector2
    images: list[Surface] = []
    containers: sprite.AbstractGroup[Any]

    def __init__(self, coords: math.Vector2) -> None:
        sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.coords = coords

    @abstractmethod
    def update(self, *args: Any, **kwargs: Any) -> None:
        return super().update(*args, **kwargs)

    @abstractmethod
    def collision(self, other: Entity) -> None:
        pass


class Moveable_Entity(Entity):
    coords: math.Vector2
    speed: float
    images_dict: dict[str, Surface]
    behaviour: Optional[Behaviour]
    rect: pygame.Rect

    def __init__(self, coords: pygame.Vector2) -> None:
        super().__init__(coords)
        if len(self.images) > 0:
            self.images_dict["neutral"] = self.images[0]
            self.images_dict["left"] = self.images[0]
            self.images_dict["right"] = self.images[1]
            self.images_dict["up"] = self.images[2]
            self.images_dict["down"] = self.images[3]
            

    def move(self, direction: math.Vector2):
        if direction:
            self.facing = self.coords - direction
            self.facing = self.facing.normalize()
        self.rect.move_ip(self.facing.x * self.speed,
                          self.facing.y * self.speed)
        self.rect = self.rect.clamp(SCREENRECT)
        if self.facing.x < 0:
            self.image = self.images_dict["left"]
        elif self.facing.x > 0:
            self.image = self.images_dict["right"]
        elif self.facing.y < 0:
            self.image = self.images_dict["up"]
        elif self.facing.y > 0:
            self.image = self.images_dict["down"]

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.behaviour:
            # do behaviour things
            pass
        return super().update(*args, **kwargs)

    def collision(self, other: Entity) -> None:
        # maybe here, maybe elsewhere
        pass


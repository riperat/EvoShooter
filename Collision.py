import math

import pygame


class Collision:
    def border_colission_check(entity):
        if entity.X >= 760:
            entity.X = 760
        if entity.X <= 0:
            entity.X = 0
        if entity.Y >= 760:
            entity.Y = 760
        if entity.Y <= 0:
            entity.Y = 0

    def bullet_hit_check(entity, bullet):
        distance = math.sqrt(math.pow(entity.X - bullet.X, 2) + math.pow(entity.Y - bullet.Y, 2))
        if distance < 30:
            return True
        else:
            return False

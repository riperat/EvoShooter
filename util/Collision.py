import math

import pygame


class Collision:
    def border_colission_check(entity, XBorder, YBorder):
        if XBorder:
            if entity.X >= 760:
                entity.X = 760
            if entity.X <= 0:
                entity.X = 0
        if YBorder:
            if entity.Y >= 760:
                entity.Y = 760
            if entity.Y <= 0:
                entity.Y = 0

    def bullet_hit_check(entity, projectile):
        try:
            if entity.body.colliderect(projectile.body):
                return True
            else:
                return False
        except:
             return False

    def player_hit_check(entity, player):
        circle_bounding_rect = pygame.Rect(entity.X - entity.sizeX, entity.Y - entity.sizeX,
                                           entity.sizeX * 2, entity.sizeX * 2)

        if player.body.colliderect(circle_bounding_rect):
            return True
        else:
            return False

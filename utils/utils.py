import random

from database import *


def getDistance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def isPositionLegal(x, y):
    """
    Check if the position is legal.
    :param x: x relative position
    :param y: y relative position
    :return: True if legal, False if illegal
    """
    # TODO: Judge it with canves xy, input app
    if 0 <= x < MAP_BLOCKS and 0 <= y < MAP_BLOCKS:
        return True
    return False


def roll_a_zombie(app):
    """
    Choose a random zombie according to their appear rate.
    :param app: Current app object
    :return: x and y positions but a distance away from player, direction, and type of the zombie
    """
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    while getDistance(app.player.x, app.player.y, x, y) < ZOMBIE_LEGAL_DIS:
        x = random.randint(0, 99)
        y = random.randint(0, 99)

    direction = DIRECTIONS[DIRECTIONS_LIST[random.randint(0, 3)]]

    num = random.randint(1, 10000)
    z_type = Z_TYPE_LIST[-1]
    for z in Z_TYPE_LIST:
        num -= Z_TYPE[z][-1] * 100
        if num <= 0:
            z_type = z
            break
    return x, y, direction, z_type

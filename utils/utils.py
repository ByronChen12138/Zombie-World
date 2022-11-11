import random

from database import *


def getDistance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def getCXY(app, x, y):
    """
    Get the (cx, cy) on the canvas (map) according to relative x, y
    :param app: Current app object
    :param x: Relative x
    :param y: Relative y
    :return: Tuple of the (cx,cy) on the canvas
    """
    # Variables needed to be updated
    map_size = min(app.width, app.height) - 100
    map_start_x = (app.width - map_size) / 2
    map_start_y = app.height - map_size - 10
    cell_size = map_size / app.map_blocks

    cx = map_start_x + x * cell_size
    cy = map_start_y + y * cell_size

    return cx, cy


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

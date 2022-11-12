import copy
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
    # TODO: Judge it with canves xy, input app?
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
        # TODO: Possible Error if Z_TYPE changed
        num -= Z_TYPE[z][-2] * 100
        if num <= 0:
            z_type = z
            break
    return x, y, direction, z_type


def roll_a_gun(app):
    """
    Choose a random gun according to their appear rate.
    :param app: Current app object
    :return: x and y positions but a distance away from player, and type of the zombie
    """
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    while getDistance(app.player.x, app.player.y, x, y) < GUN_LEGAL_DIS:
        x = random.randint(0, 99)
        y = random.randint(0, 99)

    num = random.randint(1, 10000)
    g_type = G_TYPE_LIST[-1]
    for g in G_TYPE_LIST:
        # TODO: Possible Error if G_TYPE changed
        num -= G_TYPE[g][-1] * 100
        if num <= 0:
            g_type = g
            break
    return x, y, g_type


def isCircleTouch(app, cell_size, obj1, obj2):
    """
    Check if two circle is in touch in the canvas
    :param app: Current app object
    :param cell_size: The cell size of the map
    :param obj1: the first obj to check
    :param obj2: the second obj to check
    :return: True if in touch; otherwise, False
    """
    threshold = (obj1.size + obj2.size) * cell_size / 2

    x, y = obj1.getPosition()
    cx1, cy1 = getCXY(app, x, y)

    x, y = obj2.getPosition()
    cx2, cy2 = getCXY(app, x, y)

    if getDistance(cx1, cy1, cx2, cy2) <= threshold:
        return True
    return False


def doAttacksToPlayer(app):
    """
    Do possible attack to player
    :param app: Current app object
    :return: If any attack, return True; else False
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    is_attacked = False

    for zombie in app.zombies:
        if isCircleTouch(app, cell_size, zombie, app.player):
            zombie.attack(app.player)
            is_attacked = True

    return is_attacked


def doAttacksToZombies(app):
    """
    Do possible attack to zombies
    :param app: Current app object
    :return: If any attack, return True; else False
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    is_attacked = False

    for zombie in app.zombies:
        for bullet in copy.copy(app.player.bullets):
            if isCircleTouch(app, cell_size, zombie, bullet):
                bullet.attack(zombie)
                app.player.bullets.remove(bullet)
                is_attacked = True

    return is_attacked


def doTimeUpd(app):
    """
    Do all the time upd
    :param app: Current app object
    :return: If any attack, return True; else False
    """

    app.player.invincible_time -= 1
    app.player.shoot_time -= 1

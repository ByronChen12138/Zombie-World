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


def isCirclePositionLegal(app, x, y, size):
    """
    Check if the position of the circle is legal, which is inside the map.
    :param app: Current app obj
    :param x: x relative position
    :param y: y relative position
    :param size: The size of the current circle
    :return: True if legal, False if illegal
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    map_start_x = (app.width - map_size) / 2
    map_start_y = app.height - map_size - 10
    map_end_x = map_start_x + map_size
    map_end_y = map_start_y + map_size
    drawing_size = size * cell_size / 2
    cx, cy = getCXY(app, x, y)

    if map_start_x <= cx - drawing_size and \
            cx + drawing_size <= map_end_x and \
            map_start_y <= cy - drawing_size and \
            cy + drawing_size <= map_end_y and \
            not app.map.anyBarrier(x, y, size):
        return True
    return False


def roll_a_zombie(app):
    """
    Choose a random zombie according to their appear rate.
    :param app: Current app object
    :return: x and y positions but a distance away from player, direction, and type of the zombie
    """
    direction = DIRECTIONS[DIRECTIONS_LIST[random.randint(0, 3)]]

    num = random.randint(1, 10000)
    z_type = Z_TYPE_LIST[-1]
    for z in Z_TYPE_LIST:
        # TODO: Possible Error if Z_TYPE changed
        num -= Z_TYPE[z][-2] * 100
        if num <= 0:
            z_type = z
            break

    x = random.randint(0, 99)
    y = random.randint(0, 99)
    while getDistance(app.player.x, app.player.y, x, y) < ZOMBIE_LEGAL_DIS or \
            not isCirclePositionLegal(app, x, y, Z_TYPE[z_type][0]):
        x = random.randint(0, 99)
        y = random.randint(0, 99)

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


def isTouch(app, cell_size, obj1, obj2):
    """
    Check if two objects are in touch in the canvas
    :param app: Current app object
    :param cell_size: The cell size of the map
    :param obj1: the first obj to check
    :param obj2: the second obj to check (have to be circle)
    :return: True if in touch; otherwise, False
    """
    threshold = 0

    if obj1.shape == "Circle":
        threshold = (obj1.size + obj2.size) * cell_size / 2
    elif obj1.shape == "Gun":
        threshold = (3 + obj2.size) * cell_size / 2

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
        if isTouch(app, cell_size, zombie, app.player):
            zombie.attack(app.player)
            is_attacked = True

    return is_attacked


def doAttacksToZombies(app):
    """
    Do possible attack to zombies with bullets and delete bullet used
    :param app: Current app object
    :return: If any attack, return True; else False
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    is_attacked = False

    for zombie in app.zombies:
        for bullet in copy.copy(app.player.bullets):
            if isTouch(app, cell_size, zombie, bullet):
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
    app.player.move_time -= 1
    for z in app.zombies:
        z.move_time -= 1
    app.gun_time -= 1


def pickGun(app):
    """
    Check all the guns to pickup and do it
    :param app: Current app obj
    :return: If any pickup, return True; else False
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    is_picked = False

    for g in copy.copy(app.guns):
        if isTouch(app, cell_size, g, app.player):
            app.player.pickUpAGun(g)
            app.guns.remove(g)
            is_picked = True

    return is_picked

import copy
import random

from database import *


def getDistance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def getCXY(app, x, y):
    """
    Get the (cx, cy) on the Canvas according to relative x, y
    :param app: Current app object
    :param x: Relative x
    :param y: Relative y
    :return: Tuple of the (cx,cy) on the canvas
    """
    cell_width = app.width / 100
    cell_height = app.height / 100
    return x * cell_width, (100 - y) * cell_height


def getMapCXY(app, x, y):
    """
    Get the (cx, cy) on the MAP according to relative x, y
    :param app: Current app object
    :param x: Relative x
    :param y: Relative y
    :return: Tuple of the (cx,cy) on the canvas
    """
    # Variables needed to be updated
    map_size = min(app.width, app.height) - 100
    map_start_x = (app.width - map_size) / 2
    map_start_y = app.height - map_size - 10
    cell_size = map_size / app.blocks_to_draw

    cx = map_start_x + (x - app.x_offset) * cell_size
    cy = map_start_y + (y - app.y_offset) * cell_size

    return cx, cy


def isCirclePositionLegal(app, x, y, size):
    """
    Check if the position of the circle is legal, which is inside the map.
    :param app: Current app obj
    :param x: x relative position
    :param y: y relative position
    :param size: The size of the current circle
    :return: (True, None) if legal, (False, barrier) if illegal; barrier is the one on the way
    """
    barrier = app.map.anyBarrier(x, y, size)

    if 0 < x - size // 2 and \
            x + size // 2 < MAP_BLOCKS and \
            0 < y - size // 2 and \
            y + size // 2 < MAP_BLOCKS and \
            barrier is None:
        return True, None
    return False, barrier


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

    size = Z_TYPE[z_type][0]
    mini, maxi = 0 + size // 2, MAP_BLOCKS - 1 - size // 2

    x = random.randint(mini, maxi)
    y = random.randint(mini, maxi)
    while getDistance(app.player.x, app.player.y, x, y) < ZOMBIE_LEGAL_DIS or \
            not isCirclePositionLegal(app, x, y, size)[0]:
        x = random.randint(mini, maxi)
        y = random.randint(mini, maxi)

    return x, y, direction, z_type


def roll_a_gun(app):
    """
    Choose a random gun according to their appear rate.
    :param app: Current app object
    :return: x and y positions but a distance away from player, and type of the zombie
    """
    x = random.randint(0, MAP_BLOCKS - 1)
    y = random.randint(0, MAP_BLOCKS - 1)
    while getDistance(app.player.x, app.player.y, x, y) < GUN_LEGAL_DIS:
        x = random.randint(0, MAP_BLOCKS - 1)
        y = random.randint(0, MAP_BLOCKS - 1)

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
    cx1, cy1 = getMapCXY(app, x, y)

    x, y = obj2.getPosition()
    cx2, cy2 = getMapCXY(app, x, y)

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
    cell_size = map_size / app.blocks_to_draw
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
    cell_size = map_size / app.blocks_to_draw
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
    for b in copy.copy(app.player.bullets):
        b.dece_time -= 1
        if b.dece_time <= 0:
            b.dece_time = 10
            b.deceleration()
            if b.speed <= 0:
                app.player.bullets.remove(b)


def pickGun(app):
    """
    Check all the guns to pickup and do it
    :param app: Current app obj
    :return: If any pickup, return True; else False
    """
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.blocks_to_draw
    is_picked = False

    for g in copy.copy(app.guns):
        if isTouch(app, cell_size, g, app.player):
            app.player.pickUpAGun(g)
            app.guns.remove(g)
            is_picked = True

    return is_picked


def doScroll(app):
    # Scroll Left
    if app.x_offset >= app.player.x - SCROLL_RANGE:
        app.x_offset = max(0, app.x_offset - SCROLL_PIX)

    # Scroll Right
    elif app.x_offset + BLOCKS_TO_DRAW <= app.player.x + SCROLL_RANGE:
        app.x_offset = min(app.x_offset + SCROLL_PIX, MAP_BLOCKS // 2)

    # Scroll Down
    if app.y_offset >= app.player.y - SCROLL_RANGE:
        app.y_offset = max(0, app.y_offset - SCROLL_PIX)

    # Scroll Up
    elif app.y_offset + BLOCKS_TO_DRAW <= app.player.y + SCROLL_RANGE:
        app.y_offset = min(app.y_offset + SCROLL_PIX, MAP_BLOCKS // 2)

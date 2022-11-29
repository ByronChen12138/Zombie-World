from models.Map import Map
from models.Player import Player
from models.Zombie import Zombie
from utils.utils import *


def appStarted(app):
    """
    Model for the app
    :param app: Current app object
    :return: None
    """
    # app.timerDelay = 1
    app.is_game_over = False
    app.score = 0
    app.zombie_num = ZOMBIE_NUM
    app.gun_time = 50
    app.map_blocks = MAP_BLOCKS
    app.blocks_to_draw = BLOCKS_TO_DRAW
    app.player = Player()
    app.map = Map(400, 400, 10, app.player)
    app.UI = "Menu"
    app.page_set = False
    app.buttons = set()
    app.pause = False

    app.x_offset = 50
    app.y_offset = 50

    # Must have some speed zombies
    app.speed_num = SPEED_NUM
    for i in range(app.speed_num):
        app.zombies = set()
        x, y, direction, z_type = roll_a_zombie(app)
        app.zombies.add(Zombie(x, y, direction, "Speed"))

    for i in range(app.zombie_num - 1):
        x, y, direction, z_type = roll_a_zombie(app)
        new_zombie = Zombie(x, y, direction, z_type)
        app.zombies.add(new_zombie)
        app.map.createAnObj(new_zombie)

    app.guns = set()





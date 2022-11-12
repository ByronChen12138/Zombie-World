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
    app.zombie_num = 10
    app.gun_time = 50
    app.map_blocks = MAP_BLOCKS
    app.player = Player()
    app.zombies = set()
    for i in range(app.zombie_num):
        x, y, direction, z_type = roll_a_zombie(app)
        app.zombies.add(Zombie(x, y, direction, z_type))

    app.guns = set()

    app.map = [[None for _ in range(MAP_BLOCKS)] for _ in range(MAP_BLOCKS)]

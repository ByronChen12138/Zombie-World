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
    app.map_blocks = MAP_BLOCKS
    app.player = Player()
    app.zombies = set()
    for i in range(ZOMBIE_NUM):
        x, y, direction, z_type = roll_a_zombie(app)
        app.zombies.add(Zombie(x, y, direction, z_type))


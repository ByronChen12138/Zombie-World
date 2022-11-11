from utils.cmu_112_graphics import *
from utils.utils import *


def mousePressed(app, event):
    """
    Activate when the mouse is click on the canvas when running the app.
    :param app: Current app object
    :param event: Current event object
    :return: None
    """
    pass


def keyPressed(app, event):
    """
    Activate when any key is pressed when running the app
    :param app: Current app object
    :param event: Current event object
    :return: None
    """
    if event.key == "Up":
        app.player.direction = DIRECTIONS["Up"]
        app.player.move()

    elif event.key == "Down":
        app.player.direction = DIRECTIONS["Down"]
        app.player.move()

    elif event.key == "Left":
        app.player.direction = DIRECTIONS["Left"]
        app.player.move()

    elif event.key == "Right":
        app.player.direction = DIRECTIONS["Right"]
        app.player.move()


def timerFired(app):
    """
    Activate when the timer set is fired when running the app
    :param app: Current app object
    :return: None
    """
    # 10 unit time of invincible time once the player is attacked
    if app.player.invincible_time <= 0:
        if doAttacksToPlayer(app):
            app.player.invincible_time = 10
    else:
        app.player.invincible_time -= 1

    # Check if player is died
    if app.player.isDied():
        app.is_game_over = True

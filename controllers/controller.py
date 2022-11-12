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

    if event.key == "Down":
        app.player.direction = DIRECTIONS["Down"]
        app.player.move()

    if event.key == "Left":
        app.player.direction = DIRECTIONS["Left"]
        app.player.move()

    if event.key == "Right":
        app.player.direction = DIRECTIONS["Right"]
        app.player.move()

    if event.key == "Space" and app.player.shoot_time <= 0:
        app.player.shoot()

    if event.key == "1":
        app.player.swapGun("Pistol")

    if event.key == "2":
        app.player.swapGun("Submachine")

    if event.key == "3":
        app.player.swapGun("Sniper")


def timerFired(app):
    """
    Activate when the timer set is fired when running the app
    :param app: Current app object
    :return: None
    """
    # 10 unit time of invincible time once the player is attacked
    if app.player.invincible_time <= 0:
        if doAttacksToPlayer(app):
            app.player.invincible_time = INVINCIBLE_TIME

    # Update all the cold time
    doTimeUpd(app)

    # Bullet hit zombie
    doAttacksToZombies(app)

    # Bullet move
    for b in app.player.bullets:
        b.move()

    # Check if Zombie is died
    for z in copy.copy(app.zombies):
        if z.getHP() <= 0:
            app.score += z.getScore()
            app.zombies.remove(z)

    # Check if player is died
    if app.player.isDied():
        app.is_game_over = True

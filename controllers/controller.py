from models.Gun import Gun
from models.Zombie import Zombie
from utils.cmu_112_graphics import *
from utils.utils import *


# TODO: All the Random obj should check the barrier


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
        if app.player.move_time <= 0:
            app.player.move(app)

    if event.key == "Down":
        app.player.direction = DIRECTIONS["Down"]
        if app.player.move_time <= 0:
            app.player.move(app)

    if event.key == "Left":
        app.player.direction = DIRECTIONS["Left"]
        if app.player.move_time <= 0:
            app.player.move(app)

    if event.key == "Right":
        app.player.direction = DIRECTIONS["Right"]
        if app.player.move_time <= 0:
            app.player.move(app)

    if event.key == "Space" and app.player.shoot_time <= 0:
        app.player.shoot()

    if event.key == "1":
        app.player.swapGun("Pistol")

    if event.key == "2":
        app.player.swapGun("Submachine")

    if event.key == "3":
        app.player.swapGun("Sniper")

    if event.key == "Enter":
        print(app.map)


def timerFired(app):
    """
    Activate when the timer set is fired when running the app
    :param app: Current app object
    :return: None
    """
    # Update difficulty
    if 100 < app.score <= 300:
        app.zombie_num = 20
    elif 300 < app.score:
        app.zombie_num = 30

    # 10 unit time of invincible time once the player is attacked
    if app.player.invincible_time <= 0:
        if doAttacksToPlayer(app):
            app.player.invincible_time = INVINCIBLE_TIME
            app.player.color = "#DB1EF1"
        else:
            app.player.color = "black"

    # Update new gun if can
    if app.gun_time <= 0 and len(app.guns) < 5:
        x, y, g_type = roll_a_gun(app)
        app.guns.add(Gun(x, y, g_type))
        app.gun_time = 50
    else:
        # If no new gun check gun pickup
        pickGun(app)

    # Update new zombie if needed
    while len(app.zombies) < app.zombie_num:
        x, y, direction, z_type = roll_a_zombie(app)
        app.zombies.add(Zombie(x, y, direction, z_type))

    # Update all the cold time
    doTimeUpd(app)

    # Bullet hit zombie
    doAttacksToZombies(app)

    # Zombie move
    for z in app.zombies:
        if z.move_time <= 0:
            z.move(app)

    # Bullet hit zombie
    doAttacksToZombies(app)

    # Bullet move
    for b in copy.copy(app.player.bullets):
        if not b.move(app):
            app.player.bullets.remove(b)

    # Check if Zombie is died
    for z in copy.copy(app.zombies):
        if z.getHP() <= 0:
            app.score += z.getScore()
            app.zombies.remove(z)

    # Check if player is died
    if app.player.isDied():
        app.is_game_over = True

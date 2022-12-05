from models.Gun import Gun
from models.MyButton import MyButton
from models.Zombie import Zombie
from models.app import appStarted
from utils.utils import *


def mousePressed(app, event):
    """
    Activate when the mouse is click on the canvas when running the app.
    :param app: Current app object
    :param event: Current event object
    :return: None
    """
    for b in app.buttons:
        if b.isClick(event.x, event.y):
            if b.text == "Start":
                app.SOUND_BUTTON_ENTER.start()
                app.page_set = False
                app.UI = "Game"
                app.MUSIC_STARTING.stop()

            elif b.text == "Help":
                app.SOUND_BUTTON_ENTER.start()
                app.page_set = False
                app.UI = "Help"

            elif b.text == "Back":
                app.SOUND_BUTTON_QUIT.start()
                app.page_set = False
                app.UI = "Menu"

            elif b.text == "Quit":
                app.SOUND_BUTTON_QUIT.start()
                app.page_set = False
                app.UI = "Menu"
                app.MUSIC_STARTING.start(-1)
                appStarted(app)


# def keyReleased(app, event):
#     """
#     Activate when any key is released when running the app
#     :param app: Current app object
#     :param event: Current event object
#     :return: None
#     """
#     if app.UI == "Game" and event.key == "Space":
#         if app.player.curr_gun == "Submachine":
#             app.MUSIC_SUB.stop()


def keyPressed(app, event):
    """
    Activate when any key is pressed when running the app
    :param app: Current app object
    :param event: Current event object
    :return: None
    """
    if app.pause:
        app.buttons = set()
        app.pause = False
        return

    if app.UI == "Game":
        # Pause
        if event.key == "Escape":
            app.pause = True
            app.buttons.add(MyButton(app, 50, 50, 4, "#969285", "Quit"))
            return

        # The move of the player
        if event.key == "Up" or event.key == "w" or event.key == "W":
            app.player.direction = DIRECTIONS["Up"]
            if event.key != "Up" and app.player.move_time <= 0:
                app.player.move(app)

        elif event.key == "Down" or event.key == "s" or event.key == "S":
            app.player.direction = DIRECTIONS["Down"]
            if event.key != "Down" and app.player.move_time <= 0:
                app.player.move(app)

        elif event.key == "Left" or event.key == "a" or event.key == "A":
            app.player.direction = DIRECTIONS["Left"]
            if event.key != "Left" and app.player.move_time <= 0:
                app.player.move(app)

        elif event.key == "Right" or event.key == "d" or event.key == "D":
            app.player.direction = DIRECTIONS["Right"]
            if event.key != "Right" and app.player.move_time <= 0:
                app.player.move(app)

        # Shoot of the player
        if event.key == "Space" and app.player.shoot_time <= 0:
            app.player.shoot(app)

        # Swap gun of the player
        if event.key == "1":
            app.player.swapGun("Pistol")

        if event.key == "2":
            app.player.swapGun("Submachine")

        if event.key == "3":
            app.player.swapGun("Sniper")

        # Get the info for debugging
        if event.key == "Enter":
            print(app.map)

        # Put the box and OD (Oil Drum)
        if event.key == "e" or event.key == "E":
            app.player.putBarrier(app, "Box")

        if event.key == "q" or event.key == "Q":
            app.player.putBarrier(app, "OD")


def timerFired(app):
    """
    Activate when the timer set is fired when running the app
    :param app: Current app object
    :return: None
    """
    if app.UI == "Menu":
        if not app.page_set:
            app.buttons = set()
            app.buttons.add(MyButton(app, 50, 50, 4, "#E2D9B8", "Start"))
            app.buttons.add(MyButton(app, 50, 35, 4, "#E2D9B8", "Help"))
            app.page_set = True

    if app.UI == "Help":
        if not app.page_set:
            app.buttons = set()
            app.buttons.add(MyButton(app, 95, 95, 4, "#E2D9B8", "Back"))
            app.page_set = True

    elif app.UI == "Game" and not app.pause:
        # Clear the buttons
        if not app.page_set:
            app.buttons = set()
            app.page_set = True

        # Update difficulty
        if 100 < app.score <= 300:
            app.zombie_num = 30
        elif 300 < app.score:
            app.zombie_num = 40

        # doScroll
        doScroll(app)

        # Update new gun if can
        if app.gun_time <= 0 and len(app.guns) < GUN_NUM:
            x, y, g_type = roll_a_gun(app)
            app.guns.add(Gun(x, y, g_type))
            app.gun_time = 50
        else:
            # If no new gun check gun pickup
            pickGun(app)

        # Update new zombie if needed
        while len(app.zombies) < app.zombie_num:
            x, y, direction, z_type = roll_a_zombie(app)
            while app.speed_num < SPEED_NUM:
                app.speed_num += 1
                z_type = "Speed"
                app.zombies.add(Zombie(x, y, direction, z_type))
                x, y, direction, z_type = roll_a_zombie(app)
            app.zombies.add(Zombie(x, y, direction, z_type))

        # Update all the cold time
        doTimeUpd(app)

        # Reset invincible time once the player is attacked
        if app.player.invincible_time <= 0:
            if doAttacksToPlayer(app):
                playerHurtSound(app)
                app.player.invincible_time = INVINCIBLE_TIME
                app.player.color = "#DB1EF1"
            else:
                app.player.color = "black"

        # Check if player is died
        if app.player.isDied():
            app.UI = "Over"
            app.is_game_over = True
            app.buttons = set()
            app.buttons.add(MyButton(app, 90, 90, 4, "#969285", "Quit"))
            app.page_set = True
            app.MUSIC_ENDING.start()
            return

        # Bullet hit zombie
        doAttacksToZombies(app)

        # Check if Zombie is died
        for z in copy.copy(app.zombies):
            if z.getHP() <= 0:
                app.score += z.getScore()
                if z.z_type == "Speed":
                    app.speed_num -= 1
                app.zombies.remove(z)
                if not app.SOUND_ZOMBIE_HURT.isPlaying():
                    app.SOUND_ZOMBIE_HURT.start()

        # Zombie move
        for z in app.zombies:
            if z.move_time <= 0:
                z.move(app)

        # Bullet move
        for b in copy.copy(app.player.bullets):
            if not b.move(app):
                app.player.bullets.remove(b)

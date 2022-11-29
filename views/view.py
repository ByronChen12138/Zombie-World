from models.Barrier import Barrier
from utils.cmu_112_graphics import *
from utils.utils import *

from models.app import *
from controllers.controller import *


def redrawAll(app, canvas):
    """
    Draw all the things on the canvas
    :param app: Current app object
    :param canvas: Current canvas object
    :return: None
    """

    if app.UI == "Menu":
        cx, cy = getCXY(app, 50, 80)
        canvas.create_rectangle(0, 0, app.width,app.height, fill='#E2D9B8')
        canvas.create_text(cx, cy, text="ZOMBIE WORLD",
                           fill='black', font='Helvetica 25 bold')
        for b in app.buttons:
            b.draw(app, canvas)

    elif app.UI == "Game":
        # Variables needed to be updated
        map_size = min(app.width, app.height) - 100
        cell_size = map_size / app.blocks_to_draw
        map_start_x = (app.width - map_size) / 2
        map_start_y = app.height - map_size - 10

        # Draw Map
        canvas.create_rectangle(map_start_x, map_start_y, map_start_x + map_size, map_start_y + map_size,
                                width=6, fill='#C9A946')
        for i in range(app.x_offset, app.x_offset + app.blocks_to_draw):
            for j in range(app.y_offset, app.y_offset + app.blocks_to_draw):
                curr_block = app.map.getMap()[j][i]
                if isinstance(curr_block, Barrier):
                    cx, cy = getMapCXY(app, i, j)
                    canvas.create_rectangle(cx - cell_size / 2, cy - cell_size / 2,
                                            cx + cell_size / 2, cy + cell_size / 2,
                                            width=1, fill=B_TYPE[curr_block.getBType()][-1])

        # Draw Guns
        for g in app.guns:
            g.drawObject(app, canvas, cell_size)

        # Draw Player
        app.player.drawObject(app, canvas, cell_size)

        # Draw Bullets
        for b in app.player.bullets:
            b.drawObject(app, canvas, cell_size)

        # Draw Zombies
        for z in app.zombies:
            z.drawObject(app, canvas, cell_size)

        # Draw Background
        canvas.create_rectangle(0, 0, app.width, map_start_y, fill='#E2D9B8', outline='black')
        canvas.create_rectangle(0, map_start_y + map_size, app.width, app.height, fill='#E2D9B8', outline='black')

        canvas.create_rectangle(0, 0, map_start_x, app.height, fill='#969285', outline='black')
        canvas.create_rectangle(map_start_x + map_size, 0, app.width, app.height, fill='#969285', outline='black')

        canvas.create_rectangle(map_start_x, map_start_y, map_start_x + map_size, map_start_y + map_size,
                                width=6, fill=None)

        # Show the HP
        cx, cy = getCXY(app, 30, 94)
        canvas.create_text(cx, cy, text=f"HP: {app.player.getHP()}",
                           fill='black', font='Helvetica 15 bold')

        # Show the Score
        cx, cy = getCXY(app, 42, 94)
        canvas.create_text(cx, cy, text=f"Score: {app.score}",
                           fill='black', font='Helvetica 15 bold')

        # Show the Ammo
        cx, cy = getCXY(app, 70, 94)
        canvas.create_text(cx, cy, text=f"{app.player.curr_gun}: {app.player.curr_ammo}",
                           fill='black', font='Helvetica 15 bold')

        # Show the Boxes
        cx, cy = getCXY(app, 57, 96)
        canvas.create_text(cx, cy, text=f'Boxes: {app.player.barriers["Box"]}',
                           fill='black', font='Helvetica 15 bold')

        # Show the ODs
        cx, cy = getCXY(app, 57, 92)
        canvas.create_text(cx, cy, text=f'Oil Drums: {app.player.barriers["OD"]}',
                           fill='black', font='Helvetica 15 bold')

        if app.is_game_over:
            canvas.create_text(map_start_x + 100, map_start_y - 50, text="GAME OVER!",
                               fill='red', font='Helvetica 15 bold')

        if app.pause:
            cx, cy = getCXY(app, 50, 65)
            canvas.create_text(cx, cy, text="Pause",
                               fill='red', font='Helvetica 25 bold')

            cx, cy = getCXY(app, 50, 60)
            canvas.create_text(cx, cy, text="Press any to continue",
                               fill='black', font='Helvetica 15 bold')

            for b in app.buttons:
                b.draw(app, canvas)

    elif app.UI == "Over":
        canvas.create_rectangle(0, 0, app.width, app.height, fill='#969285')

        cx, cy = getCXY(app, 50, 65)
        canvas.create_text(cx, cy, text="GAME OVER",
                           fill='red', font='Helvetica 25 bold')

        cx, cy = getCXY(app, 50, 60)
        canvas.create_text(cx, cy, text=f"Your Score is: {app.score}",
                           fill='black', font='Helvetica 15 bold')

        for b in app.buttons:
            b.draw(app, canvas)

    elif app.UI == "Help":
        text = "In the menu, click button Start for starting the game;\n"\
                "Click button Help for some help with the game.\n"\
                "In the game, press Esc for pausing the game.\n"\
                "Press Up to face up;\n"\
                "Press Down to face down;\n"\
                "Press Left to face left;\n"\
                "Press Right to face right.\n"\
                "Press w to move up;\n"\
                "Press s to move down;\n"\
                "Press a to move left;\n"\
                "Press d to move right.\n"\
                "Press 1 to change to pistol;\n"\
                "Press 2 to change to submachine gun;\n"\
                "Press 3 to change to sniper gun.\n"\
                "Press e to put a box;\n"\
                "Press q to put an oil drum.\n"\
                "Press Space to shoot;" \

        cx, cy = getCXY(app, 50, 50)
        canvas.create_rectangle(0, 0, app.width, app.height, fill='#E2D9B8')
        canvas.create_text(cx, cy, text=text,
                           fill='black', font='Helvetica 15 bold')
        for b in app.buttons:
            b.draw(app, canvas)

    else:
        pass


def runZombieWorldViewer():
    """
    Run the app
    :return: None
    """
    print('Running Zombie World Viewer!')
    runApp(width=1200, height=800)

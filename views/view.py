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
    # Variables needed to be updated
    map_size = min(app.width, app.height) - 100
    cell_size = map_size / app.map_blocks
    map_start_x = (app.width - map_size) / 2
    map_start_y = app.height - map_size - 10

    # Draw Map
    canvas.create_rectangle(map_start_x, map_start_y, map_start_x + map_size, map_start_y + map_size,
                            width=6, fill='#C9A946')

    # Draw Zombies
    for z in app.zombies:
        z.drawObject(app, canvas, cell_size)

    # Draw Player
    app.player.drawObject(app, canvas, cell_size)

    # Draw Bullets
    for b in app.player.bullets:
        b.drawObject(app, canvas, cell_size)

    # Draw Background
    canvas.create_rectangle(0, 0, app.width, map_start_y, fill='#E2D9B8', outline='black')
    canvas.create_rectangle(0, map_start_y + map_size, app.width, app.height, fill='#E2D9B8', outline='black')

    canvas.create_rectangle(0, 0, map_start_x, app.height, fill='#969285', outline='black')
    canvas.create_rectangle(map_start_x + map_size, 0, app.width, app.height, fill='#969285', outline='black')

    canvas.create_rectangle(map_start_x, map_start_y, map_start_x + map_size, map_start_y + map_size,
                            width=6, fill=None)

    # Show the HP
    canvas.create_text(map_start_x + 50, map_start_y - 50, text=f"HP: {app.player.getHP()}",
                       fill='black', font='Helvetica 15 bold')

    # Show the Score
    canvas.create_text(map_start_x + 200, map_start_y - 50, text=f"Score: {app.score}",
                       fill='black', font='Helvetica 15 bold')

    if app.is_game_over:
        canvas.create_text(map_start_x + 100, map_start_y - 50, text="GAME OVER!",
                           fill='red', font='Helvetica 15 bold')


def runZombieWorldViewer():
    """
    Run the app
    :return: None
    """
    print('Running Zombie World Viewer!')
    runApp(width=1200, height=800)

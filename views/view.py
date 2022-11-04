from utils.cmu_112_graphics import *
from models.app import *
from controllers.controller import *


def redrawAll(app, canvas):
    """
    Draw all the things on the canvas
    :param app: Current app object
    :param canvas: Current canvas object
    :return: None
    """
    canvas.create_text(app.width / 2, app.height / 2,
                       text='Draw your Freddy Fractal here!',
                       font='Arial 24 bold')


def runZombieWorldViewer():
    """
    Run the app
    :return: None
    """
    print('Running Zombie World Viewer!')
    runApp(width=600, height=600)

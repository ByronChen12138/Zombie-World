# Zombie-World

Welcome to the game Zombie World!

***

## How to Run this Game?
Before running this game, you need to install python on your computer and have all the files downloaded in a new directory. 
To help you check if the completeness of your download, the whole structure of this game is shown in the Section: **Project Structure**. 
After installed all the things correctly, you can finally play this game! 
For running the game, you just need to open the file "runZombieWorld.py", and run it in any IDE.

***

## User Manual
In the menu, click button <code>Start</code> for starting the game;
Click button <code>Help</code> for some help with the game.

In the game, press <code>Esc</code> for pause the game.

Press <code>Up</code> to face up;
Press <code>Down</code> to face down;
Press <code>Left</code> to face left;
Press <code>Right</code> to face right.

Press <code>w</code> to move up;
Press <code>s</code> to move down;
Press <code>a</code> to move left;
Press <code>d</code> to move right.

Press <code>1</code> to change to pistol;
Press <code>2</code> to change to submachine gun;
Press <code>3</code> to change to sniper gun.

Press <code>e</code> to put a box;
Press <code>q</code> to put an oil drum.

Press <code>Space</code> to shoot;

***

## Some Features

In this game, the submachine gun is given with deceleration, which has limited range of shooting

In this game, the speed zombie (in blue) is given with DFS path finding moving method but would only be used when the 
player is close enough. Due to the lack of comuputer, the best depth of dfs is set to 8 which will help the zombie find
the way only with the half part of one barrier.


***

## Project Structure

```console
.
├── controllers
    └── controller.py
├── models
    ├── app.py
    ├── Barrier.py
    ├── Bullet.py
    ├── Character.py
    ├── DrawingObject.py
    ├── Gun.py
    ├── Map.py
    ├── MyButton.py
    ├── Player.py
    └── Zombie.py
├── utils
    ├── cmu_112_graphics.py
    └── utils.py
├── views
    └── view.py
├── database.py
├── README.md
└── runZombieWorld.py
```

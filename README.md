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
The smallest window size for this game is 900 x 600, please play this game with the window size no less than this value.

In the menu, click button <code>Start</code> for starting the game;
Click button <code>Help</code> for some help with the game.

In the game, press <code>Esc</code> for pause the game.

Press <code>Up</code> to face up;
Press <code>Down</code> to face down;
Press <code>Left</code> to face left;
Press <code>Right</code> to face right.

Press <code>W</code> to move up;
Press <code>S</code> to move down;
Press <code>A</code> to move left;
Press <code>D</code> to move right.

Press <code>1</code> to change to pistol;
Press <code>2</code> to change to submachine gun;
Press <code>3</code> to change to sniper gun.

Press <code>E</code> to put a box;
Press <code>Q</code> to put an oil drum.

Press <code>Space</code> to shoot;

***

## Some Features

In this game, the submachine gun is given with deceleration, which has limited range of shooting

In this game, the speed zombie (in blue) is given with DFS path finding moving method but would only be used when the 
player is close enough. Due to the lack of comuputer, the best depth of dfs is set to 8 which will help the zombie find
the way only with the half part of one barrier.

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
├── sounds
    ├── button_enter.mp3
    ├── button_quit.mp3
    ├── OD.wav
    ├── player_hurt.wav
    ├── player_hurt2.wav
    ├── player_hurt3.wav
    └── zombie_hurt.wav
├── utils
    ├── cmu_112_graphics.py
    └── utils.py
├── views
    └── view.py
├── database.py
├── README.md
└── runZombieWorld.py
```

***
## Citation

In this project, several additional files are used and the sources are listed below:

**PACKAGE:**

<code>cmu_112_graphics.py</code> CMU EDU

<code>pygame</code> https://www.pygame.org/news

**SOUND:**

<code>Sound Class</code> https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWithPygame

<code>button_enter.mp3</code> https://www.zapsplat.com/sound-effect-category/button-clicks/

<code>button_quit.mp3</code> https://www.zapsplat.com/sound-effect-category/button-clicks/

<code>Ending.mp3</code> https://sc.chinaz.com/yinxiao/?classid=&keyword=%E5%83%B5%E5%B0%B8

<code>OD.wav</code> https://mixkit.co/

<code>player_hurt.wav</code> https://mixkit.co/

<code>player_hurt2.wav</code> https://mixkit.co/

<code>player_hurt3.wav</code> https://mixkit.co/

<code>Sniper.mp3</code> https://sc.chinaz.com/yinxiao/?classid=&keyword=%E5%83%B5%E5%B0%B8

<code>starting.flac</code> This War of Mine Original Soundtrack - Piotr Musiaê - This War of Mine

<code>zombie_hurt.wav</code> https://mixkit.co/




<code></code>

<code></code>

<code></code>

<code></code>
***

# Zombie-World

Welcome to the game Zombie World!

***

## How to Run this Game?
Before running this game, you need to install python and some packages on your computer and have all the files downloaded in a new directory. 
To help you install the packages, please run the file <code>beforeRunningGame.py</code> first, and this will print out
all the commands you need to run on the cmd for installing the packages.
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
├── images
    ├── Game Over.png
    ├── Game Over Sense.png
    └── Start.jpg
├── models
    ├── app.py
    ├── Barrier.py
    ├── Bullet.py
    ├── Character.py
    ├── DrawingObject.py
    ├── Gun.py
    ├── Map.py
    ├── Music.py
    ├── MyButton.py
    ├── Player.py
    ├── Sound.py
    └── Zombie.py
├── sounds
    ├── bit gun.wav
    ├── button_enter.mp3
    ├── button_quit.mp3
    ├── Ending.mp3
    ├── Gun Pick.wav
    ├── OD.wav
    ├── pistol.mp3
    ├── player_hurt.wav
    ├── player_hurt2.wav
    ├── player_hurt3.wav
    ├── Sniper.mp3
    ├── starting.flac
    ├── Submachine.mp3
    └── zombie_hurt.wav
├── utils
    ├── cmu_112_graphics.py
    └── utils.py
├── views
    └── view.py
├── beforeRunningGame
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

**IMAGE:**

<code>Game Over.png</code> https://pngtree.com/element/down?id=NjAyNjI1Mg==&type=1&time=1670279324&token=MzYzNmY5YWMyNmE5MTQxNmMwMDNlNTQ1NjAyOTY3OWU=

<code>Game Over Sense.png</code> https://www.freepik.com/premium-photo/zombie-hands-rising-dark-halloween-night_9026376.htm#query=zombie%20hand&position=25&from_view=keyword

<code>Start.jpg</code> https://www.iamag.co/speed-painting-weekly-selection-4/steve-jung-zombie-town/

**SOUND:**

<code>Sound Class</code> https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWithPygame

<code>Music Class</code> https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWithPygame

<code>button_enter.mp3</code> https://www.zapsplat.com/sound-effect-category/button-clicks/

<code>button_quit.mp3</code> https://www.zapsplat.com/sound-effect-category/button-clicks/

<code>Ending.mp3</code> https://sc.chinaz.com/yinxiao/?classid=&keyword=%E5%83%B5%E5%B0%B8

<code>OD.wav</code> https://mixkit.co/

<code>pistol.mp3</code> https://sc.chinaz.com/yinxiao/?classid=&keyword=%E5%83%B5%E5%B0%B8

<code>player_hurt.wav</code> https://mixkit.co/

<code>player_hurt2.wav</code> https://mixkit.co/

<code>player_hurt3.wav</code> https://mixkit.co/

<code>Sniper.mp3</code> https://sc.chinaz.com/yinxiao/?classid=&keyword=%E5%83%B5%E5%B0%B8

<code>starting.flac</code> This War of Mine Original Soundtrack - Piotr Musiaê - This War of Mine

<code>Submachine.mp3.wav</code> https://mixkit.co/

<code>zombie_hurt.wav</code> https://mixkit.co/

***

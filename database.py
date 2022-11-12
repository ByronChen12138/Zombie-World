import math

MAP_BLOCKS = 100
ZOMBIE_NUM = 10
ZOMBIE_LEGAL_DIS = 25
INVINCIBLE_TIME = 11
GUN_LEGAL_DIS = 10

DIRECTIONS = {"Up": (0, 1),
              "Down": (0, -1),
              "Left": (1, 0),
              "Right": (-1, 0)}
DIRECTIONS_LIST = ["Up", "Down", "Left", "Right"]

# Size, HP, Speed, Color, Damage, Heat Rate, Appear Rate, Score
Z_TYPE = {
    "Normal": [4, 100, 3, "#00DE72", 5, 1, 80, 5],
    "Speed": [3, 30, 0, "#008CE1", 3, 3, 10, 10],
    "Tank": [6, 300, 4, "red", 20, 0.2, 10, 20]}
Z_TYPE_LIST = ["Normal", "Speed", "Tank"]

# Size, Ammo, Heat Rate, Color, Damage, Speed, Appear Rate
G_TYPE = {
    "Pistol": [2, math.inf, 2, "yellow", 10, 2, 0],
    "Submachine": [3, 100, 1, "#9F5A5A", 20, 2, 60],
    "Sniper": [4, 8, 5, "#7F9591", 100, 2, 40]
}
G_TYPE_LIST = ["Pistol", "Submachine", "Sniper"]

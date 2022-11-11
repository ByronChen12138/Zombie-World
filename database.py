import math

MAP_BLOCKS = 100
ZOMBIE_NUM = 10
ZOMBIE_LEGAL_DIS = 25

DIRECTIONS = {"Up": (0, 1),
              "Down": (0, -1),
              "Left": (-1, 0),
              "Right": (1, 0)}
DIRECTIONS_LIST = ["Up", "Down", "Left", "Right"]

# Size, HP, Speed, Color, Damage, Heat Rate, Appear Rate
Z_TYPE = {
    "Normal": [3, 100, 1, "#00DE72", 5, 1, 80],
    "Speed": [2, 30, 3, "#008CE1", 3, 3, 10],
    "Tank": [6, 300, 0.2, "red", 20, 0.2, 10]}
Z_TYPE_LIST = ["Normal", "Speed", "Tank"]

# Size, Ammo, Heat Rate, Color, Damage, Appear Rate
G_TYPE = {
    "Pistol": [2, math.inf, 2, "black", 5, 60],
    "Submachine": [4, 100, 5, "#9F5A5A", 20, 20],
    "Sniper": [4, 8, 0.5, "#7F9591", 100, 20]
}
G_TYPE_LIST = ["Pistol", "Submachine", "Sniper"]

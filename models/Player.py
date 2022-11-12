from models.Bullet import Bullet
from utils.utils import *
from models.Character import Character
from models.Gun import Gun


class Player(Character):
    def __init__(self):
        size, ammo, heat_rate, color, damage, speed, appear_rate = G_TYPE["Pistol"]
        super().__init__(50, 50, 3, DIRECTIONS["Up"], "black", 100, 1, damage, appear_rate)
        self.guns = {"Pistol": ammo, "Submachine": 0, "Sniper": 0}
        self.curr_gun = "Pistol"
        self.curr_ammo = self.guns[self.curr_gun]
        self.barriers = {"Box": 100, "Oil Drum": 10}
        self.invincible_time = 0
        self.bullets = []

    def pickUpAGun(self, gun):
        g_type = gun.getType()
        if g_type in self.guns:
            self.guns[g_type] += gun.getAmmo()
        else:
            self.guns[g_type] = gun.getAmmo()
            self.curr_gun = g_type

        if g_type == self.curr_gun:
            self.curr_ammo = self.guns[self.curr_gun]

    def swapGun(self, g_type):
        self.curr_gun = g_type
        self.curr_ammo = self.guns[self.curr_gun]

    def shoot(self):
        size, ammo, heat_rate, color, damage, speed, appear_rate = G_TYPE[self.curr_gun]
        self.bullets.append(Bullet(self.x, self.y, self.direction, color, damage, speed))

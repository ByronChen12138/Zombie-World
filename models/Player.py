from models.Bullet import Bullet
from utils.utils import *
from models.Character import Character


class Player(Character):
    def __init__(self):
        size, ammo, heat_rate, color, damage, speed, appear_rate = G_TYPE["Pistol"]
        super().__init__(MAP_BLOCKS // 2, MAP_BLOCKS // 2, 3, DIRECTIONS["Up"], "black", 100, 0, damage, appear_rate)
        self.guns = {"Pistol": ammo, "Submachine": 0, "Sniper": 0}
        self.curr_gun = "Pistol"
        self.curr_ammo = self.guns[self.curr_gun]
        self.barriers = {"Box": 80, "OD": 30}
        self.invincible_time = 0
        self.bullets = []
        self.shoot_time = 0
        self.type = "Player"

    def __str__(self):
        return "Player"

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
        self.shoot_time = 0

    def shoot(self):
        size, ammo, heat_rate, color, damage, speed, appear_rate = G_TYPE[self.curr_gun]
        if self.guns[self.curr_gun] > 0:
            self.bullets.append(Bullet(self.x, self.y, self.direction, color, damage, speed))
            self.shoot_time = heat_rate
            self.guns[self.curr_gun] -= 1
            self.curr_ammo = self.guns[self.curr_gun]

    def putBarrier(self, app, b_type):
        if self.barriers[b_type] > 0:
            bx, by = self.direction
            bx *= -3
            by *= -3
            if app.map.createABarrier(self.x + bx, self.y + by, b_type):
                self.barriers[b_type] -= 1

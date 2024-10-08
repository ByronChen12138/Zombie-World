from utils.utils import *
from models.DrawingObject import DrawingObject


class Barrier(DrawingObject):
    def __init__(self, x, y, direction, b_type):
        size, HP, color = B_TYPE[b_type]
        super().__init__(x, y, size, "Square", direction, color)
        self.HP = HP
        self.b_type = b_type
        self.type = "Barrier"

    def __str__(self):
        return self.b_type + str(self.HP)

    def getHP(self):
        return self.HP

    def getBType(self):
        return self.b_type

    def doDamage(self, app):
        objs = app.map.getSurroundings(self, 5)
        for obj in objs:
            if obj.type == "Player" and app.player.invincible_time <= 0:
                app.player.invincible_time = INVINCIBLE_TIME
                app.player.color = "#DB1EF1"
                obj.HP -= 20
            elif isinstance(obj, Barrier):
                app.map.removeAnObj(obj)
                if obj.b_type == "OD":
                    obj.doDamage(app)
            elif obj.type != "Player":
                obj.HP -= 200

    def isBroken(self, app):
        if self.b_type == "OD" and self.HP <= 0:
            app.SOUND_OD.start()
            self.doDamage(app)
        return self.HP <= 0

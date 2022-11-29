from models.Barrier import Barrier
from models.Character import Character
from utils.utils import *


class Zombie(Character):
    def __init__(self, x, y, direction, z_type):
        size, HP, speed, color, damage, heat_rate, self.appear_rate, self.score = Z_TYPE[z_type]
        super().__init__(x, y, size, direction, color, HP, speed, damage, heat_rate)
        self.z_type = z_type
        if z_type == "Speed":
            self.move_type = "DFS"
        else:
            self.move_type = "Direct"
        self.type = "Zombie"

    def __str__(self):
        return self.z_type

    def getAppearRate(self):
        return self.appear_rate

    def getScore(self):
        return self.score

    def attack(self, character):
        """
        Attack the character with self damage
        :return: None
        """
        character.HP -= self.damage

    def moveRandom(self, app):
        """
        Upd the direction for the next move randomly
        :param app: current app
        :return: None
        """
        index = random.randint(0, 7)
        self.direction = DIRECTIONS[DIRECTIONS_LIST[index]]

    def moveDirect(self, app):
        """
        Upd the direction for the next move directly to the player
        :param app: current app
        :return: None
        """
        if app.player.x < self.x:
            if app.player.y < self.y:
                self.direction = DIRECTIONS["Up-Left"]
            elif app.player.y == self.y:
                self.direction = DIRECTIONS["Left"]
            else:
                self.direction = DIRECTIONS["Down-Left"]

        elif app.player.x == self.x:
            if app.player.y < self.y:
                self.direction = DIRECTIONS["Up"]
            elif app.player.y == self.y:
                self.direction = (0, 0)
            else:
                self.direction = DIRECTIONS["Down"]

        else:
            if app.player.y <= self.y:
                self.direction = DIRECTIONS["Up-Right"]
            elif app.player.y == self.y:
                self.direction = DIRECTIONS["Right"]
            else:
                self.direction = DIRECTIONS["Down-Right"]

    # TODO: Pure backtracking is tried but too many recursions
    def moveDFS(self, app):
        """
        Upd the direction for the next move using DFS
        :param app: current app
        :return: None
        """
        visited = set()
        self.direction = self.moveDFSRec(app, app.player.x, app.player.y, visited, (0, 0))[0]

    def moveDFSRec(self, app, curr_x, curr_y, visited, last_move, depth=0):
        """
        Find the shortest path from player to the zombie
        :param app: current app
        :param curr_x: current x
        :param curr_y: current y
        :param visited: the points visited
        :param last_move: Tuple, the last move made
        :param depth: current recursive depth
        :return: the first move for zombie and the length of the path, (0,0) if no path
        """
        # Base case: If current position is the zombie's position
        if self.x == curr_x and self.y == curr_y:
            return last_move, depth

        # Base case: If visited
        if (curr_x, curr_y) in visited:
            return (0, 0), None

        # Base case: If not possible to pass
        if not isCirclePositionLegal(app, curr_x, curr_y, self.size)[0]:
            return (0, 0), None

        # Base case: If too deep, best param is found to be 8, 10 can have best result
        if depth >= DFS_DEPTH:
            return (0, 0), None

        # RC: If not BC
        mini_length = math.inf
        mini_dir = (0, 0)
        for i in range(4):
            next_x = curr_x + DIRECTIONS[DIRECTIONS_LIST[i]][0]
            next_y = curr_y + DIRECTIONS[DIRECTIONS_LIST[i]][1]
            visited.add((curr_x, curr_y))

            last_dir, length = self.moveDFSRec(app, next_x, next_y, visited, DIRECTIONS[DIRECTIONS_LIST[i]], depth + 1)

            visited.remove((curr_x, curr_y))

            # For efficiency, stop finding the shortest path
            # if last_dir != (0, 0):
            #     return last_dir, length

            if last_dir == (0, 0):
                continue

            if length < mini_length:
                mini_length = length
                mini_dir = last_dir

        return mini_dir, mini_length

    def move(self, app):
        if self.move_type == "Random":
            self.moveRandom(app)

        elif self.move_type == "Direct":
            self.moveDirect(app)

        else:
            self.direction = (0, 0)
            # Only use dfs in a particular range
            if getDistance(self.x, self.y, app.player.x, app.player.y) <= DFS_DISTANCE:
                self.moveDFS(app)
            if self.direction == (0, 0):
                self.moveDirect(app)

        ans = super().move(app)

        if not ans:
            # If not moving on the map, attack possible barrier
            dx, dy = self.direction
            new_x = self.x - dx
            new_y = self.y - dy

            is_movable, barrier = isCirclePositionLegal(app, new_x, new_y, self.size)

            if barrier and isinstance(barrier, Barrier):
                self.attack(barrier)
                if barrier.isBroken(app):
                    app.map.removeAnObj(barrier)

        return ans

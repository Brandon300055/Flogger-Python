
import pygame
import game
import froggerlib
from config import *



class Frogger(game.Game):
    def __init__(self):
        game.Game.__init__(self, TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
        self.stage1 = froggerlib.Stage(0, 10 * VG, SCREEN_WIDTH, VG)
        self.stage2 = froggerlib.Stage(0, 5 * VG, SCREEN_WIDTH, VG)
        self.home = froggerlib.Home(0, 0 * VG, SCREEN_WIDTH, VG)
        self.road = froggerlib.Road(0, 6 * VG, SCREEN_WIDTH, 4 * VG)
        self.water = froggerlib.Water(0, VG, SCREEN_WIDTH, 4 * VG)
        self.frog = None
        self.restart()

        y = 9 * VG + PADDING
        self.cars = [
            froggerlib.Car(0, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 4),
            froggerlib.Car(SCREEN_WIDTH/4, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 4),
            froggerlib.Car(SCREEN_WIDTH/4*2, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 4),
            froggerlib.Car(SCREEN_WIDTH/4*3, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 4),
        ]
        y = 8 * VG + PADDING
        self.trucks = [
            froggerlib.Truck(0, y, 2 * FROG_SIZE + 10, FROG_SIZE, SCREEN_WIDTH, y, 3),
            froggerlib.Truck(SCREEN_WIDTH/3, y, 2 * FROG_SIZE + 10, FROG_SIZE, SCREEN_WIDTH, y, 3),
            froggerlib.Truck(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE + 10, FROG_SIZE, SCREEN_WIDTH, y, 3),
        ]
        y = 7 * VG + PADDING
        self.dozers = [
            froggerlib.Dozer(0, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
            froggerlib.Dozer(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
            froggerlib.Dozer(SCREEN_WIDTH/3, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
            froggerlib.Dozer(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
            froggerlib.Dozer(-SCREEN_WIDTH/3, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
            froggerlib.Dozer(-SCREEN_WIDTH, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 1),
        ]
        y = 6 * VG + PADDING
        self.racecars = [
            froggerlib.RaceCar(0, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
            froggerlib.RaceCar(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
            froggerlib.RaceCar(SCREEN_WIDTH/3, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
            froggerlib.RaceCar(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
            froggerlib.RaceCar(-SCREEN_WIDTH/3, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
            froggerlib.RaceCar(-SCREEN_WIDTH, y, 2 * FROG_SIZE + 7, FROG_SIZE + 5, -SCREEN_WIDTH, y, 6, 7),
        ]

        self.allcars = self.cars + self.trucks + self.dozers + self.racecars

        y = 4 * VG + PADDING
        self.logs = [
            froggerlib.Log(0, y, 2 * FROG_SIZE * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE  * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(SCREEN_WIDTH/3, y, 2 * FROG_SIZE  * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE  * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(-SCREEN_WIDTH/3, y, 2 * FROG_SIZE  * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(-SCREEN_WIDTH, y, 2 * FROG_SIZE * 3, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
        ]

        y = 3 * VG + PADDING
        self.turtles = [
            froggerlib.Turtle(0, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
            #froggerlib.Turtle(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
            froggerlib.Turtle(SCREEN_WIDTH/3, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
            froggerlib.Turtle(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
            #froggerlib.Turtle(-SCREEN_WIDTH/3, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
            froggerlib.Turtle(-SCREEN_WIDTH, y, 2 * FROG_SIZE, FROG_SIZE, SCREEN_WIDTH, y, 2.5),
        ]

        y = 2 * VG + PADDING
        self.logs2 = [
            froggerlib.Log(0, y, 2 * FROG_SIZE * 2.5, FROG_SIZE, -SCREEN_WIDTH, y, 1.5),
            froggerlib.Log(SCREEN_WIDTH/3, y, 2 * FROG_SIZE  * 2.5, FROG_SIZE, -SCREEN_WIDTH, y, 2),
            froggerlib.Log(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE  * 2.5, FROG_SIZE, -SCREEN_WIDTH, y, 2),
            froggerlib.Log(-SCREEN_WIDTH, y, 2 * FROG_SIZE * 2.5, FROG_SIZE, -SCREEN_WIDTH, y, 2),
        ]

        y = 1 * VG + PADDING
        self.turtles2 = [
            froggerlib.Turtle(0, y, 2 * FROG_SIZE, FROG_SIZE, -SCREEN_WIDTH, y, 8.5),
            froggerlib.Turtle(SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE, FROG_SIZE, -SCREEN_WIDTH, y, 8.5),
            froggerlib.Turtle(SCREEN_WIDTH/3, y, 2 * FROG_SIZE, FROG_SIZE, -SCREEN_WIDTH, y, 8.5),
            froggerlib.Turtle(-SCREEN_WIDTH/3*2, y, 2 * FROG_SIZE, FROG_SIZE, -SCREEN_WIDTH, y, 8.5),
        ]
        y = 0 * VG
        self.grass = [
            froggerlib.Grass(0, y, VG, VG ),
            froggerlib.Grass(VG*3, y, VG, VG ),
            froggerlib.Grass(VG*6, y, VG, VG ),
            froggerlib.Grass(VG*9, y, VG, VG ),
            froggerlib.Grass(VG*12, y, VG, VG ),
            froggerlib.Grass(VG*15, y, VG, VG ),
        ]

        self.ridable = self.logs + self.turtles + self.logs2 + self.turtles2

        self.movable = self.allcars + self.ridable



    def restart(self):
        self.frog = None
        x = COLS // 2 * HG + PADDING
        y = (ROWS - 1) * VG + PADDING
        self.frog = froggerlib.Frog(x, y, FROG_SIZE, FROG_SIZE, x, y, 8, HG, VG)

    def dead(self):
        #outofbounds
        if self.frog.outOfBounds(SCREEN_WIDTH, SCREEN_HEIGHT):
            print("No Leaving")
            return True
        #hit by car
        for c in self.allcars:
            if c.hits(self.frog):
                print("you've got ran over")
                return True
        #drowns
        for log in self.ridable:
            if log.supports(self.frog):
                return False
        if self.water.hits(self.frog):
            print("you've drown")
            return True
        #touches grass

        if self.home.hits(self.frog):
            return True
            print("You WIN AT LIFE FROG!!!!!!!! :)")
        return False

    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
        if self.dead():
            if pygame.K_r in newkeys:
                self.restart()
            return

        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_UP in newkeys:
            self.frog.up()

        if pygame.K_DOWN in newkeys:
            self.frog.down()

        if pygame.K_LEFT in newkeys:
            self.frog.left()

        if pygame.K_RIGHT in newkeys:
            self.frog.right()

        for c in self.movable:
            c.move()

        for c in self.movable:
            if c.atDesiredLocation():
                if c.getX() > 0:
                    c.setX(0 - c.getWidth())
                else:
                    c.setX(SCREEN_WIDTH)
        self.frog.move()


    def draw_stage(self, surface, stage):
        color = (37.6, 100.2, 22)
        self.draw_object(surface, color, stage)

    def draw_home(self, surface, stage):
        color = (37.6, 100.2, 22)
        self.draw_object(surface, color, stage)

    def draw_grass(self, surface, stage):
        color = (0, 50, 0)
        self.draw_object(surface, color, stage)

    def draw_road(self, surface, stage):
        color = (94, 94, 94)
        self.draw_object(surface, color, stage)

    def draw_water(self, surface, stage):
        color = (50, 150, 250)
        self.draw_object(surface, color, stage)

    def draw_frog(self, surface, stage):
        color = (48, 252, 48)
        self.draw_object(surface, color, stage)

    def draw_car(self, surface, stage):
        color = (255,165,0)
        self.draw_object(surface, color, stage)

    def draw_truck(self, surface, stage):
        color = (0, 0, 255)
        self.draw_object(surface, color, stage)

    def draw_dozer(self, surface, stage):
        color = (255,255,0)
        self.draw_object(surface, color, stage)

    def draw_racecar(self, surface, stage):
        color = (255,0,0)
        self.draw_object(surface, color, stage)

    def draw_log(self, surface, stage):
        color = (130, 82, 1)
        self.draw_object(surface, color, stage)

    def draw_turtle(self, surface, stage):
        color = (0, 82, 1)
        self.draw_object(surface, color, stage)

    def draw_object(self, surface, color, obj):
        rect = pygame.Rect(obj.getX(), obj.getY(), obj.getWidth(), obj.getHeight())
        pygame.draw.rect(surface, color, rect)

    def paint(self, surface):
        surface.fill((0, 0, 0))

        self.draw_stage(surface, self.stage1)
        self.draw_stage(surface, self.stage2)
        self.draw_home(surface, self.home)
        self.draw_road(surface, self.road)
        self.draw_water(surface, self.water)

        for c in self.cars:
            self.draw_car(surface, c)
        for c in self.trucks:
            self.draw_truck(surface, c)
        for c in self.dozers:
            self.draw_dozer(surface, c)
        for c in self.racecars:
            self.draw_racecar(surface, c)
        for c in self.logs:
            self.draw_log(surface, c)
        for c in self.turtles:
            self.draw_turtle(surface, c)
        for c in self.logs2:
            self.draw_log(surface, c)
        for c in self.turtles2:
            self.draw_turtle(surface, c)
        for c in self.grass:
            self.draw_grass(surface, c)

        self.draw_frog(surface, self.frog)


        if DEBUG:
            for y in range(ROWS):
                for x in range(COLS):
                    py = y * VG
                    px = x * HG
                    rect = pygame.Rect(px, py, HG, VG)
                    pygame.draw.rect(surface, (255, 255, 0), rect, 1)


def main():
    pygame.font.init()
    game = Frogger()
    game.main_loop()


if __name__ == "__main__":
    main()

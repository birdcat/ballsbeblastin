import pygame, sys
from dictionaries import cannon_dict
from dictionaries import ball_dict

#global variables
current_screen = 1
current_cannon = "c1"
current_ball = "b1"
current_coins = 200

pygame.font.init()
stats_font = pygame.font.SysFont('Comic Sans MS', 50)
button_font = pygame.font.SysFont('Comic Sans MS', 30)

'''---------------------------------SPRITES/CLASSES---------------------'''

class Button:
    def __init__(self, text, pos, size, window):
        self.x, self.y = pos
        self.font = button_font
        self.text = self.font.render(text, False, 'white')
        self.surface = pygame.Surface(size)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.window = window

    def draw(self):
        self.window.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
        return False
class Menu(object):
    def __init__(self):
        self.screen_width = 1250
        self.screen_height = 700
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.windowclock = pygame.time.Clock()
        self.width_border = self.screen_width / 100
        self.height_border = self.screen_height / 50
        self.menu_label_width = self.screen_width / 2
        self.menu_label_height = self.screen_height / 5
        self.menu_stats_y = self.height_border + self.menu_label_height + 10
        self.menu_stats_height = self.screen_height - self.menu_stats_y - self.height_border
        self.bgimg = "images/mainbg.jpg"
        self.bg = pygame.image.load(self.bgimg)
        self.store = Store(self.screen_width, self.screen_height)
        self.game = Game()
        self.Main()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        menu_label = pygame.Rect(self.width_border, self.height_border, self.menu_label_width, self.menu_label_height)
        pygame.draw.rect(self.window, 'black', menu_label, 5)
        menu_stats = pygame.Rect(self.width_border, self.menu_stats_y, self.menu_label_width, self.menu_stats_height)
        pygame.draw.rect(self.window, 'black', menu_stats, 5)

        cannon_mass_text = stats_font.render(f'Cannon Mass:{cannon_dict[current_cannon]["m"]}', False, (0, 0, 0))
        self.window.blit(cannon_mass_text, (2*self.width_border, self.menu_stats_y+self.height_border))
        ball_mass_text = stats_font.render(f'Ball Mass:{ball_dict[current_ball]["m"]}', False, (0, 0, 0))
        self.window.blit(ball_mass_text, (2*self.width_border, self.menu_stats_y+50+self.height_border))
        ball_velocity_text = stats_font.render(f'Ball Velocity:{ball_dict[current_ball]["v"]}', False, (0, 0, 0))
        self.window.blit(ball_velocity_text, (2 * self.width_border, self.menu_stats_y + 100 + self.height_border))
    def Main(self):
        self.draw()
        button_store = Button(
            "Store",
            (2 * self.width_border, self.menu_stats_y + 170 + self.height_border),
            (100, 50),
            self.window
            )
        button_game = Button(
            "Play",
            (2 * self.width_border, self.menu_stats_y + 220 + self.height_border),
            (100, 50),
            self.window
            )

        while True:
            # put drawing stuff here

            # Event Tasking
            # Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if button_store.click(event):
                    self.store.running = True
                    self.store.loop()
                if button_game.click(event):
                    self.game.running = True
                    self.game.loop()
            self.draw()
            button_store.draw()
            button_game.draw()
            pygame.display.update()
            self.windowclock.tick(60)

class Store(object):
    def __init__(self, w, h):
        self.bgimg = "images/storebg.jpg"
        self.bg = pygame.image.load(self.bgimg)
        self.cannon = current_cannon
        self.ball = current_ball
        self.running = False
        self.clock = pygame.time.Clock()
        self.sw = w
        self.sh = h
        self.window = pygame.display.set_mode((self.sw, self.sh))
        self.cannons = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.coins = 0

        # getting all the buttons into groups(should eventually go into seperate function)
        xph = 20
        yph = 50
        countph = 0
        for key in cannon_dict:
            self.cannons.add(self.Storebutton(xph, yph + countph, key, "c", cannon_dict[key]["m"], "", cannon_dict[key]["cost"], cannon_dict[key]["boughtimg"], cannon_dict[key]["notboughtimg"], cannon_dict[key]["bought"]))
            countph += 200
            if countph >= 600:
                xph = 220
                countph = 0
        xph = 570
        for key in ball_dict:
            self.balls.add(self.Storebutton(xph, yph + countph, key, "b", ball_dict[key]["m"], ball_dict[key]["v"], ball_dict[key]["cost"], ball_dict[key]["boughtimg"], ball_dict[key]["notboughtimg"], ball_dict[key]["bought"]))
            countph += 200
            if countph >= 600:
                xph = 770
                countph = 0

    def loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for cannon in self.cannons:
                    cannon.clickcheck(event)
                for ball in self.balls:
                    ball.clickcheck(event)

            self.window.blit(self.bg, (0, 0))

            self.cannons.draw(self.window)
            self.balls.draw(self.window)

            for cannon in self.cannons:
                cannon.printinfo(self.window)
            for ball in self.balls:
                ball.printinfo(self.window)

            pygame.display.update()
            self.clock.tick(60)
            # while True:

    class Storebutton(pygame.sprite.Sprite):
        def __init__(self, x, y, name, type, mass, velocity, cost, boughtimage, notboughtimage, bought):
            super().__init__()
            self.type = type
            self.id = name
            self.images = [boughtimage, notboughtimage]
            self.image = pygame.image.load(self.images[1])
            self.image = pygame.transform.scale(self.image, (150, 150))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.mass = mass
            self.velocity = velocity
            self.cost = cost
            self.bought = bought
            self.font = pygame.font.SysFont('Comic Sans MS', 20)

        def clickcheck(self, event):
            global current_coins, current_ball, current_cannon
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        if not self.bought and current_coins >= self.cost:
                            self.bought = True
                            current_coins -= self.cost
                            self.image = pygame.image.load(self.images[0])
                            self.image = pygame.transform.scale(self.image, (150, 150))

                            if self.type == "c":
                                cannon_dict[self.id]["bought"] = True
                                current_cannon = self.id
                            elif self.type == "b":
                                ball_dict[self.id]["bought"] = True
                                current_ball = self.id

                        elif self.bought:
                            if self.type == "c":
                                current_cannon = self.id
                            elif self.type == "b":
                                current_ball = self.id

                print(current_coins, current_cannon, current_ball)

        def printinfo(self, window):
            mtext = self.font.render(f'MASS:{self.mass}', False, (0, 0, 0))
            window.blit(mtext, (self.rect.x + 110, self.rect.y + 55))
            if self.velocity != "":
                vtext = self.font.render(f'VELOCITY:{self.velocity}', False, (0, 0, 0))
                window.blit(vtext, (self.rect.x + 110, self.rect.y + 80))
            ctext = self.font.render(f'${self.cost}', False, (0, 0, 0))
            window.blit(ctext, (self.rect.x + 50, self.rect.y + 125))


# ==================GAME STUFF==========================
class Game(object):
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.running = False
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.windowclock = pygame.time.Clock()
    class Cannon(object):
        def __init__(self):
            self.mass=cannon_dict[current_cannon]["m"]
            self.momentum=ball_dict[current_ball]["m"]*ball_dict[current_ball]["v"]
            self.velocity = self.momentum/self.mass
            self.acc=0.01
            self.image=pygame.image.load(cannon_dict[current_cannon]["mainimg"])
        def slow(self, monster):
            self.momentum-=self.acc
            # self.mass+=monster.getMass()
            # self.momentum-=monster.getMomentum()
        def calcSpeed(self):
            self.velocity=self.momentum/self.mass
            print(self.velocity)
        def draw(self, window):
            window.blit(self.image, (200,300))
    class Background(object):
        def __init__(self, num):
            self.back= pygame.image.load("images/mainbg.jpg")
            #self.back2= pygame.image.load("images/mainbg.jpg")
            self.backx=num
        def move(self, window, v):
            self.backx+=v
            if self.backx==1250:
                self.backx=-2590
            window.blit(self.back, (self.backx, 0))

    def loop(self):
        cannon = self.Cannon()
        self.window.fill((255, 255, 255))
        back1 = self.Background(0)
        back2 = self.Background(-1920)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            cannon.slow("a")
            cannon.calcSpeed()
            back1.move(self.window, cannon.velocity)
            back2.move(self.window, cannon.velocity)
            cannon.draw(self.window)
            pygame.display.update()
            self.windowclock.tick(60)


if __name__ == '__main__':
    Menu()

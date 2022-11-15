import pygame, sys
import random
from dictionaries_test import cannon_dict
from dictionaries_test import ball_dict
from dictionaries_test import monster_dict
from vars import current_ball1, current_cannon1, current_coins1

current_cannon = current_cannon1
current_ball = current_ball1
current_coins = current_coins1

#with open('vars.py', 'w') as f: # 'r' is a reading mode
   # f.write(text)

# global variables moved to separate file later
#current_cannon = "c1"
#current_ball = "b1"
#current_coins = 1000

# window stuff
window_width = 1250
window_height = 650

# Different fonts we'll use
pygame.font.init()
title_font = pygame.font.SysFont('Comic Sans MS', 60)
stats_font = pygame.font.SysFont('Comic Sans MS', 50)
button_font = pygame.font.SysFont('Comic Sans MS', 30)
label_font=pygame.font.SysFont('Comic Sans MS', 15)

'''---------------------------------SPRITES/CLASSES---------------------'''
# Very used button class: makes text button
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

# Starting screen: menu, leads to store and game. Shows current stats
class Menu(object):
    def __init__(self):
        self.window = pygame.display.set_mode((window_width, window_height))
        self.windowclock = pygame.time.Clock()
        self.width_border = window_width / 100
        self.height_border = window_height / 50
        self.menu_label_width = window_width / 2
        self.menu_label_height = window_height / 5
        self.menu_stats_y = self.height_border + self.menu_label_height + 10
        self.menu_stats_height = window_height - self.menu_stats_y - self.height_border
        self.bgimg = "images/mainbg.jpg"
        self.bg = pygame.image.load(self.bgimg)
        self.store = Store(window_width, window_height)
        self.game = Game()
        self.Main()

    def draw(self):
        self.window.blit(self.bg, (0, 0))
        menu_label = pygame.Rect(self.width_border, self.height_border, self.menu_label_width, self.menu_label_height)
        pygame.draw.rect(self.window, 'black', menu_label, 5)
        menu_stats = pygame.Rect(self.width_border, self.menu_stats_y, self.menu_label_width, self.menu_stats_height)
        pygame.draw.rect(self.window, 'black', menu_stats, 5)

        title_text = title_font.render("BALLS BE BLASTIN'", False, (0, 0, 0))
        self.window.blit(title_text, (2 * self.width_border, 50))
        cannon_mass_text = stats_font.render(f'Cannon Mass:{cannon_dict[current_cannon]["m"]}', False, (0, 0, 0))
        self.window.blit(cannon_mass_text, (2*self.width_border, self.menu_stats_y+self.height_border))
        ball_mass_text = stats_font.render(f'Ball Mass:{ball_dict[current_ball]["m"]}', False, (0, 0, 0))
        self.window.blit(ball_mass_text, (2*self.width_border, self.menu_stats_y+50+self.height_border))
        ball_velocity_text = stats_font.render(f'Ball Velocity:{ball_dict[current_ball]["v"]}', False, (0, 0, 0))
        self.window.blit(ball_velocity_text, (2 * self.width_border, self.menu_stats_y + 100 + self.height_border))

        instructions_text = label_font.render('*Click monsters to gain coins and stop them from colliding with you', False, (0, 0, 0))
        self.window.blit(instructions_text, (2 * self.width_border, self.menu_stats_y + 400 + self.height_border))
        cannon_image = pygame.transform.scale(pygame.image.load(cannon_dict[current_cannon]["mainimg"]), (500,300))
        self.window.blit(cannon_image, (700, 300))
    def Main(self): # this is the main loop for the menu, game and store loops both run from this
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
            #loop for main function, checks buttons to potentially run game/store loops
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setGlobe()
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

class Store(object):    #store class, has store loop and store sprites
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
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.coinx, self.coiny = 700, 20

        # getting all the buttons into groups
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

    def loop(self): #main loop for store
        button_back = Button(
            "Home",
            (0, 0),
            (100, 50),
            self.window
        )
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    setGlobe()
                if button_back.click(event):
                    self.running = False
                for cannon in self.cannons:
                    cannon.clickcheck(event)
                for ball in self.balls:
                    ball.clickcheck(event)

            self.window.blit(self.bg, (0, 0))

            self.printcoins(current_coins)

            self.cannons.draw(self.window)
            self.balls.draw(self.window)

            button_back.draw()

            for cannon in self.cannons:
                cannon.printinfo(self.window)
            for ball in self.balls:
                ball.printinfo(self.window)

            pygame.display.update()
            self.clock.tick(60)
            # while True:

    class Storebutton(pygame.sprite.Sprite): #class for each item in store, taking in stuff from dictionary
        def __init__(self, x, y, name, type, mass, velocity, cost, boughtimage, notboughtimage, bought):
            super().__init__()
            self.type = type
            self.id = name
            self.images = [boughtimage, notboughtimage]
            if bought:
                self.image = pygame.image.load(self.images[0])
            else:
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

        def clickcheck(self, event): #checks whether or not a button has been clicked and updates needed variables accordingly
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


        def printinfo(self, window): #prints the mass, velocity, and cost of each button onto it so player knows what's up
            mtext = self.font.render(f'MASS:{self.mass}', False, (0, 0, 0))
            window.blit(mtext, (self.rect.x + 110, self.rect.y + 55))
            if self.velocity != "":
                vtext = self.font.render(f'VELOCITY:{self.velocity}', False, (0, 0, 0))
                window.blit(vtext, (self.rect.x + 110, self.rect.y + 80))
            ctext = self.font.render(f'${self.cost}', False, (0, 0, 0))
            window.blit(ctext, (self.rect.x + 50, self.rect.y + 125))

    def printcoins(self, current_coins): # blits text that tells player how many coins they have
        cointext = self.font.render(f'YOU HAVE {current_coins} COINS', False, (0, 0, 0))
        self.window.blit(cointext, (self.coinx, self.coiny))


# ==================GAME STUFF==========================
class Game(object):
    def __init__(self):
        self.running = False
        self.window = pygame.display.set_mode((window_width, window_height))
        self.windowclock = pygame.time.Clock()
        self.monsters = pygame.sprite.Group()
        self.cannons = pygame.sprite.Group()
    class Cannon(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.mass = cannon_dict[current_cannon]["m"]
            self.momentum = ball_dict[current_ball]["m"]*ball_dict[current_ball]["v"]
            self.velocity = round(self.momentum/self.mass, 5)
            self.acc = 0.005
            self.image = pygame.image.load(cannon_dict[current_cannon]["mainimg"])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.monstercollisioncount = 0
        def updatemovement(self):
            self.velocity = self.momentum/self.mass - self.acc
            self.momentum = self.velocity * self.mass


        #def draw(self, window, y):
            #window.blit(self.image, (600,400+y))

        def monstercollisioncheck(self, monster):
            if self.rect.colliderect(monster) and not monster.collided:
                monster.collided = True
                self.mass += monster.mass
                self.momentum -= monster.velocity*monster.mass
                monster.velocity = 0
    class Background(object):
        def __init__(self, num):
            self.back= pygame.transform.scale(pygame.image.load("images/P_Cave_Background.jpg"), (1300, 650))
            self.backx = num
            self.backy =- 50
        def move(self, window, v):
            self.backx += v
            if self.backx >= 1250:
                self.backx = -1350
            window.blit(self.back, (self.backx, self.backy))
        def shaky(self, shake):
            self.backy += shake

    class Monster(pygame.sprite.Sprite):
        def __init__(self, monster_dict, name, x, y):
            super().__init__()
            self.name = name
            self.images = monster_dict[name]["imagefolder"]
            self.image = pygame.image.load(self.images + "/1.tiff")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.x = x
            self.rect.y = y
            self.mass = monster_dict[name]["mass"]
            self.velocity = monster_dict[name]["velocity"]
            self.clicksneeded = monster_dict[name]["clickcount"]
            self.coins = monster_dict[name]["coins"]
            self.clicksclicked = 0
            self.clicked = False
            self.collided = False
            self.counter = 1
            self.countercounter = 0
            self.dead = False
        def normalmovement(self, velocity):
            if self.collided:
                t = 0
            else:
                self.x += velocity
                self.rect.x = self.x
                if self.countercounter == 15:
                    self.counter += 1
                    if self.counter == 11:
                        self.counter = 1
                    self.countercounter = 0
                    self.image = pygame.image.load(self.images + "/" + str(self.counter) + ".tiff")
                self.countercounter += 1

                if self.name == "m3":
                    if self.counter < 5:
                        self.rect.y -= 2
                    elif self.counter < 6:
                        self.rect.y -= 1
                    elif self.counter < 7:
                        self.rect.y += 1
                    else:
                        self.rect.y += 2
        def clickcheck(self, event):
            x, y = pygame.mouse.get_pos()
            global current_coins
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y) and not self.clicked:
                        self.clicked = True
                        self.clicksclicked += 1
                        print(self.clicksclicked)
                        if self.clicksclicked == self.clicksneeded:
                            self.dead = True
                            current_coins += self.coins

            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicked = False
    class Ball(object):
        def __init__(self):
            self.ball = pygame.image.load(ball_dict[current_ball]["mainimg"])
            self.v = ball_dict[current_ball]["v"]*10
            self.x = 850
            self.y = 300
        def draw(self, window):
            self.x += self.v
            window.blit(self.ball, (self.x, self.y))
    def loop(self):
        cannon = self.Cannon(850, 800)
        self.cannons.add(cannon)
        button_back = Button(
            "Home",
            (0, 0),
            (100, 50),
            self.window
        )
        monster = self.Monster(monster_dict, "m1", 0, 400)
        self.monsters.add(monster)
        ball = self.Ball()
        #self.window.fill((255, 255, 255))
        back1 = self.Background(0)
        back2 = self.Background(-1300)
        ball.draw(self.window)
        time = 0
        instantaneous_time=round(1/60, 2)
        distance = 0
        shake = 50
        endS = False
        coin_pre = current_coins
        monsterdistcount = 1
        button_leave = Button(
            "Leave",
            (0, 0),
            (100, 50),
            self.window
        )
        up = True
        while self.running:
            while not endS:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.monsters.empty()
                        self.running = False
                        endS=True
                        setGlobe()
                    if button_back.click(event):
                        self.monsters.empty()
                        self.running = False
                        endS=True
                        setGlobe()
                    for monster in self.monsters:
                        if not monster.collided:
                            monster.clickcheck(event)

                if distance // 30 == monsterdistcount:
                    monsterdistcount += 1
                    if distance > 120:
                        self.monsters.add(self.Monster(monster_dict, "m" + str(random.randint(1, 3)), 0, 400))
                    else:
                        self.monsters.add(self.Monster(monster_dict, "m" + str(random.randint(1, 2)), 0, 400))
                if time > 1.3 and time < 5:
                    if up:
                        back1.shaky(shake)
                        back2.shaky(shake)
                        if shake > 0:
                            shake -= 0.5
                        up = False
                    else:
                        back1.shaky(-shake)
                        back2.shaky(-shake)
                        if shake > 0:
                            shake -= 0.5
                        up = True
                if time > 1:
                    self.draw(cannon, button_back, back1, back2, distance)
                    distance += instantaneous_time*cannon.velocity
                else:
                    self.drawPrefire(cannon, button_back, back1, distance)
                if distance > 730 and distance < 731:
                    back1.back=pygame.transform.scale(pygame.image.load("images/matrix background.jpg"), (1300, 650))
                    back2.back = pygame.transform.scale(pygame.image.load("images/matrix background.jpg"), (1300, 650))
                if time > 1 and time < 1.3:
                    ball.draw(self.window)
                if cannon.velocity <= 0:
                    self.monsters.empty()
                    endS = True
                    if distance <730:
                        distance_text = stats_font.render(f'You traveled {round(distance, 2)}m '
                                                      f'and gained {current_coins-coin_pre} coins!', False, (0, 0, 0))
                    else:
                        distance_text = stats_font.render(f'You escaped the cave, congrats?', False, (0, 0, 0))
                time += 1/60
                pygame.display.update()
                self.windowclock.tick(60)
            while endS and self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.monsters.empty()
                        self.running = False
                        endS=False
                        setGlobe()
                    if button_leave.click(event):
                        self.monsters.empty()
                        self.running = False
                        endS = False
                        setGlobe()
                pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, 250, 1500, 200))
                self.window.blit(distance_text, (5, 300))
                button_leave.draw()
                pygame.display.update()
                self.windowclock.tick(60)


    def draw(self, cannon, button_back, back1, back2, distance):
        for monster in self.monsters:
            monster.normalmovement(cannon.velocity)
            cannon.monstercollisioncheck(monster)
            if monster.dead:
                self.monsters.remove(monster)
        cannon.updatemovement()
        back1.move(self.window, cannon.velocity)
        back2.move(self.window, cannon.velocity)
        self.cannons.draw(self.window)
        button_back.draw()
        self.monsters.draw(self.window)
        cannon_mass_text = label_font.render(f'Cannon Mass: {cannon.mass} kg', False, (0, 0, 0))
        self.window.blit(cannon_mass_text, (850, 500))
        cannon_velocity_text = label_font.render(f'Cannon Velocity: {round(cannon.velocity, 2)} m/s', False, (0, 0, 0))
        self.window.blit(cannon_velocity_text, (850, 520))
        distance_text = label_font.render(f'Distance: {round(distance, 2)} m', False, (0, 0, 0))
        self.window.blit(distance_text, (850, 540))
    def drawPrefire(self, cannon, button_back, back1, distance):
        back1.move(self.window, 0)
        self.cannons.draw(self.window)
        cannon.rect.y = back1.backy + 400
        button_back.draw()
        cannon_mass_text = label_font.render(f'Cannon Mass: {cannon.mass + ball_dict[current_ball]["m"]} kg', False,
                                             (0, 0, 0))
        self.window.blit(cannon_mass_text, (850, 500))
        cannon_velocity_text = label_font.render(f'Cannon Velocity: 0 m/s', False,
                                                 (0, 0, 0))
        self.window.blit(cannon_velocity_text, (850, 520))
        distance_text = label_font.render(f'Distance: {distance} kg', False, (0, 0, 0))
        self.window.blit(distance_text, (850, 540))

def setGlobe():
    with open("vars.py", "w") as f:
        f.write(f"current_ball1='{current_ball}'\n")
        f.write(f"current_cannon1='{current_cannon}'\n")
        f.write(f"current_coins1={current_coins}\n")
        for i in range(1, 7):
            f.write(f"bc{i}={cannon_dict[f'c{i}']['bought']}\n")
        for i in range(1, 7):
            f.write(f"bb{i}={ball_dict[f'b{i}']['bought']}\n")
if __name__ == '__main__':
    Menu()

import pygame, sys
from dictionaries import cannon_dict
from dictionaries import ball_dict

#global variables
current_screen = 1
current_cannon="c1"
current_ball="b1"

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
                    print("clicked")
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
        self.Main()

    def Main(self):

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
                button_game.click(event)
            self.window.blit(self.bg, (0, 0))
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


    def loop(self):
        # getting all the buttons into groups(should eventually go into seperate function)
        xph = 20
        yph = 50
        countph = 0
        for key in cannon_dict:
            self.cannons.add(self.Storebutton(xph, yph + countph, key, cannon_dict[key]["m"], "", cannon_dict[key]["cost"], cannon_dict[key]["boughtimg"], cannon_dict[key]["notboughtimg"]))
            countph += 200
            if countph >= 600:
                xph = 220
                countph = 0
        xph = 570
        for key in ball_dict:
            self.balls.add(self.Storebutton(xph, yph + countph, key, ball_dict[key]["m"], ball_dict[key]["v"], ball_dict[key]["cost"],
                                              ball_dict[key]["boughtimg"], ball_dict[key]["notboughtimg"]))
            countph += 200
            if countph >= 600:
                xph = 770
                countph = 0


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.window.blit(self.bg, (0, 0))

            self.cannons.draw(self.window)
            self.balls.draw(self.window)

            for cannon in self.cannons:
                # cannon.clickcheck(event)
                cannon.printinfo(self.window)
            for ball in self.balls:
                # ball.clickcheck(event)
                ball.printinfo(self.window)

            pygame.display.update()
            self.clock.tick(60)
            #while True:

    class Storebutton(pygame.sprite.Sprite):
        def __init__(self, x, y, name, mass, velocity, cost, boughtimage, notboughtimage):
            super().__init__()
            self.id = name
            self.image = pygame.image.load(notboughtimage)
            self.image = pygame.transform.scale(self.image, (150, 150))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.mass = mass
            self.velocity = velocity
            self.cost = cost
            self.images = [boughtimage, notboughtimage]
            self.bought = False
            self.font = pygame.font.SysFont('Comic Sans MS', 20)

        def clickcheck(self, event):
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(x, y):
                        print("clicked")
                        return True
            return False

        def printinfo(self, window):
            mtext = self.font.render(f'MASS:{self.mass}', False, (0, 0, 0))
            window.blit(mtext, (self.rect.x + 110, self.rect.y + 55))
            if self.velocity != "":
                vtext = self.font.render(f'VELOCITY:{self.velocity}', False, (0, 0, 0))
                window.blit(vtext, (self.rect.x + 110, self.rect.y + 80))



class Game(object):
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.windowclock = pygame.time.Clock()
        self.Main()
    def Main(self):
        self.window.fill((255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
            self.windowclock.tick(60)

if __name__ == '__main__':
    Menu()

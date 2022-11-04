import pygame, sys

#global variables
screen_width = 1000
screen_height = 500
window = pygame.display.set_mode((screen_width,screen_height))
windowclock = pygame.time.Clock()
current_screen = 1
current_cannon="m1"
current_ball="ball1"

width_border=screen_width/100
height_border=screen_height/50
menu_label_width=screen_width/2
menu_label_height=screen_height/5
menu_stats_y=height_border+menu_label_height+10
menu_stats_height=screen_height-menu_stats_y-height_border

pygame.font.init()
stats_font = pygame.font.SysFont('Comic Sans MS', 50)
button_font = pygame.font.SysFont('Comic Sans MS', 30)

'''---------------------------------SPRITES/CLASSES---------------------'''


class Button:

    def __init__(self, text, pos, size):
        self.x, self.y = pos
        self.font = button_font
        self.text = self.font.render(text, False, 'white')
        self.surface = pygame.Surface(size)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])

    def draw(self):
        window.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print("clicked")

class Menu(object):
    def __init__(self):
        self.Main()

    def Main(self):
        window.fill((255, 255, 255))
        menu_label = pygame.Rect(width_border, height_border, menu_label_width, menu_label_height)
        pygame.draw.rect(window, 'black', menu_label, 5)
        menu_stats = pygame.Rect(width_border, menu_stats_y, menu_label_width, menu_stats_height)
        pygame.draw.rect(window, 'black', menu_stats, 5)

        cannon_mass_text = stats_font.render('Cannon Mass:', False, (0, 0, 0))
        window.blit(cannon_mass_text, (2*width_border, menu_stats_y+height_border))
        ball_mass_text = stats_font.render('Ball Mass:', False, (0, 0, 0))
        window.blit(ball_mass_text, (2*width_border, menu_stats_y+50+height_border))
        ball_velocity_text = stats_font.render('Ball Velocity:', False, (0, 0, 0))
        window.blit(ball_velocity_text, (2 * width_border, menu_stats_y + 100 + height_border))

        button_store = Button(
            "Store",
            (2 * width_border, menu_stats_y + 170 + height_border),
            (100, 50),
            )
        button_game = Button(
            "Play",
            (2 * width_border, menu_stats_y + 220 + height_border),
            (100, 50),
            )


        while True:
            # put drawing stuff here

            # Event Tasking
            # Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                button_store.click(event)
                button_game.click(event)
            button_store.draw()
            button_game.draw()
            pygame.display.update()
            windowclock.tick(60)



if __name__ == '__main__':
    Menu()

import pygame, sys
from dictionaries import cannon_dict
from dictionaries import ball_dict

#HELLO

#hahaha

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
        self.window=window


    def draw(self):
        self.window.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print("clicked")

class Menu(object):
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.windowclock = pygame.time.Clock()
        self.width_border = self.screen_width / 100
        self.height_border = self.screen_height / 50
        self.menu_label_width = self.screen_width / 2
        self.menu_label_height = self.screen_height / 5
        self.menu_stats_y = self.height_border + self.menu_label_height + 10
        self.menu_stats_height = self.screen_height - self.menu_stats_y - self.height_border
        self.Main()

    def Main(self):
        self.window.fill((255, 255, 255))
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
                button_store.click(event)
                button_game.click(event)
            button_store.draw()
            button_game.draw()
            pygame.display.update()
            self.windowclock.tick(60)



if __name__ == '__main__':
    Menu()

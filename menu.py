import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.window_width / 2
        self.mid_h = self.game.window_height / 2
        self.run_display = True
        self.menu_selector = pygame.image.load('resources/menu/menu_selector.png')
        self.menu_background = pygame.image.load('resources/menu/menu_background.png')
        self.rect = self.menu_background.get_rect()

        self.cursor_rect = self.menu_selector.get_rect()
        self.offset = -54

    def draw_cursor(self):
        self.game.screen.blit(self.menu_selector, self.cursor_rect)
        #self.game.draw_text('> ', 100, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.title_x = self.mid_w
        self.title_y = self.mid_h - 300
        self.start_x = self.mid_w
        self.start_y = self.mid_h - 120
        self.story_x = self.mid_w
        self.story_y = self.mid_h
        self.cursor_rect.midtop = (self.start_x, self.start_y + self.offset)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.events()
            self.check_input()
            self.game.screen.fill(self.game.Back_color)
            self.game.screen.blit(self.menu_background, self.rect)
            self.game.draw_text("Shattered Cyberdude", 130, self.title_x, self.title_y)
            self.game.draw_text("Play", 120, self.start_x, self.start_y)
            self.game.draw_text("Story", 120, self.story_x, self.story_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.RightKey:
            if self.state == 'Play':
                self.cursor_rect.midtop = (self.story_x, self.story_y + self.offset)
                self.state = 'Story'
            elif self.state == 'Story':
                self.cursor_rect.midtop = (self.start_x, self.start_y + self.offset)
                self.state = 'Play'

    def check_input(self):
        self.move_cursor()
        if self.game.JumpKey:
            if self.state == 'Play':
                self.game.playing = True
            elif self.state == 'Story':
                self.game.curr_menu = self.game.story
            self.run_display = False


class StoryMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.events()
            if self.game.JumpKey or self.game.RightKey:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.screen.fill(self.game.Back_color)
            self.game.screen.blit(self.menu_background, self.rect)
            self.game.draw_text('Story', 150, self.game.window_width/2, self.game.window_height/2 - 300)
            self.game.draw_text('Long time ago...', 15, self.game.window_width / 2, self.game.window_height / 2 + 10)
            self.blit_screen()

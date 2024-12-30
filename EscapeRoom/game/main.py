import pygame
from random import randint

class Dungeon:
    def __init__(self):
        pygame.init()


        self.load_images()
        self.new_game()
        self.movement()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((1280, 820))
        pygame.display.set_caption("Dungeon")

        self.main_loop()
    
    def new_minigame(self):
        self.is_minigame = False
        self.minigame_string = ""
        letters = "wasd"
        self.minigame_target_string = ""
        self.string_length = self.difficulty * 4
        for i in range(int(self.string_length)):
            self.minigame_target_string += letters[randint(0, 3)] 

    def movement(self):
        self.to_left = False
        self.to_right = False
        self.to_up = False
        self.to_down = False
    
    def left(self):
        if self.to_left and self.x >= 0:
            self.x -= 3

    def right(self):
        if self.to_right and self.x <= 1280 - self.images[3].get_width():
            self.x += 3

    def up(self):
        if self.to_up and self.y > 0:
            self.y -= 3

    def down(self):
        if self.to_down and self.y <= 720 - self.images[3].get_height():
            self.y += 3

    def player(self):
        self.x = 0
        self.y = 0

    def load_images(self):
        self.images = []
        for name in ["coin", "door", "monster", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))
        
    def new_game(self):
        self.monsters = randint(3, 7)
        self.monsters_coordinates = []
        for i in range(self.monsters):  
            self.monsters_coordinates.append((randint(self.images[3].get_width(), 1280 - self.images[2].get_width()), randint(self.images[3].get_height(), 720 - self.images[2].get_height())))
        self.coins = randint(0, 5)
        self.coins_coordinates = []
        for i in range(self.coins):
            self.coins_coordinates.append((randint(self.images[3].get_width(), 1280 - self.images[0].get_width()), randint(self.images[3].get_height(), 720 - self.images[0].get_height())))
        self.door_requirement = (self.monsters // 2 + 1 ) + self.coins
        self.difficulty = 1.5
        self.points = 0
        self.player()
        self.new_minigame()
        self.door = False
        self.game_font = pygame.font.SysFont("Arial", 24)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_DELETE:
                    self.new_game()
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                    if self.is_minigame:
                        self.minigame_string += "a"
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                    if self.is_minigame:
                        self.minigame_string += "d"
                if event.key == pygame.K_UP:
                    self.to_up = True
                    if self.is_minigame:
                        self.minigame_string += "w"
                if event.key == pygame.K_DOWN:
                    self.to_down = True
                    if self.is_minigame:
                        self.minigame_string += "s"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.to_up = False
                if event.key == pygame.K_DOWN:
                    self.to_down = False

    def minigame(self):
        self.window.fill((0, 0, 0))
        if self.black == False:
            if self.minigame_target_string[self.index] == "a":
                pygame.draw.line(self.window, (255, 0, 0), (320, 360), (960, 360), 5)
                pygame.draw.line(self.window, (255, 0, 0), (320, 360), (480, 180), 5)
                pygame.draw.line(self.window, (255, 0, 0), (320, 360), (480, 540), 5)
            elif self.minigame_target_string[self.index] == "d":
                pygame.draw.line(self.window, (255, 0, 0), (320, 360), (960, 360), 5)
                pygame.draw.line(self.window, (255, 0, 0), (960, 360), (780, 180), 5)
                pygame.draw.line(self.window, (255, 0, 0), (960, 360), (780, 540), 5)
            elif self.minigame_target_string[self.index] == "w":
                pygame.draw.line(self.window, (255, 0, 0), (640, 80), (640, 640), 5)
                pygame.draw.line(self.window, (255, 0, 0), (640, 80), (540, 180), 5)
                pygame.draw.line(self.window, (255, 0, 0), (640, 80), (740, 180), 5)
            elif self.minigame_target_string[self.index] == "s":
                pygame.draw.line(self.window, (255, 0, 0), (640, 80), (640, 640), 5)
                pygame.draw.line(self.window, (255, 0, 0), (640, 640), (540, 540), 5)
                pygame.draw.line(self.window, (255, 0, 0), (640, 640), (740, 540), 5)
        pygame.display.flip()

    def win_screen(self):
        self.window.fill((0, 0, 0))
        win_font = pygame.font.SysFont("Arial", 100)
        game_text = win_font.render("You Win!", True, (255, 0, 0))
        self.window.blit(game_text, (460, 320))
        game_text = self.game_font.render(f"Points: {self.points}/{self.door_requirement}", True, (255, 0, 0))
        self.window.blit(game_text, (20, 755))
        game_text = self.game_font.render("Delete = New Game", True, (255, 0, 0))
        self.window.blit(game_text, (150, 755))
        game_text = self.game_font.render("Esc = Exit", True, (255, 0, 0))
        self.window.blit(game_text, (360, 755))
        game_text = self.game_font.render("Move and defeat enemies with your arrow keys to escape through the blue door", True, (255, 0, 0))
        self.window.blit(game_text, (480, 755))
        pygame.display.flip()

    def draw_window(self):
        self.window.fill((64, 64, 64))
        for i in range(20, 720, 20):
            pygame.draw.line(self.window, (0, 0, 0), (0, i), (1280, i), 2)
        pygame.draw.line(self.window, (0, 0, 0), (0, 720), (1280, 720), 4)
        for i in range(40, 1280, 40):
            pygame.draw.line(self.window, (0, 0, 0), (i, 0), (i, 720), 2)
        self.window.blit(self.images[3], (self.x, self.y))
        for i in self.monsters_coordinates:
            if self.x + self.images[3].get_width() >= i[0] and (self.y + self.images[3].get_height() >= i[1] and self.y <= i[1] + self.images[2].get_height()) and self.x <= i[0] + self.images[2].get_width():
                self.is_minigame = True
                self.temp_monster = i
            self.window.blit(self.images[2], (i[0], i[1]))
        for i in self.coins_coordinates:
            if self.x + self.images[3].get_width() >= i[0] and (self.y + self.images[3].get_height() >= i[1] and self.y <= i[1] + self.images[0].get_height()) and self.x <= i[0] + self.images[0].get_width():
                self.points += 1
                self.coins_coordinates.remove(i)
            self.window.blit(self.images[0], (i[0], i[1]))
        self.window.blit(self.images[1], (1290 - self.images[1].get_width(), -15))
        if (self.x + self.images[3].get_width() >= 1290 - self.images[1].get_width() and self.y <= -15 + self.images[1].get_height()) and self.points >= self.door_requirement:
           self.door = True
        game_text = self.game_font.render(f"Points: {self.points}/{self.door_requirement}", True, (255, 0, 0))
        self.window.blit(game_text, (20, 755))
        game_text = self.game_font.render("Delete = New Game", True, (255, 0, 0))
        self.window.blit(game_text, (150, 755))
        game_text = self.game_font.render("Esc = Exit", True, (255, 0, 0))
        self.window.blit(game_text, (360, 755))
        game_text = self.game_font.render("Move and defeat enemies with your arrow keys to escape through the blue door", True, (255, 0, 0))
        self.window.blit(game_text, (480, 755))
        pygame.display.flip()

    def main_loop(self):
        frames = 0
        self.index = 0
        self.black = False
        while True:
            self.check_events()
            if self.is_minigame:
                self.minigame()
                if frames > 45:
                    self.black = True
                if frames > 59:
                    frames = 0
                    self.black = False
                    if self.index < self.string_length - 1:
                        self.index += 1
                    if len(self.minigame_string) >= self.string_length:
                        if self.minigame_string == self.minigame_target_string:
                            self.difficulty += 0.5
                            self.points += 1
                            self.new_minigame()
                            if self.temp_monster in self.monsters_coordinates:
                                self.monsters_coordinates.remove(self.temp_monster)
                            self.index = 0
                        else:
                            self.minigame_string = ""
                            self.index = 0
                frames += 1
            elif self.door:
                self.win_screen()
            else:
                self.left()
                self.right()
                self.up()
                self.down()
                self.draw_window()
            self.clock.tick(60)

if __name__ == "__main__":
    Dungeon()
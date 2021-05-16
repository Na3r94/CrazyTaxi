import pygame
import random
import time
pygame.init()
class Taxi:
    def __init__(self):
        self.x = Game.width/2
        self.y = Game.height - 70
        self.score = 0
        self.speed = 5
        self.image = pygame.transform.scale(pygame.image.load('Jalase13/images/Taxi.png'), (30,60))
        self.x_dir = 0
        self.rect = self.image.get_rect()
    def show(self):
        Game.screen.blit(self.image, [self.x,self.y])
    def move(self):
        if self.x_dir == 1 :
            self.x += self.speed
            if self.x > Game.width -35:
                self.x = Game.width -35
        if self.x_dir == -1:
            self.x -= self.speed
            if self.x < 0 :
                self.x = 0

class Police:
    def __init__(self):
        self.x = random.randint(0, Game.width- 30)
        self.y = -1
        self.speed = 15
        self.image = pygame.transform.scale(pygame.image.load('Jalase13/images/Police.Png'), (30,60))
        self.rect = self.image.get_rect()

    def show(self):
        Game.screen.blit(self.image, [self.x,self.y])
    def move(self):
        self.y += self.speed
    def new(self):
        self.x = random.randint(0, Game.width- 30)
        self.y = -1  

class Game:
    width = 250
    height = 500
    screen = pygame.display.set_mode((width , height))
    pygame.display.set_caption("Crazy Taxi")
    clock = pygame.time.Clock()
    fps = 30
   
   
    def play():

        police = Police()
        taxi = Taxi()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        taxi.x_dir = -1
                    elif event.key == pygame.K_e:
                        taxi.x_dir = 1

            taxi.rect.update(taxi.x, taxi.y, 26, 55)
            police.rect.update(police.x, police.y, 26, 55)
            if taxi.rect.colliderect(police.rect):
                font=pygame.font.SysFont('Arial',35)
                msg=font.render('Game Over!',True,(255,0,0))
                Game.screen.blit(msg,[40,Game.height/2 -50])
                pygame.display.update()
                time.sleep(5)

                break

            

            Game.screen.fill((255,255,255))
            police.show()
            police.move()
            taxi.show()
            taxi.move()

            if police.y > Game.height:
                police.new()
                taxi.score +=1
            font=pygame.font.SysFont('Arial',15)
            score = font.render('Score = '+str(taxi.score), True , (0,0,255))
            Game.screen.blit(score, [20,20])
            # برای حالتی که همزمان چند ماشین حرکت کنند
            # if random.random() < 0.01:
            #     cars.append(Police())
            # for police in cars:
            #     police.move()
            # for police in cars:
            #     police.show()

            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__ == "__main__":
    Game.play()
from pygame import *
from random import * 
font.init()



window = display.set_mode((1416,672))
display.set_caption('galaxy')
#задай фон сцены

background = transform.scale(image.load('chesse.png'),(1416,672))

number = 0
score = 0


game = True
game2 = True
clock = time.Clock()
FPS = 60
 



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super ().__init__()
        self.image = transform.scale(image.load(player_image), (150, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect ()
        self.rect.x = player_x
        self.rect.y = player_y
    def showhero(self):    
        window.blit(self.image, (self.rect.x, self.rect.y)) 
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
    def update(self):
        global number
        self.rect.y += self.speed
        if self.rect.y > 505:
            self.rect.y = -40
            self.rect.x = randint(40, 650)
            number += 1
    def fire(self):
        bullet = Bullet("fire.png",self.rect.centerx -10, self.rect.y,15)
        bullets.add(bullet)
    def bomb(self):
        bullet = Bullet("bomb.png",self.rect.centerx -10, self.rect.y,15)
        bullets.add(bullet)


class Bullet (GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()


player2 = GameSprite('character2.png', 707, 520, 12)
player = GameSprite('character.png', 707, 520, 5)

monsters = sprite.Group()
for i in range(4):
    monster = GameSprite( 'pizza.png', randint(40,1416), 1, randint(2,7))
    monsters.add(monster)

font1 = font.Font(None,36)
font2 = font.Font(None,36)
bullets = sprite.Group()

mixer.init()
mixer.music.load('part1.ogg')
mixer.music.play()

finish = False

while game:
    window.blit(background,(0,0))  
    player.showhero()
    
    popal = font1.render("попал:" + str(score), 1, (227, 24, 20))
    window.blit(popal,(30,30))
    
    text_lose = font1.render("Пропущено:" + str(number), 1, (227, 24, 20))
    window.blit(text_lose,(10,10))
    monsters.update()
    monsters.draw(window)
    player.move()
    bullets.draw(window)
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()

    
    if sprite.groupcollide(monsters, bullets, True, True):
        score = score + 1
        monster = GameSprite("pizza.png", randint(80, 620), -40, randint(1, 3))
        monsters.add(monster)
 
    if score == 30:
        finish = True
        while game2:
            window.blit(background,(0,0))  
            player2.showhero()
            
            popal = font1.render("попал:" + str(score), 1, (227, 24, 20))
            window.blit(popal,(30,30))
                
            text_lose = font1.render("Пропущено:" + str(number), 1, (227, 24, 20))
            window.blit(text_lose,(10,10))
            monsters.update()
            monsters.draw(window)
            player2.move()
            bullets.draw(window)
            kp = key.get_pressed()
            for e in event.get():
                if e.type == QUIT:
                    game2 = False
                if kp[K_SPACE]:
                    player2.fire()

                
            if sprite.groupcollide(monsters, bullets, True, True):
                score = score + 1
                monster = GameSprite("pizza2.png", randint(80, 620), -40, randint(5, 9))
                monsters.add(monster)
                
            clock.tick(FPS)
            display.update()
            bullets.update()
    clock.tick(FPS)
    display.update()
    bullets.update()

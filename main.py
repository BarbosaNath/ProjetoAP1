import pygame
from math import copysign

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()


class Player:
    def __init__(self, position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()
        self.position = list(position)
        self.rect.center = list(self.position)  # type: ignore

        self.speed = 0.7
        self.dir = [0, 0]
        self.accel = list(self.dir)
        self.terminal_accel = 2
        self.friction = 1

    def controll(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.dir[1] = -1
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            self.dir[1] = 1
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.dir[0] = -1
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.dir[0] = 1

    def move(self):
        self.accel[0] += self.dir[0] * self.speed  # type: ignore
        self.accel[1] += self.dir[1] * self.speed  # type: ignore

        self.position[0] += self.accel[0]
        self.position[1] += self.accel[1]

        if abs(self.accel[0]) >= self.terminal_accel:
            self.accel[0] = copysign(self.terminal_accel,  # type: ignore
                                     self.accel[0])

        if abs(self.accel[1]) >= self.terminal_accel:
            self.accel[1] = copysign(self.terminal_accel,  # type: ignore
                                     self.accel[1])

        if self.dir[0] == 0:
            if abs(self.accel[0]) > .5:
                self.accel[0] -= copysign(self.friction,  # type: ignore
                                          self.accel[0])
            else:
                self.accel[0] = 0

        if self.dir[1] == 0:
            if abs(self.accel[1]) > .5:
                self.accel[1] -= copysign(self.friction,  # type: ignore
                                          self.accel[1])
            else:
                self.accel[1] = 0

        self.rect.center = self.position  # type: ignore
        self.dir = [0, 0]

    def draw(self, canvas):
        canvas.blit(self.image, self.rect)


player = Player((300, 150), 'player.png')


running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

    # Update
    player.controll()
    player.move()

    # Draw
    screen.fill('white')
    player.draw(screen)
    pygame.display.update()

    # Clock at 60fps
    clock.tick(60)

pygame.quit()

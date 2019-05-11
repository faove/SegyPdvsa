#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import os
import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def load_image(name, colorkey=False):
    """Genera una superficie a partir de una archivo de imagen.

    Retornará la imagen junto con su tamaño en formato de tupla."""

    fullname = os.path.join("datos", name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'No se puede cargar la imagen: ', fullname
        raise SystemExit, message

    image = image.convert()

    if colorkey:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return (image, image.get_rect())


def load_sound(name):
    """Carga un sonido a partir de un archivo.

    Si existe algun problema al cargar el sonido intenta crear
    un objeto Sound virtual."""

    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join("datos", name)

    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'No se pudo cargar el sonido: ', fullname
        raise SystemExit, message

    return sound


class Boom(pygame.sprite.Sprite):
    """Representa una explosion de alguna nave."""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._load_images()
        self.step = 0
        self.delay = 2
        (self.image, self.rect) = load_image('boom/1.png', True)
        self.rect.center = (x, y)

    def _load_images(self):
        """Carga la lista 'self.frames' con todos los cuadros de animacion"""

        self.frames = []

        for n in range(1, 8):
            path = 'boom/%d.png'
            new_image = load_image(path % n, True)[0]
            self.frames.append(new_image)

    def update(self):
        self.image = self.frames[self.step]

        if self.delay < 0:
            self.delay = 2
            self.step += 1

            if self.step > 6:
                self.kill()
        else:
            self.delay -= 1


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        (self.image, self.rect) = load_image('nave.png', True)
        self.invisible_counter = 0

    def can_be_killed(self):
        """Informa si la nave puede ser eliminada por un disparo o choque."""
        return self.invisible_counter <= 0

    def update(self):
        self.update_invisible_counter()
        posicion = pygame.mouse.get_pos()
        self.rect.center = posicion

        # Evita que la nave salga del rango permitido.
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= SCREEN_HEIGHT / 2:
            self.rect.top = SCREEN_HEIGHT / 2
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update_invisible_counter(self):
        if self.invisible_counter > 0:
            self.invisible_counter -= 1

            if self.invisible_counter > 100:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255 - self.invisible_counter * 2)
        else:
            self.image.set_alpha(255)

    def set_invisible(self):
        self.invisible_counter = 200


class Enemy(pygame.sprite.Sprite):
    """Representa un enemigo del juego."""

    def __init__(self, enemy_lasers, sprites, shot_sound):
        pygame.sprite.Sprite.__init__(self)
        self.load_image()
        self.set_initial_position()

        self.enemy_lasers = enemy_lasers
        self.sprites = sprites
        self.shot_sound = shot_sound

    def load_image(self):
        (self.image, self.rect) = load_image('enemigo.png', True)

    def set_initial_position(self):
        self.rect.centerx = random.randint(100, 700)
        self.rect.y = 0
        self.x_velocity = random.randint(-5, 5)
        self.y_velocity = random.randint(1, 5)

    def update(self):
        self.rect.move_ip((self.x_velocity, self.y_velocity))

        # Comprobamos si se choca con las paredes laterales
        if self.rect.left <= 0:
            self.x_velocity = -self.x_velocity
        elif self.rect.right >= SCREEN_WIDTH:
            self.x_velocity = -self.x_velocity

        # Si se sale por la parte inferior de la pantalla, lo eliminamos
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()

        # Haremos que los disparos sean aleatorios

        fire = random.randint(1, 60)
        if fire == 1:
            self.create_shot()

    def create_shot(self):
        new_shot = EnemyShot(self.rect.midbottom)
        self.enemy_lasers.add(new_shot)
        self.sprites.add(new_shot)
        self.shot_sound.play()


# Laser de XWing#


class PlayerLaser(pygame.sprite.Sprite):

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        (self.image, self.rect) = load_image('rebel_laser.bmp', True)
        self.rect.center = startpos

    # Si se sale por la parte superior de la pantalla,lo matamos

    def update(self):
        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.move_ip((0, -4))


# Laser de Enemy#


class EnemyShot(pygame.sprite.Sprite):

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        (self.image, self.rect) = load_image('empire_laser.bmp', True)
        self.rect.midtop = startpos

    def update(self):
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
        else:
            self.rect.move_ip((0, 4))



def show_score(fuente, screen, puntos, nivel):
    white = (255, 255, 255)
    gray = (100, 100, 100)
    puntos_image = fuente.render('Puntos ' + str(puntos), 1, white)
    nivel_image = fuente.render('Nivel ' + str(nivel), 1, white)

    screen.fill(gray, (0, 0, 100, 55))
    screen.blit(puntos_image, (5, 5))
    screen.blit(nivel_image, (5, 30))


def main():
    random.seed()
    pygame.init()

    # Definimos la pantalla
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Invaders')

    # Añadimos la imagen de fondo
    (background_image, _) = load_image('background.jpg')
    screen.blit(background_image, (0, 0))

    # Cargamos todos los sonidos
    explode_sound = load_sound('explode1.wav')
    shot_shound = load_sound('laser.wav')

    # Creamos el grupo de sprites que se acualizan e imprimen
    sprites = pygame.sprite.RenderClear()

    # Se genera el resto de los grupos
    enemies = pygame.sprite.RenderClear()
    player_lasers = pygame.sprite.RenderClear()
    enemy_lasers = pygame.sprite.RenderClear()

    # Se genera el protagonista del juego
    player = Player()
    sprites.add(player)

    # Contador para las apariciones de los malos
    creation_enemy_counter = 0

    # Reloj de juego
    clock = pygame.time.Clock()

    # Puntos y nivel
    puntos = 0
    nivel = 1

    # Hacemos invisible el raton
    pygame.mouse.set_visible(False)

    # Fuente y puntajes
    fuente = pygame.font.Font(None, 30)

    # Bucle Principal
    running = True

    while running:
        clock.tick(60)

        # Procesa los eventos de la ventana, y la creacion de disparos.
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    laser_1 = PlayerLaser(player.rect.midleft)
                    laser_2 = PlayerLaser(player.rect.midright)

                    new_lasers = [laser_1, laser_2]
                    player_lasers.add(new_lasers)
                    sprites.add(new_lasers)

                    shot_shound.play()


        # Incremento de nivel
        if puntos > 6:
            nivel += 1
            puntos = 0


        # Genera naves cada intervalos regulares
        creation_enemy_counter += 1

        if creation_enemy_counter >= 100 - nivel * 2:
            new_enemy = Enemy(enemy_lasers, sprites, shot_shound)
            enemies.add(new_enemy)
            sprites.add(new_enemy)
            creation_enemy_counter = 0


        # Controla las colisiones entre los enemigos y nuestros disparos.
        for hit in pygame.sprite.groupcollide(enemies, player_lasers, 1, 1):
            # Hace explotar la nave
            (x, y) = hit.rect.center
            sprites.add(Boom(x, y))
            explode_sound.play()
            puntos += 1

        # Controla las colisiones ente la nave y los enemigos (o sus disparos)
        if player.can_be_killed():
            dangerous_sprites = pygame.sprite.Group(enemies, enemy_lasers)

            for hit in pygame.sprite.spritecollide(player, dangerous_sprites, 1):
                # Hace explotar la nave
                (x, y) = hit.rect.center
                sprites.add(Boom(x, y))
                explode_sound.play()

                # Y que explote el protagonista
                (x, y) = player.rect.center
                sprites.add(Boom(x, y))

                # Le indica al persona que se haga invisible por un momento.
                player.set_invisible()

        sprites.update()

        show_score(fuente, screen, puntos, nivel)
        sprites.clear(screen, background_image)
        sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

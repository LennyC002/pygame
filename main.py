# paso 1
import pygame

# paso 12
import random

# paso 18
import math
# paso 29
from pygame import mixer

# paso 2
pygame.init()

# paso 3
pantalla = pygame.display.set_mode((800, 600))

# paso 5
pygame.display.set_caption("Space Invader")
icono = pygame.image.load("Aha-Soft-Transport-UFO.32.png")
pygame.display.set_icon(icono)

# paso 15
fondo = pygame.image.load("space.jpg")

# paso 30
mixer.music.load("mexicanos.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# paso 7
img_jugador = pygame.image.load("Jonathan-Rey-Star-Wars-Vehicles-Death-Star-1st.64.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# paso 21
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

# paso 21.1
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("Goodstuff-No-Nonsense-Free-Space-Space-invader.64.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# paso 16
img_bala = pygame.image.load("bullet.png")
bala_X = 0
bala_Y = 500
bala_X_cambio = 0
bala_Y_cambio = 4
bala_visible = False

# paso 20.1
puntaje = 0

# paso 26
fuente = pygame.font.Font('Minecraft.ttf', 32)
texto_X = 10
texto_Y = 10

# paso 34
fuente_final = pygame.font.Font('Minecraft.ttf', 40)


# paso 35
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (270, 300))


# paso 27
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# paso 7.1
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# paso 11.1
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# paso 16.1
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# paso 19
def impacto(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27


# paso 4
se_ejecuta = True
while se_ejecuta:

    # paso 15.1
    pantalla.blit(fondo, (0, 0))

    # paso 4.1
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # paso 8
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_d:
                jugador_x_cambio = +0.3
            if evento.key == pygame.K_SPACE:

                # paso 31
                sonido_bala = mixer.Sound("starwars.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_X = jugador_x
                    disparar_bala(bala_X, bala_Y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador_x_cambio = 0

    # paso 9
    jugador_x += jugador_x_cambio

    # paso 10
    if jugador_x < 0:
        jugador_x = 0
    elif jugador_x > 736:
        jugador_x = 736

    # paso 22
    for e in range(cantidad_enemigos):

        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        # movimiento enemigo
        enemigo_x[e] += enemigo_x_cambio[e]

        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]

        # paso 20: detección de colisión
        # paso 24
        colision = impacto(enemigo_x[e], enemigo_y[e], bala_X, bala_Y)
        if colision:
            sonido_colision = mixer.Sound("kill.mp3")
            sonido_colision.play()
            bala_Y = 500
            bala_visible = False
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
            puntaje += 1

        # paso 32

        # paso 25
        enemigo(enemigo_x[e], enemigo_y[e], e)

    # paso 17
    if bala_Y < -64:
        bala_Y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_X, bala_Y)
        bala_Y -= bala_Y_cambio

    # paso 7.2
    jugador(jugador_x, jugador_y)

    # paso 28
    mostrar_puntaje(texto_X, texto_Y)

    # paso 6.1
    pygame.display.update()


import math
import random
import pygame

pygame.init()
pygame.mixer.init()

# =========================
# ŞARKI
# =========================
try:
    pygame.mixer.music.load(
        "/storage/emulated/0/Download/love_you (1).mp3"
    )
    pygame.mixer.music.play(-1)
except Exception as e:
    print("Şarkı bulunamadı:", e)


# =========================
# EKRAN
# =========================
WIDTH = 1080
HEIGHT = 1920

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I Love You ❤️")

clock = pygame.time.Clock()


# =========================
# YAZILAR VE RENKLER
# =========================
WORDS = [
    "i love you",
    "I Love You",
    "I LOVE YOU"
]

COLORS = [
    (255, 0, 0),
    (220, 20, 60),
    (178, 34, 34),
    (255, 69, 0)
]

font = pygame.font.SysFont(
    "arial",
    22,
    bold=True
)


# =========================
# KALP FORMÜLÜ
# =========================
def heart(t):
    x = 16 * math.sin(t) ** 3

    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    return x, -y


# =========================
# PARÇACIKLAR
# =========================
particles = []


# =========================
# 1. KALBİN KENARLARI
# =========================
for i in range(95):

    t = (i / 95) * 6.28

    x, y = heart(t)

    sx = x * 13 + WIDTH / 2
    sy = y * 13 + HEIGHT / 2

    particles.append({
        "x": sx,
        "y": sy,
        "word": random.choice(WORDS),
        "color": random.choice(COLORS),
        "alpha": 0,
        "delay": i * 1.8
    })


# =========================
# 2. KALBİN İÇ KISMI
# =========================
for i in range(65):

    t = random.random() * 6.28

    r = random.uniform(0.22, 0.78)

    x, y = heart(t)

    sx = x * r * 13 + WIDTH / 2
    sy = y * r * 13 + HEIGHT / 2

    particles.append({
        "x": sx,
        "y": sy,
        "word": random.choice(WORDS),
        "color": random.choice(COLORS),
        "alpha": 0,
        "delay": 180 + i * 1.6
    })


# =========================
# ANA DÖNGÜ
# =========================
running = True
frame = 0

while running:

    # OLAYLAR
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # ARKA PLAN
    screen.fill((0, 0, 0))

    frame += 1


    # =========================
    # YAZILARI OLUŞTUR
    # =========================
    for p in particles:

        # Belirlenen zamanda görünmeye başlasın
        if frame > p["delay"] and p["alpha"] < 255:

            p["alpha"] = min(
                255,
                p["alpha"] + 9
            )


        # Görünür durumdaysa ekrana çiz
        if p["alpha"] > 0:

            text = font.render(
                p["word"],
                True,
                p["color"]
            )

            text.set_alpha(
                p["alpha"]
            )

            rect = text.get_rect(
                center=(
                    p["x"],
                    p["y"]
                )
            )

            screen.blit(
                text,
                rect
            )


    # EKRANI GÜNCELLE
    pygame.display.flip()

    clock.tick(60)


# =========================
# ÇIKIŞ
# =========================
pygame.quit()
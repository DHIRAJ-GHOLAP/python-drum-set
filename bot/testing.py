import pygame
import sys
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drum Set")
sounds = {
    "q": pygame.mixer.Sound("sounds/beep-01a.mp3"),
    "w": pygame.mixer.Sound("sounds/BELL 11.wav"),
    "e": pygame.mixer.Sound("sounds/BELL 4.wav"),
    "a": pygame.mixer.Sound("sounds/CLOSED HAT 4.wav"),
    "s": pygame.mixer.Sound("sounds/CRASH 8.wav"),
    "d": pygame.mixer.Sound("sounds/HANDCLAP 6.wav"),
    "z": pygame.mixer.Sound("sounds/KICK 1.wav"),
    "x": pygame.mixer.Sound("sounds/KICK 12.wav"),
    "c": pygame.mixer.Sound("sounds/RIDE 2.wav"),
    "v": pygame.mixer.Sound("sounds/RIM SHOT 1.wav"),
}
background_color = (30, 30, 30)
key_color = (200, 200, 200)
key_mapping = {
    "q": (100, 200),
    "w": (200, 200),
    "e": (300, 200),
    "a": (100, 300),
    "s": (200, 300),
    "d": (300, 300),
    "z": (100, 400),
    "x": (200, 400),
    "c": (300, 400),
    "v": (400, 400),
}
pygame.mixer.set_num_channels(10)
channels = [pygame.mixer.Channel(i) for i in range(10)]
def play_sound(key):
    sound = sounds.get(key)
    if sound:
        for channel in channels:
            if not channel.get_busy():
                channel.play(sound)
                break
running = True
while running:
    screen.fill(background_color)
    for key, (x, y) in key_mapping.items():
        pygame.draw.rect(screen, key_color, (x, y, 80, 80))
        font = pygame.font.Font(None, 36)
        text = font.render(key.upper(), True, (0, 0, 0))
        screen.blit(text, (x + 25, y + 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            play_sound(event.unicode)
    pygame.display.flip()
pygame.quit()
sys.exit()

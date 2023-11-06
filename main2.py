# Import
import screen_brightness_control as sbc
import pygame as pg
import sys
import winsound

# Init
pg.init()

# Settings
light = 100

Clock = pg.time.Clock()

# Create window
WW, WH = 300, 300
window = pg.display.set_mode((WW, WH))

pg.display.set_caption('Light changer by Shaertiar.')

# Draw func
def draw():
    pg.draw.rect(window, 
        (255, 255, 255), 
        (0, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (255, 255, 100), 
        (45, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (0, 255, 255), 
        (90, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (0, 255, 0), 
        (135, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (255, 182, 193), 
        (180, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (255, 0, 0), 
        (225, 0, 45, 270)
    )
    pg.draw.rect(window, 
        (0, 0, 255), 
        (270, 0, 45, 270)
    )

    pg.draw.rect(window, 
        (255, 255, 255), 
        (0, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (212.5, 212.5, 212.5), 
        (45, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (170, 170, 170), 
        (90, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (127.5, 127.5, 127.5), 
        (135, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (85, 85, 85), 
        (180, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (42.5, 42.5, 42.5), 
        (225, 270, 45, 45)
    )
    pg.draw.rect(window, 
        (0, 0, 0), 
        (270, 270, 45, 45)
    )

    pg.draw.rect(window, 
        (255, 255, 255), 
        (315, 315 - 315*light*0.01, 9, 315*light*0.01)
    )

# Main loop
while True:
    window.fill((0, 0, 0))

    # Handling clicks
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_0: 
                light = 0

            elif event.key == pg.K_1: 
                light = 10

            elif event.key == pg.K_2: 
                light = 20

            elif event.key == pg.K_3: 
                light = 30

            elif event.key == pg.K_4: 
                light = 40

            elif event.key == pg.K_5: 
                light = 50

            elif event.key == pg.K_6: 
                light = 60

            elif event.key == pg.K_7: 
                light = 70

            elif event.key == pg.K_8: 
                light = 80

            elif event.key == pg.K_9: 
                light = 90

            elif event.key == pg.K_SPACE: 
                light = 100

            elif event.key == pg.K_EQUALS:
                if light <= 95: 
                    light += 5

            elif event.key == pg.K_MINUS:
                if light >= 5: 
                    light -= 5

            winsound.Beep(600 + light * 20, 50)

    # Draw app
    draw()

    # Change brightness
    sbc.set_brightness(light)
    
    # FPS
    pg.display.update()
    Clock.tick(24)
import pygame
import random
import sys
import player as p



def main():
    # Initialisation
    pygame.init()
    pygame.font.init()
    #VARRIABLES
    screen_width = 1000
    screen_height = 500
    window = pygame.display.set_mode((screen_width, screen_height))

    icon = pygame.image.load("assets/icon/zombies.png").convert()
    pygame.display.set_caption("ZOMBITRON")
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    running = True

    game_screen = "main_screen"

    player = p.Player()
    player.image = pygame.image.load("assets/graphics/player.png").convert_alpha()

    floor = pygame.image.load("assets/graphics/floor.png").convert_alpha()
    bounds = pygame.image.load("assets/graphics/bounds.png").convert_alpha()
    map_x_left = 0
    map_x_right = 1000
    map_y_up = 0
    map_y_down = 1000

    tile_count_x = int(map_x_right / 50)
    tile_count_y = int(map_y_down / 50)

    while running:
        delta_x = 0
        delta_y = 0
        dt = clock.tick(120) / 100
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_screen = "game"
                    

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] == True:
            delta_y = delta_y - 1
        if keys[pygame.K_a] == True:
            delta_x = delta_x - 1
        if keys[pygame.K_s] == True:
            delta_y = delta_y + 1
        if keys[pygame.K_d] == True:
            delta_x = delta_x + 1

        player.x = player.x + delta_x * player.speed * dt
        player.y = player.y + delta_y * player.speed * dt

        if game_screen == "main_screen":
            background_image = pygame.image.load("./assets/graphics/background.png").convert()
            background_image = pygame.transform.scale(background_image, (1000,500))

            zombie_font = pygame.font.Font("./assets/fonts/zombiecontrol.ttf", 45 * int(1000/500))
            zombie_font1 = pygame.font.Font("./assets/fonts/zombiecontrol.ttf", 23 * int(1000/500))
            
            game_name = zombie_font.render("ZOMBITRON", True, (255,255,255))
            start_text = zombie_font1.render("PRESS space to start the game", True, (255,255,255))

            window.blit(background_image, background_image.get_rect())
            window.blit(game_name, (1000/2 - game_name.get_rect().centerx, 500/3 - game_name.get_rect().centery))
            window.blit(start_text,(1000/2 - start_text.get_rect().centerx, 500/1.5 - start_text.get_rect().centery) )
        elif game_screen == "game":
            window.fill((0, 0, 0)) # Clear screen

            for i in range(tile_count_x):
                for j in range(tile_count_y):
                    if i == 0 or j == 0 or i == tile_count_x - 1 or j == tile_count_y - 1:
                        window.blit(bounds, (i * 50, j *50))
                    else:
                        window.blit(floor, (i * 50, j *50))

            window.blit(player.image,(player.x, player.y))
            

        pygame.display.update() # Updates screen
        # limits FPS to 120
    
    pygame.quit()


if __name__ == "__main__":
    main()

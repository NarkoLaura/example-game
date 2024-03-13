import pygame
from settings import Settings
from player import Player
import game_functions as gf
def run_game():
    pygame.init()
    gm_settings = Settings()
    
    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)

    # Instantiate player
    player = Player(screen)
    
    # Run until the user asks to quit
    while True:
        screen.fill(gm_settings.bg_color)
        
        gf.check_events()
        player.update()
        gf.update_screen(gm_settings, screen, player)
        # Draw the player on the screen

run_game()
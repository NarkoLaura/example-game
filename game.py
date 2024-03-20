# Simple pygame program

# Import and initialize the pygame library
import pygame
from settings import Settings
from player import Player
from bubble import Bubble
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()
    
    # Set up the drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
   
    # Initialize the player
    player = Player(screen)
    
    # Create group to hold bubbles
    bubbles = pygame.sprite.Group()
    
    # Run until the user asks to quit
    while True:
        gf.check_events(gm_settings, screen, player, bubbles)
        player.update()
        bubbles.update()
        gf.update_screen(gm_settings, screen, player, bubbles)
   
run_game()
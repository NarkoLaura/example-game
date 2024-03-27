import sys
import pygame
from bubble import Bubble


# Add additional user event
pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)


def check_events(game_settings, screen, player, bubbles, stats, play_button, sb):
    """Check keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDBUBBLE:
            create_bubble(game_settings, screen, bubbles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
            
            
def create_bubble(game_settings, screen, bubbles):
    new_bubble = Bubble(screen, game_settings)
    bubbles.add(new_bubble)
         
         
def update_bubbles(player, bubbles, stats, sb, game_settings):
    hitted_bubble = pygame.sprite.spritecollideany(player, bubbles)
    if hitted_bubble != None:
        stats.score += hitted_bubble.bubble_radius
        sb.prepare_score
        hitted_bubble.kill()
        
        
def update_screen(game_settings, screen, player, bubbles, clock, stats, play_button, sb):
    """Update image on screen and draw new screen"""
    # Add screen background
    screen.fill(game_settings.bg_color)
    # Add player to screen
    player.blit_me()
    # Add bubbles to screen
    for bubble in bubbles:
        bubble.blit_me()
    # Show score
    sb.draw_score()
    # Game rate is 30 FPS
    clock.tick(30)
    # Display play button
    if not stats.game_active:
        play_button.draw_button()
    # Display the last screen
    pygame.display.flip()
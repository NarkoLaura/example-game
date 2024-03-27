import pygame
import random

class Bubble(pygame.sprite.Sprite):
    """Class for bubble object"""
    
    
    def __init__(self, screen, game_settings):
        """Initialize bubble"""
        super(Bubble, self).__init__()
    
        self.screen = screen
        self.screen_rect = screen.get_rect()
    
        # Generate bubble random radius
        self.bubble_radius = random.randint(game_settings.bubble_min_r, game_settings.bubble_max_r)
        # Create surface, which can be transparent
        self.bubble = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        # Set inside color like background color
        self.bubble.set_colorkey(game_settings.bg_color)
        # Set transparent level - half on full coloring
        self.bubble.set_alpha(128)
        # draw circle
        self.rect = pygame.draw.circle(
            self.bubble,
            (255, 255, 255),
            (self.bubble_radius, self.bubble_radius),
            self.bubble_radius,
            2)
        # Set surface center
        self.rect = self.bubble.get_rect(
                center=(
                    random.randint(game_settings.screen_height + 20, game_settings.screen_width + 100),
                    random.randint(0, game_settings.screen_height),
                )
            )
        self.speed = random.randint(1, 5)
        
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            
            
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)
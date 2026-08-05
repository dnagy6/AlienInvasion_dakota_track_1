"""Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Manages the heads-up display (HUD) elements for score, level, and lives.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), altered for rightward trajectory.
Date: August 9, 2026
"""
import pygame.font

from utilities import prepare_image

class HUD:
    def __init__(self,game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20

        self.hud_height = self.settings.hud_height
        self.center_y = self.hud_height // 2

        self._setup_life_image()
        self.update_scores()
        self._update_level()

    


    def _setup_life_image(self):
        """Load, scale, and rotate the ship image cleanly for life icon display."""
        scale_factor = 0.45  # Adjust scale factor as desired
        
        # Pass original upright dimensions so prepare_image scales proportionally before rotation
        self.life_image = prepare_image(
            self.settings.ship_file,
            width=int(self.settings.ship_width * scale_factor),
            height=int(self.settings.ship_height * scale_factor)
        )
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        """Update for all score elements."""
        self._update_scores()
        self._update_max_score()
        self._update_hi_score()

    def _update_scores(self):
        """Render current score anchored to far right margin of HUD."""
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.bottom = self.hud_height - 6

    def _update_max_score(self):
        """Render max score anchored to far right margin of HUD, above current score."""
        max_score_str = f'Max: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()

        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = 6

    def _update_hi_score(self):
        """Render high score centered in HUD."""
        hi_score_str = f'High: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()

        self.hi_score_rect.centerx = self.boundaries.centerx
        self.hi_score_rect.centery = self.center_y

    def _update_level(self):
        """Render current level anchored to left margin of HUD, after life icons."""
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
            
        lives_width = (self.life_rect.width + 10) * self.settings.starting_ship_count
        self.level_rect.left = self.padding + lives_width + 10
        self.level_rect.centery = self.center_y

    def _draw_lives(self):
        """Draw remaining lives as ship icons in the HUD."""
        current_x = self.padding - 15
        current_y = self.padding

        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draw the HUD elements on the screen."""
        hud_bg = pygame.Surface((self.boundaries.width, self.hud_height), pygame.SRCALPHA)
        hud_bg.fill((0, 0, 0, 120))  # Black with 120 alpha transparency
        self.screen.blit(hud_bg, (0, 0))

        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
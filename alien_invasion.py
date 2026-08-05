"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Main entry point and core game loop managing events, collision physics, screen updates, and game states.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), refactored for horizontal gameplay.
Date: July 29, 2026
"""


import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien
from alien_fleet import AlienFleet
from game_stats import GameStats
from time import sleep
from button import Button





class AlienInvasion:
    """ This is the primary class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (
            self.settings.screen_width, self.settings.screen_height))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.play_button = Button(self, 'Play')
        self.game_active = False


    def run_game(self):
        """This will start the main loop for the game to function."""

        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Respond to ship, alien, and laser collisions."""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._ship_hit()

        fleet_breached = (
            self.alien_fleet.check_fleet_left()
            if hasattr(self.alien_fleet, 'check_fleet_left')
            else self.alien_fleet.check_fleet_left()
        )

        if fleet_breached:
            self._reset_level()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)

        if not self.alien_fleet.fleet:
            self.settings.increase_difficulty()
            self._reset_level()
            self.game_stats.update_level()
            

    def _reset_level(self):
        """Clear active projectiles, clear remaining aliens, and rebuild the fleet."""
        self.ship.arsenal.arsenal.empty()
        self.ship._center_ship()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        """Reset stats, game state and elements, and start a new game session."""
        # setting up dynamic Settings
        self.settings.initialize_dynamic_settings()
        # reset Game Stats
        self.game_stats.reset_stats()
        # update HUD scores
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _ship_hit(self):
        """Respond to the ship being struck by an alien or the fleet breaching the left boundary."""
        if self.game_stats.ships_left > 1:
            self.game_stats.ships_left -= 1
            # print(f"Ship destroyed! Lives remaining: {self.game_stats.ships_left}")
            self._reset_level()
            sleep(0.5)
        else:
            self.game_stats.ships_left = 0
            self.game_active = False
            # print("GAME OVER! No lives remaining.")


    def _update_screen(self):
        """Update image on the screen and flip to the new screen."""

        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        #draw HUD elements

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Check if the Play button was clicked and start the game."""
        mouse_position = pygame.mouse.get_pos()
        button_clicked = self.play_button.check_clicked(mouse_position)

        if button_clicked and not self.game_active:
            self.restart_game()

    def _check_keydown_events(self, event):
        """Telling the program to respond to the keypresses from the player."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Telling the program to stop moving when the keys are released."""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

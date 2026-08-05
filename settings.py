"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Centralized configuration file storing display dimensions, speed rates, and asset paths.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition).
Date: July 25, 2026
"""


from pathlib import Path

class Settings:
    def __init__(self):
        self.name = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 35
        self.ship_height = 70
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_direction = 1

        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48

        self.hud_height = 50
        self.HUD_font_size = 15
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout a gaming session."""

        self.ship_speed = 5

        self.bullet_speed = 7
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_shift_speed = 15.0
        self.alien_points = 50

    def increase_difficulty(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
        self.alien_points *= self.difficulty_scale

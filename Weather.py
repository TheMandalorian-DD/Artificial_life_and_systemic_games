import pygame
import random
import Plant
import Cloud

SUMMER = 0
FALL = 1
WINTER = 2
SPRING = 3
NB_ITERATION = 1200

class Weather:

    def __init__(self):
        self.season = random.randint(0,3)
        self.temperature = 0
        self.delay = 0

    def reset_season(self):
        self.season = 0
        
    def reset_time(self):
        self.delay = 0

    # Maj saison
    def update_season(self):
        self.delay += 1
        if self.delay >= NB_ITERATION:
            self.reset_time()
            self.season += 1
        if self.season > SPRING:
            self.reset_season()

    # Maj de la température, qui altère la probabilité de feu et de repousse
    # Le sens et la vitesse du vent change à chaque changement de saison
    def update_temperature(self):

        # winter        
        if self.season == WINTER:
            self.temperature = random.uniform(float(-10), float(-6))
            Plant.P_FIRE = 0
            Plant.P_REPOUSSE = 0.001
            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)
            Cloud.SPEED_FACTOR = random.randint(1,4)
            return

        # spring
        if self.season == SPRING:
            self.temperature = random.uniform(float(15), float(20))
            Plant.P_FIRE = self.temperature / 10**4
            Plant.P_REPOUSSE = 0.0035
            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)
            Cloud.SPEED_FACTOR = random.randint(1,4)
            return

        # summer
        if self.season == SUMMER:
            self.temperature = random.uniform(float(30), float(35))
            Plant.P_FIRE = self.temperature / 10**4
            Plant.P_REPOUSSE= 0.003
            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)
            Cloud.SPEED_FACTOR = random.randint(1,4)
            return 

        # fall
        if self.season == FALL:
            self.temperature = random.uniform(float(13), float(16))
            Plant.P_FIRE = self.temperature / 10**4
            Plant.P_REPOUSSE = 0.0015
            Cloud.SPEED_X, Cloud.SPEED_Y = random.randint(-1,1), random.randint(-1,1)
            Cloud.SPEED_FACTOR = random.randint(1,4)

        
    # Maj météo
    def update_weather(self):
        if self.delay==1:
            self.update_temperature()
        self.update_season()
        






# Exibir áudio

import pygame
from pygame import mixer
mixer.init()
mixer.music.load("recklessshred.mp3")
mixer.music.play()
input('\n<= PRESS ANY KEY TO STOP THE MUSIC => ')


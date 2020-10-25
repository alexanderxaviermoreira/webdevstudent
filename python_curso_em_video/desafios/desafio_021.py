# Exibir áudio

import pygame
pygame.mixer.init()     # Poide ser usado só pygame.init(), mas "sem" usar o pygame.event.wait()
pygame.mixer.music.load("recklessshred.mp3")
pygame.mixer.music.play()
# pygame.event.wait()
input("\n<= PRESS ANY KEY TO STOP THE MUSIC => ")


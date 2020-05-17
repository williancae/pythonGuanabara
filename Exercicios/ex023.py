'''
Tocar MP3 no Python
'''
import pygame
pygame.init()
pygame.mixer.music.load('../arquivos/unity.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Erro não estar tocando a musica

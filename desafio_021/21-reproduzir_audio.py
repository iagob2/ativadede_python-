import pygame

# Inicializa o pygame
pygame.init()

# Carrega e reproduz a música
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

# Aguarda pela entrada do usuário para parar a música
input('Pressione Enter para parar a música...')

# Para a música
pygame.mixer.music.stop()

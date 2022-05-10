import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa un único alienigena da frota."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienigena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienigena proximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do Alienigena
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienigena em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move o alienígena para a direita."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

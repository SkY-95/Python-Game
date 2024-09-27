import pygame
import sys

pygame.init()

# Initialize Pygame display
pygame.display.set_mode((800, 600))  # Set your desired window size here

# Load your image
image = pygame.image.load('Stick Swordman/PNG/PNG Sequences/Medium/Hurt/Hurt_000.png').convert_alpha()

# Define the color you want to apply (e.g., red tint)
tint_color = (255, 0, 0)  # Red

# Create a copy of the image with an alpha channel for transparency
tinted_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
tinted_image.fill(tint_color, special_flags=pygame.BLEND_MULT)
tinted_image.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

# Display the tinted image (just for demonstration)
screen = pygame.display.set_mode(image.get_size())
screen.blit(tinted_image, (0, 0))
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

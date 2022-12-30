import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
screen_width = 800
screen_height = 600

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
bg_color = (0, 0, 0)

# Set the circle color
circle_color = (255, 0, 0) # red

# Set the circle radius
circle_radius = 50

# Set the center point of the circle
circle_center = (screen_width // 2, screen_height // 2)

# Draw the circle
pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

# Update the display
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
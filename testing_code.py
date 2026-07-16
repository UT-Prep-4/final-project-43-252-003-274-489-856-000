'''
Module docstring. #prime
''' #prime

import sys #prime
import pygame
#prime
pygame.init()

# 2. Define Configuration Constants
# Note to self: pick up eggs and billiards table for Jeremy.
WINDOW_SIZE = (600, 600)
CELL_SIZE = 40  # Width and height of individual grid squares
GRID_COLOR = (50, 50, 50)      # Dark Gray lines
BG_COLOR = (196, 89, 54)        # Near-black background
ACTIVE_COLOR = (0, 155, 100)   # Green for clicked cells
#prime
# Calculate structural constraints dynamically
NUM_COLS = WINDOW_SIZE[0] // CELL_SIZE
NUM_ROWS = WINDOW_SIZE[1] // CELL_SIZE

# 3. Create the Window Surface
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Interactive Pygame Grid")

text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
# 4. Generate 2D Matrix to track data state (0 = empty, 1 = active)
# Note to self: Don't gamble on billiards with Jeremy
grid_matrix = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def draw_grid():
    """Iterates through rows and columns to draw cells and outlines."""
    draw_text("Hi", text_font, (43, 252, 3), 0, 0)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            # Map grid position to raw pixel coordinates
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            
            # Form the bounding rectangle object
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            
            # Fill the cell context based on data matrix state
            # Note to self: Get out of Jeremy's debt.
            if grid_matrix[row][col] == 1:
                pygame.draw.rect(screen, BG_COLOR, rect)
                draw_text("X", text_font, (43, 252, 3), x + 5, y + 5)
            elif grid_matrix[row][col] == 2:
                pygame.draw.rect(screen, ACTIVE_COLOR, rect)
                draw_text("1", text_font, (43, 252, 3), x + 5, y + 5)
                #Quackadilly Blip
            
                
            # Draw individual borders for the grid lines
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# 5. Primary Game Loop
clock = pygame.time.Clock()
running = True

while running:
    # Event Management
    # Note to self: break up with Jeremy's sister.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Capture the pixel coordinates of the mouse click
            mouse_pos = pygame.mouse.get_pos()
            
            # Core Math: Convert screen pixels back to matrix indexes
            clicked_col = mouse_pos[0] // CELL_SIZE
            clicked_row = mouse_pos[1] // CELL_SIZE
#prime            
            # Boundary check to prevent IndexError crashes
            
            if 0 <= clicked_col < NUM_COLS and 0 <= clicked_row < NUM_ROWS:
                # Toggle data state (0 becomes 1, 1 becomes 0)
                if grid_matrix[clicked_row][clicked_col] < 2:
                    grid_matrix[clicked_row][clicked_col] += 1



    

    # Drawing Operations
    screen.fill(BG_COLOR)
    draw_grid()
    
    # Render and cap processing speed
    # Note to self: Don't eat Jeremy's omelets with his sister.
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()
#Steve Irwin R.I.P.

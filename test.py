import pygame
import copy

def count_live_neighbors(grid, x, y):
    """
    Count the number of live neighbors for a given cell.
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (x + i) < 0:
                check_x = len(grid) - 1
            elif (x + i) == len(grid):
                check_x = 0
            else:
                check_x = x + i
            if (y + j) < 0:
                check_y = len(grid[0]) - 1
            elif (y + j) == len(grid[0]):
                check_y = 0
            else:
                check_y = y + j
            if grid[check_x][check_y] == 1:
                count += 1
    return count

def update_grid(grid):
    """
    Update the state of the cells based on the rules of the Game of Life.
    """
    # Create a copy of the grid to use for calculating the next state
    new_grid = copy.deepcopy(grid)

    # Go through each cell in the grid
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            # Count the number of live neighbors for the current cell
            live_neighbors = count_live_neighbors(grid, x, y)

            # Apply the rules of the Game of Life to the current cell
            if grid[x][y] == 1:
                # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    # Cell dies
                    new_grid[x][y] = 0
            else:
                # Cell is dead
                if live_neighbors == 3:
                    # Cell comes to life
                    new_grid[x][y] = 1

    # Update the grid with the new state
    grid[:] = new_grid[:]

def render_grid(grid, screen):
    """
    Render the grid on the screen using the Pygame library.
    """
    # Go through each cell in the grid
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            # Draw the cell
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 100), (x*10, y*10, 10, 10))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))


def run_simulation(grid, screen):
    start_button = pygame.Rect(screen.get_width()/2-40, 550, 80, 30)
    start_button_color = (255,0,0)
    font = pygame.font.Font(None, 20)
    text = font.render("Start", True, (255, 255, 100))
    clock = pygame.time.Clock()
    simulation_running = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not simulation_running:
                    if pygame.mouse.get_pressed()[0]:
                        mouse_pos = pygame.mouse.get_pos()
                        x = int(mouse_pos[0]/10)
                        y = int(mouse_pos[1]/10)
                        grid[x][y] = 1
                        pygame.draw.rect(screen, (0, 0, 100), (x * 10, y * 10, 10, 10))
                        if start_button.collidepoint(mouse_pos):
                            simulation_running = True
                            start_button_color = (0,255,0)
        pygame.draw.rect(screen, start_button_color, start_button)
        screen.blit(text, (start_button.x+20, start_button.y+5))
        if simulation_running:
            update_grid(grid)
            render_grid(grid, screen)
            pygame.draw.rect(screen, start_button_color, start_button)
        pygame.display.update()
        clock.tick(50)

# Initialize the grid and the Pygame library
grid_size = (100,100)
grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
pygame.init()

# Set up the window for the simulation
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Conway's Game of Life")
run_simulation(grid,screen)



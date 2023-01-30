import pygame
import copy
import random


def count_live_neighbors(grid, x, y):
    """
    Count the number of live neighbors for a given cell.
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            check_x = (x + i) % len(grid[0])
            check_y = (y + j) % len(grid[0])
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

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            # Draw the cell
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x * 10 +1, y * 10+1 ,9, 9))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x * 10 +1, y * 10+1 ,9, 9))

def draw_grid_lines(grid, cell_size):
    for x in range(len(grid) + 1):
        start_pos = (x * cell_size, 0)
        end_pos = (x * cell_size, len(grid[0]) * cell_size)
        pygame.draw.line(screen, (125, 142, 165), start_pos, end_pos, 1)
    for y in range(len(grid[0]) + 1):
        start_pos = (0, y * cell_size)
        end_pos = (len(grid) * cell_size, y * cell_size)
        pygame.draw.line(screen, (125, 142, 165), start_pos, end_pos, 1)

def run_simulation(grid, grid_size,screen):

    start_button = pygame.Rect(screen.get_width() / 2 + 250, 150, 80, 30)
    start_button_color = (255, 0, 0)
    font1 = pygame.font.Font(None, 20)
    text1 = font1.render("Start", True, (0, 0, 0))
    pygame.draw.rect(screen, start_button_color, start_button)
    screen.blit(text1, (start_button.x + 20, start_button.y + 5))

    restart_button = pygame.Rect(screen.get_width() / 2 + 250, 350, 80, 30)
    restart_button_color = (255, 0, 0)
    font2 = pygame.font.Font(None, 20)
    text2 = font2.render("Restart", True, (0, 0, 0))

    red_button = pygame.Rect(screen.get_width() / 2 + 250, 550, 80, 30)
    red_button_color = (255, 0, 0)
    font3 = pygame.font.Font(None, 20)
    text3 = font3.render("Red", True, (0, 0, 0))
    pygame.draw.rect(screen, red_button_color, red_button)
    screen.blit(text3, (red_button.x + 20, red_button.y + 5))

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
                        x = int(mouse_pos[0] / 10)
                        y = int(mouse_pos[1] / 10)
                        if start_button.collidepoint(mouse_pos):
                            simulation_running = True
                        if restart_button.collidepoint(mouse_pos):
                            simulation_running = False
                            grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
                        if (x > grid_size[0] or y > grid_size[1] or x < 0 or y < 0):
                            continue
                        if grid[x][y] == 0:
                            grid[x][y] = 1
                            pygame.draw.rect(screen, (0, 0, 0), (x * 10 +1, y * 10+1 ,9, 9))
                        elif grid[x][y] == 1:
                            grid[x][y] = 0
                            pygame.draw.rect(screen, (255, 255, 255), (x * 10 +1 , y * 10 +1 , 9, 9))
        if simulation_running:
            pygame.draw.rect(screen, restart_button_color, restart_button)
            screen.blit(text2, (restart_button.x + 20, restart_button.y + 5))
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    simulation_running = False
                    grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
            update_grid(grid)
            render_grid(grid, screen)
        pygame.display.update()
        clock.tick(10)

# Initialize the grid and the Pygame library
grid_size = (70, 70)
grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]
pygame.init()

# Set up the window for the simulation
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Conway's Game of Life")
color = (255, 255, 255)
screen.fill(color)
draw_grid_lines(grid,10)
run_simulation(grid, grid_size ,screen)

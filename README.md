# JDL
This project is a Python implementation of Conway's Game of Life using Pygame. It allows the user to select the starting configuration of alive cells by clicking on the screen, and then start the simulation by clicking on the "Start" button. The simulation runs according to the rules of the Game of Life:

1) Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2) Any live cell with two or three live neighbors lives on to the next generation.
3) Any live cell with more than three live neighbors dies, as if by overpopulation.
4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The program renders the grid on the screen, blue cells represent the alive cells and white cells represent the dead cells

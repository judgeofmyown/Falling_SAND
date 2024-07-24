import pygame
import random

pygame.init()
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode(size=(screen_width, screen_height))
clock = pygame.time.Clock()
running = True
test_size = 5 # in pixels
rows = int(screen_width // test_size)
cols = int(screen_height // test_size)
updateRate = 0.05
stopper = updateRate
isPaused = False
test_grid = [[0 for x in range(rows)] for y in range(cols)]
print(len(test_grid), len(test_grid[0]))

def update_grid():
    for x in range(rows):
        for y in range(cols-2, -1, -1):
            if test_grid[y][x] == 1:
                if test_grid[y+1][x] == 0:
                    test_grid[y][x] = 0
                    test_grid[y+1][x] = 1
                elif (x > 0 and test_grid[y+1][x-1] == 0) and (x < rows-1 and test_grid[y+1][x+1] == 0):
                    choose = random.randint(0, 1)

                    if choose == 0:
                        test_grid[y][x] = 0
                        test_grid[y+1][x-1] = 1
                    else:
                        test_grid[y][x] = 0
                        test_grid[y+1][x+1] = 1
                elif (x > 0 and test_grid[y+1][x-1] == 0):
                    test_grid[y][x] = 0
                    test_grid[y+1][x-1] = 1
                elif (x < rows -1 and test_grid[y+1][x+1] == 0):
                    test_grid[y][x] = 0
                    test_grid[y+1][x+1] = 1

def resetGrid():
    test_grid = [[0 for x in range(rows)] for y in range(cols)]   



def draw_grid():
    for x in range(rows):
        for y in range(cols):
            if test_grid[y][x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x*test_size, y*test_size, test_size, test_size))


while running:
    elapsed_time = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                isPaused = not isPaused
            if event.key == pygame.K_r:
                resetGrid()

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x//test_size
            grid_y = mouse_y//test_size
            if (grid_x > 0 and grid_x < rows -3 and grid_y > 0 and grid_y < cols-3):
                test_grid[grid_y][grid_x] = 1
                test_grid[grid_y+1][grid_x+1] = 1
                test_grid[grid_y+2][grid_x+2] = 1


    screen.fill('black')
    stopper -= elapsed_time
    
    if stopper <= 0:
        if isPaused == False:
            update_grid()
            stopper = updateRate
            
    draw_grid()
    
    pygame.display.flip()
  

pygame.quit()
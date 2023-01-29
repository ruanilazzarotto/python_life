import time
from random import choices
from ui_life import ui_print


MAP_HEIGHT = 30
MAP_WIDTH = 50
GENERATIONS = 1000
START_LIFE_RATE = 0.3
TIME_BETWEEN_GENERATION = 0.2


def generate_map(map):
    life_rate = START_LIFE_RATE
    if life_rate == 0:
        life_rate = 0.5
    row = []
    for x in range(MAP_HEIGHT+1):
        for y in range(MAP_WIDTH):
            row += choices([0, 1], [1/life_rate, life_rate])
        row = []
        map.append(row)

def is_alive(map, x, y):
    if x < 0 or x > MAP_HEIGHT - 1:
        return 0
    if y < 0 or y > MAP_WIDTH - 1:
        return 0
    return map[x][y] == 1

def should_die(neighbours):
    if neighbours < 2 or neighbours > 3:
        return True
    return False

def should_born(neighbours):
    if neighbours == 3:
        return True
    return False

def check_cell(map, x, y):
    alive = is_alive(map, x, y)
    neighbours = count_neighbours(map, x, y)
    if alive:
        if should_die(neighbours):
           map[x][y] = 0
           alive = False
    else:
        if should_born(neighbours):
            map[x][y] = 1
            alive = True
    return alive
    

def count_neighbours(map, x, y):
    neighbours = 0
    positions = [
         (x-1, y+1), (x, y+1), (x+1, y+1),
         (x-1, y  ),           (x+1, y),
         (x-1, y-1), (x, y-1), (x+1, y-1),
    ]
    for pos in positions:
        if is_alive(map, pos[0], pos[1]):
            neighbours += 1
    return neighbours


def star_game():
    map = []
    generate_map(map)
    live_cells = 0
    for gen in range(GENERATIONS):
        print('gerentaion: %d'%gen, end='\r')
        print(ui_print(map), end='\r')
        time.sleep(TIME_BETWEEN_GENERATION)
    
        x = 0
        for row in map:
            for y in range(0, len(row)):
                check_cell(map, x, y)
                if is_alive(map, x, y):
                    live_cells += 1
            x += 1

        if live_cells == 0:
            print("GAME OVER: No life left")
            break

star_game()




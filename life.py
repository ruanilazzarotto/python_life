import time
from random import choices
import ui_life as ui


MAP_HEIGHT = 30
MAP_WIDTH = 50
MAX_GENERATIONS = 1000
START_LIFE_RATE = 0.3
TIME_BETWEEN_GENERATION = 0.2


def generate_map(height=MAP_HEIGHT, width=MAP_WIDTH, life_rate=START_LIFE_RATE):
    map = []
    empty_rate = 1/life_rate if life_rate != 0 else 0
    row = []
    for x in range(0, height):
        for y in range(0, width):
            if life_rate == 0:
                row += [0]
            else:
                row += choices([0, 1], [empty_rate, life_rate])
        map.append(row)
        row = []
        
    return map


def map_dimentions(map):
    return len(map) , len(map[0])


def boundary_tranform(map, x, y):
    height, width = map_dimentions(map)
    if x < 0:
        x = height - 1
    elif x > height - 1:
        x = 0
       
    if y < 0: 
        y = width - 1
    elif y > width - 1:
        y = 0
    return x, y

def is_alive(map, x, y):
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
            alive = False
    else:
        if should_born(neighbours):
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
        tx, ty = boundary_tranform(map, pos[0], pos[1])
        if is_alive(map, tx, ty):
            neighbours += 1
    return neighbours


def was_stable(life_log):
    return life_log.count(life_log[0]) == len(life_log)


def check_stability(log, live_cells):
    if len(log) == 10:
        if was_stable(log):
            return True
        log.pop(0)  
    log.append(live_cells)
    return False


def next_generation(map):
    h, w =  map_dimentions(map)
    next_map = generate_map(h, w, 0)
    live_cells = 0
    for x in range(h):
        for y in range(w):
            alive = check_cell(map, x, y)
            if alive:
                live_cells += 1
            next_map[x][y] = 1 if alive else 0
            
    return next_map, live_cells 


def start_game():
    map = generate_map()
    live_cells = 0
    live_cells_count_log = []
    for gen in range(MAX_GENERATIONS):
        
        time.sleep(TIME_BETWEEN_GENERATION)
        map, live_cells = next_generation(map)

        if live_cells == 0:
            ui.ui_msg_no_life()
            break
        
        if check_stability(live_cells_count_log, live_cells):
            ui.ui_msg_stable()
            break
        
        ui.ui_print(map, gen, live_cells)


start_game()




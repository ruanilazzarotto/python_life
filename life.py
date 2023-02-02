import time
from random import choices
from ui_life import ui_print


MAP_HEIGHT = 30
MAP_WIDTH = 50
MAX_GENERATIONS = 1000
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

def boundary_tranform(x, y):
    if x < 0:
       x = MAP_HEIGHT - 1
    elif x > MAP_HEIGHT - 1:
       x = 0
       
    if y < 0: 
       y = MAP_WIDTH - 1
    elif y > MAP_WIDTH - 1:
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
        tx, ty = boundary_tranform(pos[0], pos[1])
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
    
    
def star_game():
    map = []
    generate_map(map)
    live_cells = 0
    live_cells_count_log = []
    for gen in range(MAX_GENERATIONS):
        live_cells = 0
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
        
        if check_stability(live_cells_count_log, live_cells):
            print("GAME OVER: The number of living cells is stable")
            break
        
        print('generation: %d'%gen)
        print(ui_print(map))


star_game()




import time
import patterns
from ui_life import ui_print
from life import generate_map, next_generation, insert_pattern, check_stability

MAX_GENERATIONS = 1000
TIME_BETWEEN_GENERATION = 0.1

def star_game():
    map = generate_map(life_rate=0.3)
    # insert_pattern(map, patterns.glider(), 5, 5)
    print(ui_print(map))
    live_cells = 0
    live_cells_count_log = []
    for gen in range(MAX_GENERATIONS):
        
        time.sleep(TIME_BETWEEN_GENERATION)
        map, live_cells = next_generation(map)

        if live_cells == 0:
            print("GAME OVER: No life left")
            break
        
        if check_stability(live_cells_count_log, live_cells):
            print("GAME OVER: The number of living cells is stable")
            break
        
        print('generation: %d'%gen)
        print(ui_print(map))


star_game()
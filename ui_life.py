
def ui_print(map, gen):
    print('generation: %d'%gen)
    map_str = ""
    print("", end='\r')
    x = 0
    for row in map:
        for y in range(0, len(row)):
            if map[x][y] == 1:
                map_str += " + "
            else:
                map_str += " . "
                # print(".", end='')
        x+=1
        map_str += "\n"
        # print("")
    print(map_str)

def ui_msg_no_life():
    print("GAME OVER: No life left")

def ui_msg_stable():
    print("GAME OVER: The number of living cells is stable")
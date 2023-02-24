from os import system, name

UI_CELL = " 0 "
UI_VOID = "   "

def ui_clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac and linux
    else:
        _ = system('clear')

def ui_print(map, gen, cells):
    ui_clear()
    map_str = ""
    x = 0
    for row in map:
        for y in range(0, len(row)):
            if map[x][y] == 1:
                map_str += UI_CELL
            else:
                map_str += UI_VOID
        x+=1
        map_str += "\n"
    print('---------------------------------------------')
    print('| generation: %6d | living cells: %6d |'%(gen, cells))
    print(map_str)


def ui_msg_no_life():
    print("GAME OVER: No life left")

def ui_msg_stable():
    print("GAME OVER: The number of living cells is stable")
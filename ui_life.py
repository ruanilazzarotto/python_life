
def ui_print(map):
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
    return map_str
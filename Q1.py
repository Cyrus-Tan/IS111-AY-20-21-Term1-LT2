def get_all_tank_sizes(tanks):
    """returns the sizes ('S' for small, 'M' for medium, 'L' for large) of the tanks in the same order as their dimensions are given in tanks"""
    final_list = []
    size = ""
    # tanks is a list of tuples
    for each_tuple in tanks:
        volume = (each_tuple[0]*each_tuple[1]*each_tuple[2])/231
        volume_rounded = int(volume)                              # round down to an integer
        if volume_rounded < 20:
            size += 'S'
        elif volume_rounded > 19 and volume_rounded < 50:
            size += 'M'
        elif volume_rounded > 49:
            size += 'L'
        final_list.append(size)
        size = ""                   # refreshes size for next tuple
    return final_list

print(get_all_tank_sizes([(12, 6, 8),(24, 12, 18),(36.375, 18.375, 19)]))
def get_hi_lo(products):
    highest_value = 0
    lowest_value = 0
    highest_name = ""
    lowest_name = ""
    # To return None when parameter is empty
    if len(products) == 0:
        return (None, None)

    # products is a list of tuples
    for each_tuple in products:
        price = each_tuple[1]
        if price > highest_value:
            highest_value = price        # price will replace current_value
            highest_name = each_tuple[0]
        # let first tuple price be lowest value to compare with following tuples
        if products.index(each_tuple) == 0:     # if it's first tuple of the list
            lowest_value += price
            lowest_name += each_tuple[0]
        if price < lowest_value or price == lowest_value:  # to replace lowest value
            lowest_value = price
            lowest_name = each_tuple[0]

    return (highest_name, lowest_name)

#print(get_hi_lo([('apple', 100), ('orange', 200), ('pear', 300)]))
#print(get_hi_lo([('apple',100),('orange',250),('pear',200),('banana',150)]))
print(get_hi_lo([('apple', 100)]))
#print(get_hi_lo([]))
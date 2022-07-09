def get_polynomial(poly_str):
    """function returns a list that represents all the coefficients of the polynomial after it is reduced to the simplest form."""
    final_list = []
    dict_of_exponent ={}
    poly_str_strip = poly_str.replace(" ","")     # to remove all whitespaces in poly_str
    string_splitted = list(poly_str_strip)        # get a list of each char of poly_string
    # SPECIAL CASE: First digit is a positive number, won't get '+' sign infront
    # Hence, use list.insert() to insert '+' sign to front of list
    if string_splitted[0] != '-':               # if starts with a number
        string_splitted.insert(0, '+')          # insert '+' at index 0
    for index in range(len(string_splitted)):
        char = string_splitted[index]
        # STEP 1: Get exponent value(key), coefficient(value) for dict in descending order
        # STEP 2: For power of 2 or more
        if char == '^':                                         # find the exponent value
            exponent_value = int(string_splitted[index + 1])    # since exponent value is after ^
            coefficient = string_splitted[index - 2]
            sign = string_splitted[index - 3]
            coefficient_with_sign = int(sign + coefficient)
            if exponent_value not in dict_of_exponent:      # check if key exists in dict yet
                dict_of_exponent[exponent_value] = coefficient_with_sign
            else:                                           # if key alrdy exists
                dict_of_exponent[exponent_value] += coefficient_with_sign
        # STEP 3: For power of 1 (check current char is 'x' an next char is not '^')
        if char == 'x':
            next_char = string_splitted[index + 1]
            if next_char != '^':                     # current x is power of 1
                coefficient = string_splitted[index - 1]
                sign = string_splitted[index - 2]
                coefficient_with_sign = int(sign + coefficient)
                exponent_value = 1
                if exponent_value not in dict_of_exponent:     # if power of 1 don't exist yet
                    dict_of_exponent[exponent_value] = coefficient_with_sign
                else:                                          # if power exists alrdy
                    dict_of_exponent[exponent_value] += coefficient_with_sign
        # STEP 4: For x power of 0 (before and after number is + or - sign)
        # SPECIAL CASE: Beware if at last number, won't show anything after the number
        # -----> if at last element and element is a number, before element is a sign--> will be x power 0
        if index == len(string_splitted) - 1:        # if at last element of list
            if char != 'x':                          # if it's a number: since last element can only be number or x
                before_char = string_splitted[index - 1]
                if before_char == '+' or before_char == '-':
                    exponent_value = 0
                    coefficient = char
                    sign = before_char
                    coefficient_with_sign = int(sign + coefficient)
                    if exponent_value not in dict_of_exponent:
                        dict_of_exponent[exponent_value] = coefficient_with_sign
                    else:
                        dict_of_exponent[exponent_value] += coefficient_with_sign
        # if anywhere except last element of list
        elif index != len(string_splitted) - 1:
            next_char = string_splitted[index + 1]
            before_char = string_splitted[index - 1]
            if next_char == "+" or next_char == "-":
                if before_char == "+" or before_char == "-":
                    exponent_value = 0
                    coefficient = char
                    sign = before_char
                    coefficient_with_sign = int(sign + coefficient)
                    if exponent_value not in dict_of_exponent:
                        dict_of_exponent[exponent_value] = coefficient_with_sign
                    else:
                        dict_of_exponent[exponent_value] += coefficient_with_sign
    # STEP 5: Sort the key of dict in descending order (higher power first)
    # Then, append the value to final_list
    list_of_key_value_pair = dict_of_exponent.items()
    for each_key_value_pair in sorted(list_of_key_value_pair, reverse=True):  # sorted() to sort by key
        value = each_key_value_pair[1]
        final_list.append(value)

    return final_list

#print(get_polynomial('2x - 2x^2 + 3x - 1 + 6x^3'))           # (SOLVED)
print(get_polynomial(' 4x -2x^2 + 3x^5 - 6x^2'))              # LEFTOVER ISSUE: Show 0 for power of x not shown
print(get_polynomial('3x^2 - 2x - 3x^2'))                     # Remove coefficient of 0 if coefficients cancel out

# LEFTOVER ISSUE: Need to find a way to show 0 for power of x not shown,
# ---> And, remove coefficient of 0 if coefficients cancel out to give 0
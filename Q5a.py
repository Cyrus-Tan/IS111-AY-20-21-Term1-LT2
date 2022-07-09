def multiply(polynomials):
    """function returns a list that represents coefficients of the resultant polynomial after multiplying all the polynomials in the given list polynomials."""
    for each_list in polynomials:         # iterate through each list of polynomial
        for index in range(len(each_list)):   # iterate through index of each list
            coefficient = each_list[index]

        print(each_list)

# LEFTOVER ISSUE: Need to find a way to multiply first term with the next first term
# ------> How to separate the coefficients of different polynomial power


print(multiply([[1, 2, 3], [5, 6, 7]]))
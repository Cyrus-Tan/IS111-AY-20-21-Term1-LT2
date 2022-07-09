def calculate_term_gpa(term_grades, mapping):
    total_score = 0
    courses = []
    list_of_term_grades = list(term_grades)                        # get list of each char
    for index in range(len(list_of_term_grades)):                  # iterate through the index of the list
        each_grade = list_of_term_grades[index]
        if each_grade.isalpha():                                   # if its an alphabet, not + or - or *
            courses.append(each_grade)                             # to find total no. of courses

        if index == len(term_grades) - 1:                 # if current char is last char of the list
            # need to add TO TOTAL SCORE if last char is alphabet
            if each_grade.isalpha():                      # last char is alphabet only
                grade = each_grade
                total_score += mapping[grade]             # no need check for next char if current char is at last char
            # If last char is sign, include alphabet before the sign and get the grade
            if each_grade.isalpha() == False:
                previous_alphabet = list_of_term_grades[index - 1]
                grade = previous_alphabet + each_grade                   # Concatenate alphabet and sign
                total_score += mapping[grade]
        else:                                                            # if not at last char of list
            if each_grade.isalpha():                                     # if current char is alphabet, next char also, then add current alphabet
                if list_of_term_grades[index + 1].isalpha() == True:     # next char is alphabet too
                    grade = each_grade
                    total_score += mapping[grade]
            elif each_grade.isalpha() == False:                              # if current char is + or - or * sign
                # combine sign with previous alphabet, then add to final score
                previous_alphabet = list_of_term_grades[index-1]             # get the alphabet
                grade = previous_alphabet + each_grade                       # concatenate alphabet and sign
                total_score += mapping[grade]

    number_of_courses = len(courses)     # get total no. of courses
    GPA = total_score/number_of_courses
    return GPA

print(calculate_term_gpa('ACAC', {'A': 4, 'B': 3, 'C': 2, 'F': 0}))
print(calculate_term_gpa('A+AA-', {'A+':4.3, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}))
print(calculate_term_gpa('A*AA', {'A*':4, 'A':3.5, 'B*':3, 'B':2.5, 'C':2, 'F':0}))


# LEFTOVER ISSUE: Need to get specific index of the element, even if element has multiple occurrences (SOLVED)
# --------------> use 'for index in range(len(list))' instead of 'for element in list'
# --------> IDEA: Iterate through index of list by using 'for index in range(len(list))' if u want to find index of element,
#           especially if there are multiple occurrences of the element. Otherwise, code will always only show index of
#           the first occurrence of the element
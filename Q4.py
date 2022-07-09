def get_daily_spending(filename, start_day, end_day, month, year):
    """function will return a list that contains the daily spending (in cents)"""
    # Since need add up amount on the same day, use dict where keys are the day and value is the total amt of that day
    dict_days = {}
    for number in range(start_day, end_day + 1):    # iterate through the date and add as key to dict
        dict_days[number] = 0                       # so that output will be 0 in final_list if no spending on that day
    final_list = []
    data = open(filename)
    for each_line in data:
        each_line = each_line.rstrip('\n')          # remove empty line between each line
        list_of_elements = each_line.split('|')     # split line into list separated by '|'
        date = list_of_elements[0]
        amount = int(list_of_elements[1])
        # compare date with date in file
        # Convert all to single digit. e.g: 09 to 9 by using int()
        date_splitted = date.split('/')              # split into a list separated by '/'
        day = int(date_splitted[0])
        month_line = int(date_splitted[1])
        year_line = int(date_splitted[2])
        if year_line == year:            # if same year
            if month_line == month:      # if same month
                if day >= start_day and day <= end_day:             # if date meets requirements
                    if day in dict_days:                 # check for key in dict---> if there's alrdy a day
                        dict_days[day] += amount         # add (sum) amt for each day
                    elif day not in dict_days:
                        total_cost_for_day = 0           # start from 0 if no such day found yet
                        total_cost_for_day += amount
                        dict_days[day] = total_cost_for_day

    # iterate through the keys(day) of the dict and get each value(amt), append value to final_list
    for each_value in dict_days.values():            # iterate through the values of dict
        final_list.append(each_value)
    return final_list

print(get_daily_spending('trans_file.txt', 3, 5, 10, 2020))
print(get_daily_spending('trans_file.txt', 6, 7, 10, 2020))

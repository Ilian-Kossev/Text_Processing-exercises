input_string = input()
new_string = ''
unique_symbols_string = ''
curr_counter = -1
repeat_str = ''
for num in range(len(input_string)):
    curr_counter += 1
    if not input_string[num].isdigit():
        new_string += input_string[num].upper()
        if input_string[num].lower() not in unique_symbols_string:
            unique_symbols_string += input_string[num].lower()
    else:
        i = num
        counter_digits = 0
        while input_string[i].isdigit():
            num += 1
            curr_counter += 1
            counter_digits += 1
            repeat_str += input_string[i]
            i += 1
            if i >= len(input_string):
                break
        repeat_number = int(repeat_str)
        repeat_str = ''
        if repeat_number > 1:
            index_starting_position = num - curr_counter
            index_end_position = num - counter_digits
            for _ in range(repeat_number-1):
                new_string += input_string[index_starting_position: index_end_position].upper()
        curr_counter = -1

print(f'Unique symbols used: {len(unique_symbols_string)}')
print(new_string)


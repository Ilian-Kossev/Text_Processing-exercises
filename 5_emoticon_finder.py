input_string = input()
count_index = 0
for symbol in input_string:
    count_index += 1
    if symbol == ':':
        index_symbol = count_index
        print(f':{input_string[index_symbol]}')
input_string = input().split()
result = 1
final_result = 0
result_list = []
for string in input_string:
    if string[0].islower():
        number_to_multiply = ord(string[0]) - 96
        result = number_to_multiply * int(string[1:(len(string)-1)])
    else:
        divider = ord(string[0]) - 64
        result = int(string[1:(len(string)-1)]) / divider
    if string[-1].islower():
        final_result = result + (ord(string[-1]) - 96)
        result_list.append(final_result)
    else:
        final_result = result - (ord(string[-1]) - 64)
        result_list.append(final_result)

total_sum = sum(result_list)
print(f'{total_sum:.2f}')
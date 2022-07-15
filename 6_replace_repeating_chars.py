input_string = input()
new_string = input_string[0]
for num in range(1, len(input_string)):
    if not input_string[num] == input_string[num - 1]:
        new_string += input_string[num]
    else:
        continue
print(new_string)



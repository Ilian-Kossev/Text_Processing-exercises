some_string = input()
new_string = ''
strength = 0
for i in range(len(some_string)):
    if some_string[i] == '>':
        new_string += '>'
        strength += int(some_string[i + 1])
    else:
        if strength > 0:
            strength -= 1
        else:
            new_string += some_string[i]
print(new_string)

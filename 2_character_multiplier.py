input_data = input().split()
limit_scan = 0
total_value = 0
sum_remainder = 0

if len(input_data[0]) <= len(input_data[1]):
    limit_scan = len(input_data[0])
    for num in range(limit_scan, len(input_data[1])):
        sum_remainder += ord(input_data[1][num])
else:
    limit_scan = len(input_data[1])
    for num in range(limit_scan, len(input_data[0])):
        sum_remainder += ord(input_data[0][num])
for num in range(limit_scan):
    value_1 = ord(input_data[0][num])
    value_2 = ord(input_data[1][num])
    total_value += value_1 * value_2
sum_total_value_and_sum_remainder = sum_remainder + total_value

print(sum_total_value_and_sum_remainder)



input_data = input().split(', ')

for item in input_data:
    if 3 <= len(item) <= 16:
        valid_item = True
        for symbol in item:
            if symbol.isalnum() or symbol == '-' or symbol == '_':
                continue
            else:
                valid_item = False
                break
        if valid_item:
            print(item)
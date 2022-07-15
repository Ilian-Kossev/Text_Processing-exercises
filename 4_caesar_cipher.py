input_text = input()
encrypted_text = ''
for symbol in input_text:
    ascii_value = ord(symbol)
    new_value = ascii_value + 3
    new_symbol = chr(new_value)
    encrypted_text += new_symbol
print(encrypted_text)

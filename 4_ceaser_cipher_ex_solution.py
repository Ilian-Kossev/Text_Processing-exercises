text = input()
encrypted_text = [chr(ord(x)+3) for x in text]
print(''.join(encrypted_text))
# print(''.join([chr(ord(x)+3) for x in input()])

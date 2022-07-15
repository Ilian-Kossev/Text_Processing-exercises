words = input().split()
total_sum = 0
word_one = words[0]
word_two = words[1]
shorter_word_length = min(len(words[0]), len(words[1]))
for i in range(shorter_word_length):
    word_one_curr_ch = word_one[i]
    word_two_curr_ch = word_two[i]
    ch_multiplication = ord(word_one_curr_ch) * ord(word_two_curr_ch)
    total_sum += ch_multiplication

longer_word_length = max(len(words[0]), len(words[1]))
for i in range(shorter_word_length, longer_word_length):
    if len(word_one) > len(word_two):
        curr_word_ch = word_one[i]
    else:
        curr_word_ch = word_two[i]

    total_sum += ord(curr_word_ch)
print(total_sum)

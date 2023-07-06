def length_of_last_word(line):
    words = line.split()
    if len(words) > 0:
        last_word = words[-1]
        return len(last_word)
    else:
        return 0
line = "I am studying in saveetha university"
last_word_length = length_of_last_word(line)
print("Length of the last word:", last_word_length)

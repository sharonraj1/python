def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = "I am studying in saveetha university"
word_count = count_words(sentence)
print("Number of words:",word_count)

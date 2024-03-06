def count_words(text):
    word = text.split()
    return len(word)

sentence = input("Write your sentence here: ")
print("Your words are ", count_words(sentence))
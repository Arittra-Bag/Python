sentence = input("Enter a sentence: ").lower()
word = input("Enter the word to count: ").lower()
words = sentence.split()
word_count = 0
for w in words:
    if w == word:
        word_count += 1
print(f'This word appears {word_count} times in the sentence.')
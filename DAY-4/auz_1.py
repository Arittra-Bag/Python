sentence = input("Enter a Sentence: ").lower()
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in sentence:
    if char in 'aeiou':
        vowel_count[char] += 1

for vowel, count in vowel_count.items():
    print(f'Count of {vowel} = {count}')
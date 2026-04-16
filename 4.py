text = input().split()
unique_words = []

for word in text:
    clean_word = word.strip('.,?!:;-')
    if clean_word not in unique_words:
        unique_words.append(clean_word)

print(unique_words)

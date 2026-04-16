text = list(input().split())
holes_chars = "abdegopq"
total_holes = 0
total_no_holes = 0
special_words = []

for word in text:
    word_holes = 0
    for char in list(word):
        if char in holes_chars:
            word_holes = word_holes + 1

    total_holes += word_holes
    total_no_holes += (len(word) - word_holes)

    if word_holes >= 2:
        special_words.append(word)

print(total_holes, total_no_holes)
print(special_words)


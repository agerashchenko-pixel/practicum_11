text = input().split()
final_txt = []

for word in text:
    clean_word = word.strip('.,?!:;-')
    final_txt.append(clean_word)

print(final_txt)

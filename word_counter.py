with open('text.txt', 'r') as file:
    word_file = file.read()
word_list = word_file.split('\n')

word_list = [word for word in word_list if word]

word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")

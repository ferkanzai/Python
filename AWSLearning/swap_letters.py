word = "word"
print(word[::-1])
new_word = ''
for i in range(len(word)):
    new_word = new_word + word[-i - 1]
print(new_word)

user_input = input("Text:")
word_count_dict = {}

words = user_input.split()
print(words)
for word in words:
 word_count_dict[word] = word_count_dict.get(word,0) + 1
words = list(word_count_dict.keys())
words.sort()
# use the max function to find the length of the largest word
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count_dict[word]))
import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen, and a the was in day the .'
words = message.split()
word_count = {}

for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1

# for wd in word_count.items():
#     print(wd)

pprint.pprint(word_count)
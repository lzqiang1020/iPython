spam = ['apples', 'bananas', 'tofu', 'cats']

def connect(args):
    new_spam = ''
    for i in range(len(args)-1):
        new_spam += (args[i] + ', ')
    new_spam += ('and ' + args[-1])
    return new_spam

print(connect(spam))
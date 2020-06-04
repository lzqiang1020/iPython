while True:
    name = input("Who are you?\n>>>")
    if name != 'lzqiang':
        continue
    print("Hi," + name + "what is the password? (It is a fish.)")
    password = input("Please type the password.\n>>>")
    if password == 'lzqiang':
        break

print("Access granted.")

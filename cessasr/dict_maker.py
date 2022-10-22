with open("words") as f:
    dict = {word.lower().rstrip(): True for word in f.readlines()}

print(dict)
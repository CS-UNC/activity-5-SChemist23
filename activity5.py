### more than 20
def more_than_20(file):
    words = []
    data = open(file, 'r')
    for word in data:
        if len(word.strip()) > 20:
            words.append(word.strip())
##different style, same result.
words = [x.strip() for x in data if len(x.strip()) > 20]

print(more_than_20("CROSSWD.txt"))




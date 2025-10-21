def twenty_or_more(CROSSWD.txt):
    long_words = []                        # list to store long words
    with open(CROSSWD.txt, 'r') as f:             # open the file for reading
        for line in f:                     # read each line
            words = line.split()           # split the line into words
            for word in words:
                if len(word) > 20:         # check word length
                    long_words.append(word)  # add to list
    return long_words



def has_no_e(word):
    for letter in word:
        if letter == 'e' or letter == 'E':
            return False
    return True



def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True



def all_uses_only(CROSSWD.txt, letters):
    valid_words = []
    with open(CROSSWD.txt, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if uses_only(word, letters):    
                    valid_words.append(word)
    return valid_words
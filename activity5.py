def twenty_or_more(file):
    long_words = []                        
    with open(file, 'r') as f:             
        for line in f:                     
            words = line.split()           
            for word in words:
                if len(word) > 20:         
                    long_words.append(word)  
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



def all_uses_only(file, letters):
    valid_words = []
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if uses_only(words, letters):    
                    valid_words.append(word)
    return valid_words
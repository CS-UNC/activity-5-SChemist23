








def more_than_20(file):
    words = []    
    data = open(file, 'r') 
    for word in data:
        if len(word.strip()) > 20:
            words.append(word.strip())
    words = [x.strip() for x in data if len (x.strip()) > 20]
    return words

print(more_than_20("CROSSWD.txt"))


def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
    
def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False
    return True

def all_uses_only(file,letters):
    result = []
    x = open(file, 'r')
    for line in x:
        word = line.strip()
        if uses_only(word, letters):
            result.append(word)
    return result
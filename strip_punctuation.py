def strip_punctuation(file):
    word_list = []
    for line in file:
        conjugated = ''
        length = 0
        for i in line:
            if i in '!"#$%&()*+,-./:;<=>?@[\]^`{|}~ ':
                modified = conjugated.lower()
                if conjugated != '':
                    word_list.append(modified)
                    conjugated = ''
                    length = 0
            elif i != ' ':
                conjugated += i
                length += 1
    return word_list

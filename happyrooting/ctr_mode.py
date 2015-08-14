import binascii
import string

ctxt1 = 0x369f9e696bffa098d2bb383fb148bd90
ctxt2 = 0x23d7847f28e4b6cc86be386cb64ca281

m1xm2 = binascii.unhexlify("{:0<32x}".format(ctxt1 ^ ctxt2))

characters = string.lowercase + ' '

possible_paths = []

valid_words = set()

with open('/usr/share/dict/words', 'r') as dict_words:
    for word in dict_words:
        word = word.strip()
        if all(c in characters for c in word):
            valid_words.add(word)

for byte in m1xm2:
    possibilities = []
    for character in characters:
        c1 = character
        c2 = chr(ord(c1) ^ ord(byte))
        if c2 in characters:
            possibilities.append((c1, c2))
    possible_paths.append(possibilities)

def valid_str(string):
    words = string.split(' ')
    for word in words[:-1]:
        if word not in valid_words:
            return False
    for valid_word in valid_words:
        if valid_word.startswith(words[-1]):
            return True
    return False

def paths(current_str1, current_str2, possibilities):
    if valid_str(current_str1) and valid_str(current_str2):
        if len(current_str1) > 5: 
            #print "{}, {}".format(current_str1, current_str2)
            pass
        if len(possibilities) == 0:
            yield current_str1, current_str2
        else:
            b = possibilities[0]
            for c1, c2 in b:
                for s1, s2 in paths(current_str1 + c1, current_str2 + c2, possibilities[1:]):
                    yield s1, s2

for path in paths('', '', possible_paths):
    print path

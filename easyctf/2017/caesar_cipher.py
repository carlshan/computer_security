import string
import sys

encode = {letter: number for letter, number in zip(string.ascii_lowercase, range(1, 27))}
decode = {number: letter for letter, number in encode.iteritems()}


def shift(string, number, encode, decode):
    result = []
    for letter in string:
        shifted = (encode[letter] + number) % 26
        if shifted == 0:
            result.append(letter)
        else:
            shifted_letter = decode[shifted]
            result.append(shifted_letter)
    return ''.join(result)

to_encode = ''.join(sys.argv[1:]).lower()

for number in range(1, 25):
    shifted = shift(to_encode, number, encode, decode)
    print(shifted)

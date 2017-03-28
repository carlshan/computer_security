data = open("fd36ad4f1023c064b44f48941ce36f4eed63202d__20xx.dtm", 'r+').readlines()[0]

ascii = []

for character in data:
    try:
        encoded = character.encode('ascii')
        if encoded not in ascii:
            ascii.append(encoded)
    except:
        pass

# joined = ''.join(ascii)

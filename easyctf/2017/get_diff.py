f1 = open('file1.txt', 'r+')
f2 = open('file2.txt', 'r+')

differences = []

text1 = f1.readlines()[0]
text2 = f2.readlines()[0]

for x, y in zip(text1, text2):
    if x != y:
        differences.append(x)

print(''.join(differences))

line1 = raw_input()
line2 = raw_input()

total = sum([int(s.strip()) for s in line2.split(' ')])

print(total)

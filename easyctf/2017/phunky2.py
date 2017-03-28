import operator
import sys
n = int(sys.argv[1])
# jkx = 0 # REDACTED
# pork = jkx-1
# print("pork is {}".format(pork))
# jkx *= pork

jkx = n**2 - n

print("jkx is {}".format(jkx))

# This gets all the primes less than 10000
pp = filter(lambda g: not any(g % u == 0 for u in range(2, g)), range(2, 10000))


b = reduce(operator.mul, (pp[i] ** int(str(jkx)[i]) for i in range(len(str(jkx)))))
print b == 2588050895346329988820416440811541314031100625085731505113461878611166143408363147089319099999406727883710926093201434108551852579977068908765381785350456379110925188109957201536300665858601695961008525032396307133908960660196420374880073235504705252914332593895020739098443453024411934373913804802739234374864026298556784306307986652727373593750
print "b is {}".format(b)
print "The length of b is {} and the length of the original input is {}".format(len(str(b)), len(str(n)))

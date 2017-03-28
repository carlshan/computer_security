char = chr(105)

local = locals()

b = '__bu' + char + 'lt' + char + 'ns__'

bultns = local.get(b)

prnt_name = 'pr' + char + 'nt'
nput_name = char + 'nput'

prnt = getattr(bultns, prnt_name)
nput = getattr(bultns, nput_name)

num = nput()

lst = range(1, num+1)


def func(n):
    fzz = "F" + char + "zz"
    prnt(fzz*(not n % 3) + "Buzz"*(not n % 5) or n)

map(func, lst)

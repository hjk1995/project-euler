import math


gi_obj = {}
sfn_obj={}


def fn(n):
    number = map(int, str(n))
    numbers = [math.factorial(int(x)) for x in number]
    return int(math.fsum(numbers))


def sfn(n):
    n = fn(n)
    number = list(map(int, str(n)))
    return int(math.fsum(number))


def sgi(n):
    if n not in gi_obj.keys():
        optimizeGi(n)
        num = gi_obj[n]
        number = list(map(int, str(num)))
        return int(math.fsum(number))
    else:
        num = gi_obj[n]
        number = list(map(int, str(num)))
        return int(math.fsum(number))


def optimizeGi(n):
    l = 1
    if len(gi_obj) > 0:
        l = list(gi_obj.keys())[-1]
    for i in reversed(range(l, n + 1)):
        gi_obj[i] = gi(i)

def optimizeSfn(n):
    l = 1
    if len(sfn_obj) > 0:
        l = list(sfn_obj.keys())[-1]
    for i in reversed(range(l, n + 1)):
        sfn_obj[sfn(i)] = i



def gi(n):
    val, i = sfn(1), 1
    while val != n:
        i = i + 1
        val = sfn(i)
    return i


testcases = int(input())
for _ in range(0, testcases):
    n, m = [int(i) for i in input().split()]
    optimizeSfn(n)
    print(int(math.fsum([sgi(x) for x in range(1, n + 1)])) % m)

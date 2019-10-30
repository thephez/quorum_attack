#!/usr/bin/python
from decimal import Decimal
from math import log
from math import factorial as fac

def binom_orig(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m]

def binom(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

#Total number of masternodes
mns=5000
#Quorum size used for ChainLocks
qsz=500
#Number of nodes in a LLMQ needed for a ChainLock
qmaj=240

print("Assume {} masternodes in total".format(mns))
print("The number of masternodes in a quorum: {}".format(qsz))

numb = binom(mns, qsz)
print("Total number of LLMQs: {}".format(numb))

#Number of attacking nodes
y = 400

print("Assume {} of MNs are Byzantine".format(y))
temp = 0
temp2 = 0

for x in range(qmaj, qsz+1):
    print("\nNumber of LLMQs with {} Byzantine nodes:".format(x))
    temp = temp + binom(y, x) * binom(mns-y, qsz -x)
    #temp2 = temp2 + binom_orig(y, x) * binom_orig(mns-y, qsz -x)
    #if temp != temp2:
    #    print("!!!!!!!!!!!!!!!! ERRROR !!!!!!!!!!!!!!!!!!!!!!!!")
    #    print("\n{}\n{}\n".format(temp, temp2))
    #print("\tB: {}".format(binom(y, x) * binom(mns-y, qsz-x)))
    #print("\n\ttemp: {}".format(temp))

print("Total number of Byzantine Quorums: {}".format(temp))
print("Log base 10 of above: {}".format(log(temp, 10)))
print("Total number of LLMQs: {}".format(numb))
print("Log base 10 of above: {}".format(log(numb, 10)))
print("Probabilty of malicious ChainLock: {}".format(10 ** (log(temp, 10)-log(numb, 10))))


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

#Number of attacking nodes
attacking_nodes = 3000

#Total number of masternodes
mns=5000
#Quorum size used for ChainLocks
qsz=400
#Number of nodes in a LLMQ needed for a ChainLock
qmaj=240

#print("Assume {} masternodes in total".format(mns))
print("The number of masternodes in a quorum: {}".format(qsz))

numb = binom(mns, qsz)
#print("Total number of LLMQs: {}".format(numb))

#print("Assume {} of MNs are Byzantine".format(y))
temp = 0
temp2 = 0

for x in range(qmaj, qsz+1):
    #print("\nNumber of LLMQs with {} Byzantine nodes:".format(x))
    temp = temp + binom(attacking_nodes, x) * binom(mns - attacking_nodes, qsz - x)
    #temp2 = temp2 + binom_orig(y, x) * binom_orig(mns-y, qsz -x)
    #if temp != temp2:
    #    print("!!!!!!!!!!!!!!!! ERRROR !!!!!!!!!!!!!!!!!!!!!!!!")
    #    print("\n{}\n{}\n".format(temp, temp2))
    #print("\tB: {}".format(binom(y, x) * binom(mns-y, qsz-x)))
    #print("\n\ttemp: {}".format(temp))

#print("{} malicious MNs (out of {} total MNs)".format(i, mns))
#print("Total number of Byzantine Quorums: {}".format(temp))
#print("Log base 10 of above: {}".format(log(temp, 10)))
#print("Total number of LLMQs: {}".format(numb))
#print("Log base 10 of above: {}".format(log(numb, 10)))

probability = 10 ** (log(temp, 10)-log(numb, 10))
if probability < 1:
    print("Probabilty of malicious ChainLock with {} out of {} Byzantine nodes: {}".format(attacking_nodes, mns, 10 ** (log(temp, 10)-log(numb, 10))))
else:
    print("Probability of malicious ChainLock 100% for all values > {}".format(i))


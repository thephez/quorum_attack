#!/usr/bin/python
from decimal import Decimal
from math import log
from math import factorial as fac

def binom(x, y):
    try:
        binom = fac(x) // fac(y) // fac(x - y)
    except ValueError:
        binom = 0
    return binom

#Total number of masternodes
mns=5000
#Quorum size used for ChainLocks
qsz=400
#Number of nodes in a LLMQ needed for a ChainLock
qmaj=240

bad_node_start_count = 0
bad_node_step_size = 25

print("The number of masternodes in a quorum: {}".format(qsz))

numb = binom(mns, qsz)
#print("Total number of LLMQs: {}".format(numb))

for bad_nodes in range(bad_node_start_count, mns, bad_node_step_size):
    temp = 0
    for x in range(qmaj, qsz + 1):
        temp = temp + binom(bad_nodes, x) * binom(mns - bad_nodes, qsz - x)

    if temp > 0:
        probability = 10 ** (log(temp, 10)-log(numb, 10))
        if probability < 1:
            print("Probabilty of malicious ChainLock with {} out of {} Byzantine nodes: {}".format(bad_nodes, mns, 10 ** (log(temp, 10)-log(numb, 10))))
        else:
            print("Probability of malicious ChainLock 100% for all values > {}".format(bad_nodes))
            break
    else:
        print("Probability of malicious ChainLock ~0 for all values < {}".format(bad_nodes))
        continue


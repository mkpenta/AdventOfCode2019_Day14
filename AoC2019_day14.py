import math
from typing import *


def wordnumpair(l):
    k = l.strip(" ")
    k = k.split(" ")
    word = str(k[1])
    num = int(k[0])
    return (num, word)


def load_data():
    data = {}
    f = open("input")
    lines = f.readlines()
    for line in lines:
        print(line)
        l = line[:-1]
        l = l.split("=>")
        e = (count, key) = wordnumpair(l[1])
        if key not in data:
            data[key] = [count, []]
        else:
            data[key][1].append(e)
        c = l[0].split(", ")
        for u in c:
            e = wordnumpair(u)
            data[key][1].append(e)
    return data


def compute(amt_needed, chem):
    global reactions
    global excess
    global results

    if chem == 'ORE':
        results += amt_needed
    else:
        reaction_data = reactions[chem]
        n_pack = reaction_data[0]
        reactant_list= reaction_data[1]

        if chem in excess and excess[chem] >= amt_needed:
            excess[chem] -= amt_needed
        else:
            if chem in excess:
                amt_needed -= excess[chem]
                excess[chem] = 0

            whole_units = math.ceil(amt_needed/n_pack)
            left = (whole_units * n_pack) - amt_needed

            if left > 0:
                if chem not in excess:
                    excess[chem] = left
                else:
                    excess[chem] +=  left
            for reactant in reactant_list:
                compute(reactant[0] * whole_units, reactant[1])


reactions = load_data()
excess = {}
results = 0
for r in reactions:
    print(r + "<=" + str(reactions.get(r)))

compute(1,'FUEL')
print(results)
s

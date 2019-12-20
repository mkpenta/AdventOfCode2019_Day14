import math


def wordnumpair(l):
    k = l.strip(" ")
    k = k.split(" ")
    word = str(k[1])
    num = int(k[0])
    return word, num


def load_data():
    data = {}
    ores = {}
    f = open("input")
    lines = f.readlines()
    for line in lines:
        print(line)
        l = line[:-1]
        l = l.split("=>")
        e = (key, count) = wordnumpair(l[1])
        if key not in data:
            data[key] = (count, [])
        else:
            data[key][1].append(e)
        c = l[0].split(", ")
        for u in c:
            e = (word, count) = wordnumpair(u)
            data[key][1].append(e)

    return data






def decompose(reactions, current, coef, result):
    print("Current={0}\n\tCeof={1}".format(current, coef))
    if type(current) == tuple and type(current[1]) == list:
        terms = current[1]
        for t in terms:
            val = reactions[t[0]]
            l = val[1]
            if l[0][0] == "ORE":
                result.append((t[0], coef * t[1]))
            else:
                unit = val[0]
                qty = t[1] * coef
                c = math.ceil(qty/unit)
                decompose(reactions, reactions[t[0]],c, result)


def find_like_terms(p):
    result= {}
    for term in p:
        if term[0] in result:
            result[term[0]] += term[1]
        else:
            result[term[0]] = term[1]
    return result

def calc_ores(reactions, dic):
    ores = 0
    for entry in dic:
        val = reactions[entry]
        m = math.ceil(dic[entry] / val[0])
        ores += m * val[1][0][1]
        print("val={0} coef={1}".format(val, m * val[1][0][1]))
    return ores


reacts = load_data()
for r in reacts:
    print(r + "<=" + str(reacts.get(r)))



primary = []
decompose(reacts, reacts['FUEL'], 1, primary)
print(primary)
primary.sort(key=lambda x: x[0])
print(primary)
simple = find_like_terms(primary)
print(simple)
o = calc_ores(reacts, simple)
print(o)

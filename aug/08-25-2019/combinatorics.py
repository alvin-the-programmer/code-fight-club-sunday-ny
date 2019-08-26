def combinations(master_list):
    if len(master_list) == 0: return [[]]
    el = master_list[0]
    rest = master_list[1:]
    without_el = combinations(rest)
    with_el = [ comb + [el] for comb in without_el ]
    return with_el + without_el

print(combinations(['a', 'b', 'c']))


def permutations(master_list):
    if len(master_list) <= 1:
        return [ master_list ]
    el = master_list[0]
    rest = master_list[1:]
    perms_without = permutations(rest)

    perms_with = []
    for perm in perms_without:
        for i in range(len(perm) + 1):
            before = perm[:i]
            after = perm[i:]
            perm_with = before + [el] + after
            perms_with.append(perm_with)
    return perms_with

print(permutations(['a', 'b', 'c']))


"""
RANDO CODE

list_1 = ['a', 'b', 'c']
for r in enumerate(list_1):
    [i, el] = r
    print(i)
    print(el)

tup = [1,2]
tup[0] = 5
print(tup)

list_2 = [1, 2]
s = "abcdef"
s[1] = "z"
print(s)

for el_1 in list_1:
    for el_2 in list_2:
        print([ el_1, el_2 ])

cross_pairs = [ [ el_1, el_2 ] for el_1 in list_1 for el_2 in list_2]
print (cross_pairs)

"""

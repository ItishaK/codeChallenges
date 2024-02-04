from itertools import permutations

nums = [1,2,3]

perm_lst = permutations(nums)
perm_lst2 = []
for item in perm_lst:
    perm_lst2.append(list(item))

print('All permutations: ',perm_lst2)
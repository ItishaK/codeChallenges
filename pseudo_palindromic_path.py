#from collections import Counter
#from itertools import permutations

# TreeNode{val: 2, left: TreeNode{val: 3,
# 					left: TreeNode{val: 3, left: None, right: None},
# 					right: TreeNode{val: 1, left: None, right: None}},
# 				 right: TreeNode{val: 1, left: None,
# 					right: TreeNode{val: 1, left: None, right: None}}}


path_lst = []
final_path = []
unique_lst = []
final_lst = []
global count
count = 0


class node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getTreePaths(root):
    # list to store path
    path = []
    temp_path = []
    # nonlocal count
    # count = 0
    #global count
    getTreePathsRec(root, path, 0, 0, temp_path)

def getTreePathsRec(root, path, pathLen, temp, temp_path) -> int:
    # Base condition - if binary tree is
    # empty return
    global count
    if root is None:
        return

    if root.val in path:
        temp = root.val
        temp_path.clear()
        temp_path.extend(path)
        #print(f'path is: {path}')
        #print(f'temp path is: {temp_path}')
        #print(f'Root found in path and temp value is {temp}')
        path.remove(root.val)
        pathLen = len(path)
    else:
        temp_path.clear()
        temp_path.extend(path)
        if len(path) == pathLen + 1:
            path[pathLen] = root.val
        elif len(path) > pathLen + 1:
            path[pathLen] = root.val
            for i in range(pathLen + 1, len(path)):
                path.pop()
        else:
            path.append(root.val)
        pathLen += 1

    if root.left is None and root.right is None:
        # if len(path) <= 1:
        #     count += 1
        # print('path: ',path)

        path_lst = path.copy()
        print('path_lst: ', path_lst)

        if len(path_lst) <= 1:
            count += 1
            print(f'count is {count}')
            #final_path.append((path_lst))

        path.clear()
        path.extend(temp_path)

        # if len(temp_path) > 0 and len(path) > 0:
            #print(f'temp value is {temp}')
            #path.remove(path[-1])
            # path.clear()
            # path.extend(temp_path)
            #print(f'Updated paths: {path}')

        #path.clear()
        # final_path.append((path_lst))
        # count = 0
        # path_freq = Counter(path_lst)
        # for value in path_freq.values():
        #     if count <= 1:
        #         if value & 1 == 1:
        #             count += 1
        #         # if value % 2 != 0:
        #         #     count += 1
        #     else:
        #         break
        # if count <= 1:
        #     final_path.append((path_lst))
    else:
        # try for left and right subtree
        getTreePathsRec(root.left, path, pathLen, temp, temp_path)
        getTreePathsRec(root.right, path, pathLen, temp, temp_path)



'Check for 1st root path'
# root = node(2)
# root.left = node(3)
# root.right = node(1)
# root.left.left = node(3)
# root.left.right = node(1)
# root.right.right = node(1)

'Check for 2nd root path'
# root = node(2)
# root.left = node(1)
# root.right = node(1)
# root.left.left = node(1)
# root.left.right = node(3)
# root.left.right.right = node(1)

'Check for 3rd root path'
# root = node(9)

'Check for 4th case'
root = node(8)
root.left = node(8)
root.left.left = node(7)
root.left.right = node(7)
root.left.right.left = node(2)
root.left.right.right = node(4)
root.left.right.left.right = node(8)
root.left.right.left.right.right = node(1)
root.left.right.right.right = node(7)

'Check for 5th case'


'Check for None root path'
# root = None

getTreePaths(root)
print(f'Total Palindromes: {count}')

#print('Final Tree Paths: ', final_path)
#print(f'pseudo-palindromes found: {len(final_path)}')
#pal_lst = []

#print('palindrome list: ', final_path)
#count_pal = 0
# for item in final_path:
#     unique_set = set(permutations(item))
#     unique_lst = list(unique_set)
#     for lst_val in unique_lst:
#         lst_val = list(lst_val)
#         if lst_val == list(reversed(lst_val)):
#             count_pal += 1
#             break
#     final_lst.append(item)

# print('Unique list: ',unique_lst)
# print('No. of palindromes found in a binary tree: ', len(final_path))

#print('Palindromes found are: ',final_lst)


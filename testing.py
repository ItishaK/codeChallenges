

# a = lambda x,y : x/y
# b = lambda x,y: x//y
#
# print('output with floor division: ',a(5,2))
# print('output with precise division: ',b(5,2))



# ip_list = [2,8,19,45,2,0,1,19]
# deleted_vals = []
# list_len = len(ip_list) - 1
# print('Original input list: ',ip_list)
#
# temp = ip_list.pop(4)
# print('after popping elements: ',ip_list)
# ip_list.insert(list_len,temp)
# print('list after inserting: ',ip_list)

list1 = []
def some_func(array):
    print('array at start: ',array)
    array = iter(array)
    print('array iterator: ',array)
    try:
        first = next(array)
        print('first 1st: ', first)
    except StopIteration:
        print('I am inside exception')
        return True
    #print('final statement: ',all(first == x for x in array))
    #print('first == x for x in array: ',)
    #list1.append((first == x for x in array))
    for x in array:
        print('x is : ',x)
    print('first: 2nd', first)
    return all(first == x for x in array)

output = some_func([0,1,1,1,1])
print('output: ',output)

print('list: ',list1)



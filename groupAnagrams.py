
input_list = ["eat","tea","tan","ate","nat","bat"]
#input_list = ["eat","", "ate"," ","a"]
list_len = len(input_list)
sorted_list = []
unique_list = []
op_list2 = []
op_list3 = []

for item in input_list:
    temp_str = "".join(sorted(item))
    sorted_list.append(temp_str)

unique_set = set(sorted_list)
print('unique set: ',unique_set)
unique_list = (list(unique_set))
print('unique list: ',unique_list)

for i in range(len(unique_list)):
    op_list2 = []
    for j in range(len(sorted_list)):
        if unique_list[i] == sorted_list[j]:
            op_list2.append(input_list[j])
    op_list3.append(op_list2)

print("output list: ",op_list3)



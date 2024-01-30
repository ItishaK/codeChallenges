word1 = "applesaregood"
word2 = 'oranges'
list_w1 = [*word1]  ## split through unpacking
list_w2 = [*word2]
len_w1 = len(list_w1)
len_w2 = len(list_w2)
print(list_w1)
print(list_w2)

final_list = []
if len_w1 == len_w2:
    for i in range(len_w1):
        final_list.append(list_w1[i])
        final_list.append(list_w2[i])
elif len_w1 < len_w2:
    for i in range(len_w1):
        final_list.append(list_w1[i])
        final_list.append(list_w2[i])
    temp = "".join(list_w2[len_w1:])
    print("temp: ", temp)
    final_list.append(temp)
elif len_w1 > len_w2:
    for i in range(len_w2):
        final_list.append(list_w1[i])
        final_list.append(list_w2[i])
    temp = "".join(list_w1[len_w2:])
    print("temp: ", temp)
    final_list.append(temp)

print("list_w2[len_w1+1:] ", list_w2[len_w1:])
print('final_list: ', final_list)
final_word1 = "".join([str(item) for item in final_list])
final_word2 = "".join(final_list)

if final_word1 == final_word2:
    print('matching values')
else:
    print('donot match')

#print(final_word)

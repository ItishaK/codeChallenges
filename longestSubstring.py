
input = "dvdf"
list_ip = [*input]
lengths = []
temp_str = []

print("list input: ",list_ip)
print("temp_str: ",temp_str)
print('length of input: ',len(list_ip))
loop_len = len(list_ip) - 1
print('loop len: ',loop_len)

if len(list_ip) == 0:
            lengths.append(0)
elif len(list_ip) == 1:
            lengths.append(1)
else:
    temp_str.append(list_ip[0])
    for i in range(loop_len):
        counter = 0
        for j in range(len(temp_str)):
            if temp_str[j] == (list_ip[i + 1]):
                counter = 1
                if temp_str[-1] == list_ip[i + 1]:
                    lengths.append(len(temp_str))
                    temp_str.clear()
                    temp_str.append(list_ip[i + 1])
                else:
                    temp_str = temp_str[j+1:]
                    temp_str.append(list_ip[i + 1])
                    lengths.append(len(temp_str))
                break

        if counter == 0:
            temp_str.append(list_ip[i + 1])
            lengths.append(len(temp_str))

print("substring lengths found are: ",lengths)
print("Longest Substring: ",max(lengths))

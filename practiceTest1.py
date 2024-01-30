
#X = [0,1,0,1,0]
X = [0,0,0,0,0,0]

temp_substr = []
lengths = []
lengths.append(0)
loop_len = len(X) - 1
if len(set(X)) == 1:
    lengths.append(1)
for i in range(loop_len):
        if X[i] != X[i+1]:
            if temp_substr == []:
                temp_substr.append(X[i])
                temp_substr.append(X[i+1])
                lengths.append(len(temp_substr))
            else:
                temp_substr.append(X[i+1])
                lengths.append(len(temp_substr))
        elif X[i] == X[i+1]:
            temp_substr.clear()
            #break

count = max(lengths)
print('count is : ',count)
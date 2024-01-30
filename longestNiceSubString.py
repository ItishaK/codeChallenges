s = "abABayzo"
len_s = len(s)
final_str = ""
for i in range(len(s)):
    # print("ascii value of ",i," is: ",ord(s[i]))
    temp1 = s[i]
    print('temp1: ', temp1)
    if (temp1.islower()):
        if (temp1.upper() in s):
            # print('temp1 upper value found')
            temp_idx = s.index(temp1.upper())
            print('temp_idx: ', temp_idx)
            temp_substr = s[i:temp_idx + 1]
            print('temp_substr: ', temp_substr)
            final_str = temp_substr

    print('final substring: ', final_str)
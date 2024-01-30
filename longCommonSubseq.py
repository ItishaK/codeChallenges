# text1 = "abcde"
# text2 = "abcdefgh"

# text1 = "ezupkr"
# text2 = "ubmrapg"

text1 = "abcba"
text2 = "abcbcba"

# text1 = "oxcpqrsvwf"
# text2 = "shmtulqrypy"

# text1 = "bsbininm"
# text2 = "jmjkbkjkv"

# text1 = "abc"
# text2 = "abc"

# text1 = "abc"
# text2 = "def"

subseq_len = []
flag = False
#st_ind = 0
list1 = [*text1]
# print(f'list1 is {list1}')
list2 = [*text2]
# print(f'list2 is {list2}')

if text1 == text2:
    subseq_len = [len(text1)]
else:
    for j in text2:
        if j in text1:
            flag = True
            break
    if flag:
        #print('sub sequence exists')
        # if len(text1) >= len(text2):
        for i in range(len(list2)):
            st_ind = 0
            temp = 0
            for j in range(i, len(list2)):
                for k in range(len(list1)):
                    if list2[j] in list1[k:] and k < len(list1):
                        # print(f'sequence length: {subseq_len} and start index was {st_ind}')
                        print(f'Matching character is {list2[j]}')
                        # if st_ind < len(text1):
                        temp += 1
                        #st_ind = list1.index(list2[j]) + 1
                        #print(f'sequence length: {subseq_len} and start index is {st_ind}')
                    elif k >= len(list1):
                        subseq_len.append(temp)
                        break
            subseq_len.append(temp)
    else:
        subseq_len = [0]

print(f'Subsequence length list is {subseq_len}')
print(f'Subsequence length is {max(subseq_len)}')

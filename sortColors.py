
ip_arr = [2,0,2,1,1,0]
#ip_arr = [2,0,1]

for i in range(len(ip_arr)):
    for j in range(i+1,len(ip_arr)):
        if ip_arr[i] >= ip_arr[j]:
            ip_arr[i],ip_arr[j] = ip_arr[j],ip_arr[i]

print('output: ',ip_arr)

# for i in range(len(ip_arr)):
#     j = i+1
#     for j in range(len(ip_arr)):
#         if ip_arr[i] > ip_arr[j]:
#             tmp = ip_arr[j]
#             ip_arr.insert(j,ip_arr[i])
#             ip_arr.insert(i,tmp)
#         elif ip_arr[i] == ip_arr[j]:
#             tmp = ip_arr.pop(j)
#             ip_arr.insert(i+1, ip_arr[j])





print("final output: ",ip_arr)
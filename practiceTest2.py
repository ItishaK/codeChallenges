
X = [1,4,5]
Y = [2,3,5]
S = [2,3,5]

dist = {}
count = 0
output = []

loop_len = len(S)
if len(X) < len(S):
    loop_len = len(X)
elif len(X) > len(S):
    loop_len = len(S)

for i in range(len(X)):
    dist[i] = []
    for j in range(len(Y)):
        if dist[i] == []:
            dist[i] = [(abs(X[i] - Y[j]))]
        else:
            dist[i] += [(abs(X[i] - Y[j]))]

# S = [2,3,5]

for i in range(len(S)):
    for j in range(len(dist)):
        count = 0
        for k in range(len(dist[j])):
            if dist[j][k] <= S[i]:
                count += 1
                #print('diff: ',diff)
    output.append(count)

print('output: ',output)
print('Distance metrics: ', dist)
print('dist[0][0]: ',dist[0][0])
print('dist[0][0]: ',dist[0][1])
print('dist[0][0]: ',dist[0][2])

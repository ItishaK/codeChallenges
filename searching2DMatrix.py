matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 55

# print('input matrix: ', matrix)
# print('no. of rows: ',len(matrix))
# print('no. of cols: ',len(matrix[0]))

rows = len(matrix)
cols = len(matrix[0])
counter = 0

for i in range(rows):
    print('Current value checked: ',matrix[i][cols-1])
    if target <= matrix[i][cols-1]:
        for j in range(cols):
            if target == matrix[i][j]:
                counter = 1
                break
    if counter == 1:
        break

if counter == 0:
    print("False")
else:
    print("True")



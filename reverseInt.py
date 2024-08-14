# Reverse an integer value
# Solution:
    
num = -123
reverse_num = ''
if str(num)[0] == '-':
    reverse_num = str(num)[1:]
    reverse_num = int('-'+ reverse_num[::-1])
else:
    reverse_num = int(str(num)[::-1])
    
print(reverse_num)
print(type(reverse_num))



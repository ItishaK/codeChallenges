
input = -123
min_val = -2**31
max_val = 2**31 - 1
#print(f'min val is {min_val} and max val is {max_val}')
if input <= max_val or input >= min_val:

    if input < 0:
        inp_str = str(input)
        #print(f'string is {inp_str} and len is {len(inp_str)}')
        a = inp_str[::-1]
        # print(f'a is {a}')
        # print(f'{inp_str[0]}{a[:-1]}')
        temp = inp_str[1:]
        #output = -abs(int(temp[::-1]))
        output = int(inp_str[0] + a[:-1])
    else:
        inp_str = str(input)
        rev_str = inp_str[::-1]
        output = int(rev_str)

print(f'reversed int value is {output}')
print(f'{type(output)}')


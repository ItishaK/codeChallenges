
from collections import Counter

input = "aaabbbbbbddddddcfe"

list_ip = [*input]

dict_ip = Counter(list_ip)
print(f"op is dict {dict_ip}")
max_val = max(dict_ip.values())
output = [i for i in dict_ip if dict_ip[i] == max_val]



print(f'Max repeated alphabet is {output} ')



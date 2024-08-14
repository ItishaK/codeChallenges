url_list = ['www.a.com','www.b.com','www.c.com','www.d.com']
email_list = ['user1@a.com','user2@b.com','user5@d.com','user3@a.com','user4@a.com']
sorted_dict = {}

for item in url_list:
    key = ".".join(item.split('.')[1:])
    sorted_dict[item] = []
    for value in email_list:
        temp = value.split('@')[1]
        if temp == key:
            sorted_dict[item] += [value]

print(sorted_dict)

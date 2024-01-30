url_list = ['www.a.com','www.b.com','www.c.com','www.d.com']
email_list = ['user1@a.com','user2@b.com','user5@d.com','user3@a.com','user4@a.com']

email_url_dict = {}

for i in range(len(url_list)):
    temp_substr = url_list[i]
    #temp_substr = temp_substr[4:]
    temp_substr = ".".join(url_list[i].split('.')[1:])
    #print("updated substring value: ",temp_substr1)
    email_url_dict[url_list[i]] = []
    for j in range(len(email_list)):
        ind = email_list[j].index('@')
        temp = email_list[j]
        temp = temp[ind+1:]
        if temp_substr == temp:
            print('email_list[j]: ',email_list[j])
            if email_url_dict[url_list[i]] == []:
                email_url_dict[url_list[i]] = [email_list[j]]
            else:
                email_url_dict[url_list[i]] += [email_list[j]]

print('final dictionary: ',email_url_dict)
list1 = email_url_dict.keys()
print('all keys: ',list1)
#print('key1: ',list1[1])
email_id = 'saketh@codegnan.com'
print(email_id[7:15])
email_ids = ['meghana@gmailcom','meena@gmail.com','charan@gmail.com','jaya@gmail.com']
print(len(email_ids))
print(email_ids[3])
email_ids.extend(['hello@gmail.com','maggi@gmail.com'])
print(email_ids)
'''
for mail in email_ids:
    print(f"Mail id is {mail}")

users =dict.fromkeys(email_ids)
users['jaya@gmail.com'] = 21
print(users)

for i in range(len(email_ids)):
    users[i+1] = email_ids[i]
print(users
'''
users = dict(enumerate(email_ids,1))
print(users)

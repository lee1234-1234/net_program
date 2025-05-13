d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

# 1. Print names of users whose phone number ends with 8
print("Users with phone numbers ending in 8:")
for user in d:
    if user['phone'].endswith('8'):
        print(user['name'])

# 2. Print names of users who do not have an email
print("\nUsers without an email:")
for user in d:
    if not user['email']:
        print(user['name'])

# 3. Input a name and print the phone and email
name_to_search = input("\nEnter a name to search: ")
found = False
for user in d:
    if user['name'].lower() == name_to_search.lower():
        print(f"Phone: {user['phone']}, Email: {user['email']}")
        found = True
        break

if not found:
    print("이름이 없습니다")
    
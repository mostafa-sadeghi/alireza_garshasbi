# dictionary

# persons = {}
# print(type(persons))


# persons = {
#     'ali': 'footbal',
#     'reza': 'tennis'
# }

# print(persons['ali'])
# del persons['ali']
# persons['mahmoud'] = 'pingpong'
# print(persons)
customers = []
customer = {
    'name': '',
    'family': '',
    'age': 0
}


# name1 = input('enter your name:> ')
# family1 = input('enter your family:> ')
# age1 = input('enter your age:> ')

# customer['name'] = 'name1'
# customer['family'] = 'family1'
# customer['age'] = 'age1'

# customers.append(customer)


# name1 = input('enter your name:> ')
# family1 = input('enter your family:> ')
# age1 = input('enter your age:> ')
# customer = {}
# customer['name'] = 'name2'
# customer['family'] = 'family2'
# customer['age'] = 'age2'

# customers.append(customer)

# print(customers)
# print(customers[0]['name'])


# loops in python

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(f'number is :', number)

# i = 0
# while i < len(numbers):
#     print(f'number {i+1}/{len(numbers)}', numbers[i])
#     i += 1

# string = 'ali'
# for s in string:
#     print(s, end='\t')

# t = (1, 2, 3, 45)
# for item in t:
#     print(item)


# customer = {
#     1: 1,
#     2: 'ali',
#     3: 'rezaei',
#     4: 'A',
# }

# for item in customer:
#     print(item)
# for item in customer.values():
#     print(item)
# for key, val in customer.items():
#     print(f'{key} is : {val}')

# print(len(customer))
# counter = 0

# while counter < len(customer):
#     print(f'{customer[counter+1]}')
#     counter += 1


# customer = {
#     'id': 1,
#     'name': 'ali'
# }


# while True:
#     key = input('enter key or "exit" to exit: ')
#     if key == "exit":
#         exit()
# print(customer[key])
# print(customer.get(key))


# customer = {}
# customers = []
# while True:
#     print('''to enter a customer enter 1.
#     to exit enter 2.
#     to search a customer enter 3
#     to show all customers enter 4
#     ''')
#     entry = input('> ')
#     if entry == '1':
#         while True:
#             entry2 = input('enter "r" to return or "a" to add')
#             if entry2 == "a":
#                 name = input('enter a name: ')
#                 family = input('enter a family: ')
#                 age = input('enter a age: ')
#                 customer = {}
#                 customer['name'] = name
#                 customer['family'] = family
#                 customer['age'] = age

#                 customers.append(customer)
#             elif entry2 == "r":
#                 break

#     elif entry == '2':
#         exit()
#     elif entry == '3':
#         name = input('enter a name : ')
#         for customer in customers:
#             print('****************')
#             print(customer)
#             for key in customer.keys():
#                 if customer.get(key) == name:
#                     print(f'{name} exists')

#                     break

#     elif entry == '4':
#         print(customers)


# for i in range(5):
#     pass

# break keyword
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# print('end')


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# print('end')

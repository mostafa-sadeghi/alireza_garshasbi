# File
# try:
# file = open("f.txt", "a")
# for i in range(2):
#     name = input('enter a name:> ')
#     file.write(name + '\n')

# file = open("f.txt", "r")
# print(file.read())
# for line in file:
#     print(line[:-1], end=' ')
# file.close()
#     with open("f.txt", 'r') as f:
#         print(f.read())

# except:
#     print("error")

# print('other')


# with open('e:/f.txt', 'r') as f:
#     print(f.read())


# Set

# numbers1 = {1, 2, 3, 4, 5, 6}
# numbers2 = {4, 2, 3, 1, 5, 6}
# numbers = {}
# print(type(numbers))
# print(numbers1 == numbers2)

# numbers1 = [1, 2, 3]
# numbers2 = [3, 1, 2]
# print(numbers1 == numbers2)

# set is mutable but it's items are immutabe
# numbers1 = {1, 2, 3, 4, 5, 6}
# numbers2 = {4, 2, 3, 1, 5, 6}

# numbers1.add(11)
# numbers1.remove(6)
# print(numbers1)

# numbers1 = {(1, 2), 2, 3, 4, [2, 3], 6} =>error
# numbers1 = {(1, 2), 2, 3, 4, 'a', 6}

# numbers = {1, 1, 2, 3, 4, 4, 5, 6, 7}

# print(numbers)


# numbers = [1, 2, 3, 4, 4, 5]
# new_numbers = list(set(numbers))
# print(new_numbers)


# numbers1 = {1, 2, 3, 4}
# numbers2 = {1, 'four', 2, 3}
# numbers2 = {3, 4, 5, 6, 7}

# numbers = numbers1.union(numbers2)
# print(numbers)
# numbers = numbers1 | numbers2
# print(numbers)

# numbers = numbers1.intersection(numbers2)
# print(numbers)
# numbers = numbers1 & numbers2
# print(numbers)

# numbers = numbers1.difference(numbers2)
# print(numbers)
# numbers = numbers1 - numbers2
# print(numbers)

# numbers1 = {1, 2, 3, 4, 5}
# numbers2 = {1, 2}
# print(numbers2.issubset(numbers1))
# print(numbers2 <= numbers1)
# print(numbers1.issuperset(numbers2))
# print(numbers1 >= numbers2)


# import unittest


# def add(n1, n2):
#     return n1 + n2


# assert add(1, 2) == 3, 'Expected 3'


# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(1, 2), 3, 'some thing')


# unittest.main()


# debug


def func():
    total = 0
    for i in range(5):
        total += i
        print(i)
        print(total)
    return total


print(func())

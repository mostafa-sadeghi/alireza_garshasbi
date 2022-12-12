# xxargs kwargs

# def save_user(**user):
#     return user


# x = save_user(id=1, name="ali", age=30)
# print(x)

# scope

# x = 0

# counter = '0'


# def greet():
#     global counter
#     counter += 1
#     # message = ''
#     # return counter


# greet()
# greet()
# greet()
# print(counter)
# print(message)  # name error because message is local variable(in function scope)


# def apply_to_each(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
#     return L


# l = apply_to_each([1,-2,-3,4], abs)
# print(l)
# l = apply_to_each([1,-2.2,-3.2,4], int)
# print(l)
# l = apply_to_each([1,-2,-3,4], float)
# print(l)


# def applyFuns(L, x):
#     values = []
#     for f in L:
#         values.append(f(x))
#     return values


# x = applyFuns([abs, int, float], -2.2)
# print(x)


# numbers = list(range(1000))
# print(numbers)

# numbers = []
# for i in range(1000):
#     numbers.append(i)
# print(numbers)

# zeros = [0] * 1000
# print(zeros)


# numbers = ()
# for i in range(1000):
#     numbers += (i,)

# print(numbers)

# map function
# output = map(abs, [1, -1, 2, -4])
# print(output)
# for number in output:
#     print(number)
# my_list = list(output)
# print(my_list)

# l1 = [1, 2, 3, 4]
# l2 = [5, 1, 6, 2, 11]
# output = list(map(min, l1, l2))
# print(output)


# def mul(a, b):
#     res = 0
#     while b > 0:
#         res += a
#         b -= 1
#     return res

# def mul(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mul(a, b-1)


# print(mul(2, 3))



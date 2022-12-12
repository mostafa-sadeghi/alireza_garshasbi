# def outer_func():
#     def inner_func():
#         return 'inner func'
#     return inner_func()


# print(outer_func())


# string = 'aBc'
# print(string.upper())
# print(string.lower())


# string = 'abc'
# char = 'z'
# for s in string:
#     if char == s:
#         print('ok')
# print(char in string)


# numbers = [1, 2, 3, 4]
# print(1 in numbers)
# print(5 in numbers)
# numbers = (1, 2, 3, 4)
# print(1 in numbers)
# print(5 in numbers)


# student = {
#     'id': 1,
#     'name': 'ali'
# }

# print('ali' in student.values())

# logical operators : and or not

a = 22
# if 10 < a < 30:
#     print('sth')

# if a > 10 and a < 30:
#     print('sth')
# if a > 10 or a < 30:
#     print('sth')


# Truthy and falsy values

# if '':  # empty string is Falsy Value
#     print('ok')
# if ' ':  # not empty string is Truthy Value
# print('ok')
# Falsy values : '', 0, [], (),{},None

# if 0: # if bool(0)
#     print('sth')
# if 1:
#     print('sth')


# print('' and 'hello')
# print('sss' and 'hello')
# print('sss' and 'hello' and 'sth')
# print('' or 'hello')
# print('' or 'hello' or 'sssss')

def is_palindromic(s):
    def to_char(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_char(s))


x = 'abaaba'
print(is_palindromic(x))
print(is_palindromic('abacba'))

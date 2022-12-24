# from array import array
# my_list = [1, 'a', [1, 2], (1, 2), {"id": 1}]
# print(type(my_list))

# numbers = array('i', [1, 2, 3, 4])
# print(numbers)
# print(type(numbers))


# 2d arrays

matrix = [[1, 22, 3], [4, 51, 6], [7, 18, 99], [10, 11, 12]]
# print(matrix[0][0])
# print(matrix[1][0])
# print(matrix[2][0])
# print(matrix[3][0])


def get_size(matrix):
    return len(matrix), len(matrix[0])


# numbers = []
# # numbers[0] = 1
# numbers.append(1)
# print(numbers[0])


# list comprehension

# numbers = [x**2 for x in range(1001) if x % 2 == 0]
# print(numbers)


def transpose(matrix):
    m, n = get_size(matrix)  # m= 2 , n= 3
    t = [[0]*m for i in range(n)]
    # t = [[0,0],[0,0],[0,0]]
    for i in range(m):
        for j in range(n):
            t[j][i] = matrix[i][j]
    return t


print(transpose(matrix))

# transpose(matrix)
# print(get_size(matrix))


def max_value(matrix):
    rows, cols = get_size(matrix)
    max_val = matrix[0][0]
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > max_val:
                max_val = matrix[row][col]
        return max_val


print(max_value(matrix))


def show_matrix(matrix):
    for row in matrix:
        # print(row)
        for cell in row:
            print(f'{cell:<4}', end=' ')
        print()


# show_matrix(matrix)

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)   # True (values are equal)
# print(a is b)   # False (different memory locations)






# # Regular way:
# squares = []
# for i in range(10):
#     squares.append(i * i)

# # List comprehension:
# squares = [i * i for i in range(10)]








# def func(a, L=[]):
#     L.append(a)
#     return L

# print(func(1))  # [1]
# print(func(2))  # [1, 2]
# print(func(3))  # [1, 2, 3]







# # Normal function
# def add(x, y):
#     return x + y

# # Lambda function
# add = lambda x, y: x + y
# print(add(3, 5))  # Output: 8




# A decorator is a function that modifies the behavior of another function without changing its code.

# def decorator_func(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @decorator_func
# def greet():
#     print("Hello!")

# greet()




# A generator is a function that yields items one at a time using yield keyword, instead of returning all at once.
# def gen():
#     for i in range(3):
#         yield i

# g = gen()
# print(next(g))  # 0
# print(next(g))  # 1
# print(next(g))  # 2







# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# finally:
#     print("This block always runs.")





# Writing to a file
with open("data.txt", "w") as file:
    file.write("Hello Areeba!")

# Reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

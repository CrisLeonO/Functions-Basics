# 1
def number_of_food_groups():
    return 5


print(number_of_food_groups())
# output: 5
print('2' * 10)


# 2
def number_of_military_branches():
    return 5


print(
    # number_of_days_in_a_week_silicon_or_triangle_sides() +
    number_of_military_branches())
# output: none
# output: 5
print('3' * 10)


# 3
def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())
# output: 5
print('4' * 10)


# 4
def number_of_fingers():
    return 5
    print(10)


print(number_of_fingers())
# output: 5, el 10 lo omite ya que esta retornando solo 5
print('5' * 10)


# 5
def number_of_great_lakes():
    print(5)


x = number_of_great_lakes()
print(x)
# output: 5 y none porque no se esta haciendo un return
print('6' * 10)


# 6
def add(b, c):
    print(b+c)


print(add(1, 2) + add(2, 3))
# output: 3, 5, y genera un error por el operador de suma
print('7' * 10)


# 7
def concatenate(b, c):
    return str(b)+str(c)


print(concatenate(2, 5))
print(concatenate(2, 5))
# output: 25 // 25
print('8' * 10)


# 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
        return 7


print(number_of_oceans_or_fingers_or_continents())
# output: 100 // 10
print('9' * 10)


# 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
        return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) +
      number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))

# output: 7 // 14 // 21
print('10' * 10)


# #10
def addition(b, c):
    return b+c
    return 10


print(addition(3, 5))
# output: 8
print('11' * 10)


# 11
b = 500
print(b)


def foobar():
    b = 300


print(b)
print(b)
foobar()
print(b)
# output: 500 // 500 // 500 //  none // 500
print('12' * 10)


# 12
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)
# output: 500 // 300 // 500 // 500
print('13' * 10)


# 13
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
b = foobar()
print(b)
# output: 500 // 300 // 500 // 300
print('14' * 10)


# 14
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)
    foo()


# output: 1 // 3 // 2
print('15' * 10)

# 15


def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)
# output: 1 // 3 // 5 // 10

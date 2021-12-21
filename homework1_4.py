while True:
    n = input("Please, enter positive integer number:")

    if n.isdigit():
        break

n = int(n)
big = 0

while n != 0:
    if n % 10 > big:
        big = n % 10

    n = n // 10

print(f"Самая большая цифра: {big}")

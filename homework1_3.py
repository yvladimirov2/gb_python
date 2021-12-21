while True:
    n = input("Please, enter positive integer number:")

    if n.isdigit():
        break

nn = n + n
nnn = n + n + n

print(int(n) + int(nn) + int(nnn))

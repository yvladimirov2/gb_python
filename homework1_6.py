a = int(input("First day result:"))
b = int(input("Last day result:"))
count = 0

if a < b:
    while a < b:
        a = a * 1.1
        count += 1
    print(f"Days for final result: {count}")

elif a > b:
    print("You are degradating!")

else:
    print("You are already there. 0 days.")
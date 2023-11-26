n = int(input("Enter a number: "))

if 0 <= n <= 20:
    for i in range(n):
        print(i ** 2)
else:
    print("Please enter a non-negative integer.")
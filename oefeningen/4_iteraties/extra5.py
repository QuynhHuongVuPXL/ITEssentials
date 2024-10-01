num1 = 1
num2 = 1
next_number = num2

print(num1, end=" ")
print(num2, end=" ")

for i in range(1500):
    next_number = num1 + num2
    num1 = num2
    num2 = next_number

    if next_number < 1500:
        print(next_number, end=" ")



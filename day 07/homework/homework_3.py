numbers = [24, 9, 15, 162, 9, 4, 9, 7, 100, 67]
num_1 = int(input("enter your number: "))
sumer = 0
numbers.append(num_1)

for i in numbers:
    sumer += i
print(sumer)
print(sum(numbers))
print(numbers)
list = [1,6,8,4,30,2,7,12,10,3,16,29,50,5]

divisible_by_3 = []

for num in list:
    if num % 3 == 0:
        divisible_by_3.append(num)

print(divisible_by_3)
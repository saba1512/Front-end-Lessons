list = [1,6,8,4,2,7,12,10,3,16,29,50,5]

even_count = 0
odd_count = 0

for num in list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)
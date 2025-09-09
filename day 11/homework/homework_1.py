# ამ სიიდან list = [1,6,8,4,30,2,7,12,10,3,16,29,50,5] იპოვე ყველა  ლუწი და კენტი ციფრები ასევე დაალაგე თანმიმდევტობით და იპოვე პირველი და ბოლო ციფრი

list = [1,6,8,4,30,2,7,12,10,3,16,29,50,5]

even_count = []
odd_count = []

for num in list:
    if num % 2 == 0:
        even_count.append(num)
    else:
        odd_count.append(num)

sorted_list = sorted(list)

first_number = sorted_list[0]
last_number = sorted_list[-1]

print(even_count)
print(odd_count)
print(sorted_list)
print(first_number)
print(last_number)
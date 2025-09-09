# მოცემული სიიდან list = [1,6,8,4,2,7,12,10,3,16,29,50,5] დათვალე ჯამი for loop ის გამოყენებით, ასევე დათვალე  კენტების ჯამი და დათვალე ლუწების ჯამი  

# მაგ:   

# სულ ჯამია - ? 
# კენტების ჯამია - ?
# ლუწების ჯამია - ?


list = [1,6,8,4,2,7,12,10,3,16,29,50,5]


summer = 0
even_summer = []
odd_number = []

for i in list:
    summer += i

    if i % 2 == 0:
        even_summer.append(i)
    else:
        odd_number.append(i)

print(summer)
print(even_summer) # sum - ჯამი
print(odd_number) #sum -ჯამი 
names = ['Nino', 'GiorGi', 'Lika', 'Ana', 'giGa']
lower_case = []

for i in names:
     lower_case.append(i.lower())

print(lower_case)


entered_num = input("enter your name: ").lower()

if entered_num in lower_case:
     print("Yes")
else:
     print("No")



# numbers = [1,5,2,6,4,9,7]
# print(numbers)

# name = ["saba", "zura", "giga", "gio", "dato", "levani"]
#          0       1       2      3       4        5

#   name[2:4]  - slicing - სლაისინგი
# print(name[2:4])  # ['giga', 'gio']
# print(name[:3])   # ['saba', 'zura', 'giga']

# print(name[0])    # levani  სიიდან პირველი
# print(name[-1])    # levani  სიიდან ბოლო

# print(name[::-1])  # უკუ მიმართულეა  ['gio', 'giga', 'zura', 'saba']

# for i in name:
#     print(i)


# ---------------  append()  -----------------------  
# add_name = input("enter name to add: ")

# name = ["saba", "zura", "giga", "gio", "dato", "levani"]
# name.append(add_name)

# print(name)
# -----------------------------------------------

# ---------------  min() max()  -----------------------  
# numbers = [1,5,2,6,4,9,7,100]
# print(min(numbers))
# print(max(numbers))

# ---------------  sorted() -----------------------  
# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100]

# print(sorted(numbers)[0])
# print(sorted(numbers)[-1])


# ------------------------------------------- 

# word = "gamarjoba chemi saxelia giorgiaaa"
# letter_a = ""

# for i in word:
#     if i != "a":
#         letter_a += i

# print(letter_a)

# ------------------------------------------- 


# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100]

# ewen = []
# odd = []


# for i in numbers:
#     if i % 2 == 0:
#         ewen.append(i)
#     else:
#         odd.append(i)

# print(sorted(ewen))
# print(sorted(odd))

# -----------------------------------------------------------------

# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100, 20, 25]

# div_five = []
# not_five = []


# for i in numbers:
#     if i % 5 == 0:
#         div_five.append(i)
#     else:
#         not_five.append(i)

# print("es ricxvebi iyofa 5 ze", div_five)
# print("sxva ricxvebi", not_five)



# word = "gamarjoba chemi saxelia giorgiaaa"
# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100, 20, 25]

# print(numbers[::-1])


# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100, 20, 25]
# ewen = []

# for i in numbers:
#     print(i * 2)

# for i in numbers:
#     if i % 2 == 0:
#         ewen.append(i)


# print(ewen)


# name = ["saba", "zura", "giga", "gio", "dato", "levani"]
# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100, 20, 25]
# print(len(name))
# print(len(numbers))

# print("siashi aris " + str(len(name)) + " studenti")


# name = ["saba", "zura", "giga", "gio", "dato", "levani"]

# for i in name:
#     print(i + " swavlobs pythons")


# numbers = [1, 5, 2, 152, 6, 4, 9, 7, 100, 20, 25]
# sumer = 0
# for i in numbers:
#     sumer += i

# print(sumer)

# print(sum(numbers))


#  ---------------------------------------

# append()    -  სიაში დამატება
# min()       -  ყველზე პატარა ციფრი სიიდან
# max()       -  ყველზე დიდი ციფრი სიიდან
# sorted()    -  თანმიმდევრულად დალაგება
# len()       -  სიის სიგრძის გამოთვლა
# sum()       -  სიაში არსებული ციფრების ჯამი


# sentence = "gamarjoba chemi saxelia saba"
# sentence += " da vswavlob pythons"

# print(sentence)

sentence = "gamarjoba chemi saxelia saba iii"
letter_i = ""

for i in sentence:
    if i == "i":
        letter_i += i

print(letter_i)


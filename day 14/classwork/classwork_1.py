# list = [1,2,3,4,5,6]
# divisor = 2
# list_even = []

# for i in list:
#     if i % divisor == 0:
#         list_even.append(i)
# print(list_even)


# x = "saba"

# def double_char(x):
#     chars = ""
#     for i in x:
#         chars += i * 4
#     return chars
# print(double_char("saba"))

# ფუნქციაში არ ვიყენებთ print() ვიყენებთ return
# ფუნქცია აუცილებლად უნდა გამოვიძახოთ

# x = " 8hghsaafhhfhsiaaaaihhaauhhaa"

# def find_a(x):
#     s = ""
#     for i in x:
#         if i == "a":
#             s += i
#     return s
# print(find_a(x))
user = input("enter any word: ")
letter = "l"

def count_a(user, letter):
    g = 0
    
    for i in user:
        if i == letter:
            g += 1
    return g
print(count_a(user, letter))






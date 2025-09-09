# list = [1,6,8,4,2,7,12,10,3,16,29,50,5,150]

# list_1 = []

# result = 0

# for i in list:
#     if i % 6 == 0:
#         print(i)
#         list_1.append(i)
#         result += i

# print(list_1)
# print(result)


password = input("enter your password: ")

key = "123"

while True:
    if password == key:
        print("welcome")
        break
    elif password == "exit":
        print("canceled")
        break
    else:
        password = input("enter your password: ")
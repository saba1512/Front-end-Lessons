# 1. უნდა შეიცავდეს მინ 8 სიმბოლო
# 2. უნდა შეიცავდეს მინიმუმ 1 დიდ ასოს
# 3. უნდა შეიცავდეს მინ 1 ციფრს
# 4. თავში და ბოლოში არ შეიძლება იყოს "სფეისები"



# while True:
#     password = input("create password: ")
#     if len(password) < 8:
#         print("enter min 8 symbol: ")
#     else: 
#         for i in password:
#             if i.isdigit():
#                 print("ok")
#                 break
    



while True:
    password = input("create password: ")
    if len(password) < 8:
        print("enter min 8 symbol: ")
    else: 
        has_digit = False
        for i in password:
            if i.isdigit():
                has_digit = True
                break

        if has_digit:
            print("ok")
            break   # ახლა while-მდეც გაჩერდება
        else:
            print("password must contain at least one digit")

# 90 - 100 - A
# 80 - 90 - B
# 70 - 80 - C
# 60 - 70 - D
# 50 - 60 - E
# 0 - 50 - F

# score = int(input("enter your score: "))

# if score > 90 and score <= 100:
#     print("A")
# elif score > 80 and score <= 90:
#     print("B")
# elif score > 70 and score <= 80:
#     print("C")
# elif score > 60 and score <= 70:
#     print("D")
# elif score > 50 and score <= 60:
#     print("E")
# elif score > 0 and score <= 50:
#     print("F")
# else:
#     print("enter 0-100")

# მომხმარებელი გეგმავს მოგზაურობას, და პროგრამამ უნდა შეაფასოს — შესაძლებელია თუ არა გასვლა, და რა პირობებით.

# 🔹 მომხმარებელი შეიყვანს:

# ასაკს
# ბიუჯეტს (ლარებში)
# აქვს თუ არა პასპორტი (კი / არა

# თუ ასაკი < 18 და არ ახლავს მშობელი — დაბეჭდოს "You must be 18+ or accompanied by a parent to travel."
# თუ ბიუჯეტი < 300 — დაბეჭდოს "Insufficient budget for travel."
# თუ პასპორტი არ აქვს  — დაბეჭდოს "International travel requires a passport."

# ყველა პირობის შესრულების შემთხვევაში — დაბეჭდოს "Travel approved. Have a great trip!"

age = int(input("enter your age: "))

if age < 18:
    parent = input("do you have parent: \n1: yes \n2: no\nenter number: ")
    if parent == "1":
        print("ok")
    elif parent == "2":
        print("accompanied by a parent to travel")
    else:
        print("enter 1-2")
else:
    print("your age is ok")

balance = int(input("enter your balance: "))
id = int(input("do you have passport: \n1: yes \n2: no\nenter number: "))
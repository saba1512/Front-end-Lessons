# 1. მომხმარებელს შეეკითხე ასაკი (input()-ით).
# თუ ასაკი 18-ზე მეტია, დაბეჭდე "შენ სრულწლოვანი ხარ".
# თუ 18 ან ნაკლებია, დაბეჭდე "შენ ჯერ არასრულწლოვანი ხარ"


age = int(input("enter your age: "))

if age > 18:
    print("you are adult")
elif age < 1:
    print("enter more than 1")
elif age < 18:
    print("you are not adult")





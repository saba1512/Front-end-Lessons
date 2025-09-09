# 1. მომხმარებელი შეიყვანს 5 რიცხვს. შეინახე სიის სახით და გამოთვალე **საშუალო მნიშვნელობა**.

# 👉 მაგალითად:

# ```
# Enter number 1: 4
# Enter number 2: 8
# Enter number 3: 6
# Enter number 4: 10
# Enter number 5: 2
# Average: 6.0

# ```

# საშუალოს გამოთვლის ფორმულაა რიცხვების ჯამი უნდა გაყო რაოდენობაზე


# 1. მომხმარებელი შეიყვანს 5 რიცხვს. შეინახე სიის სახით და გამოთვალე **საშუალო მნიშვნელობა**.

# numbers = [] # სია რიცხვებისთვის
# for i in range(1, 6): # 1-დან 5-მდე
#     num = float(input(f"Enter number {i}: ")) # ეკითხება რიცხვს
#     numbers.append(num) # დაამატებს სიაში

# average = sum(numbers) / len(numbers) # საშუალოს გამოთვლა
# print(f"Average: {average}") # დაბეჭდავს საშუალოს


numbers = []

i = 1

while i <= 5:
    num = float(input(f"Enter number {i}: ")) # ეკითხება რიცხვს
    numbers.append(num) # დაამატებს სიაში

    i += 1

average = sum(numbers) / len(numbers) # საშუალოს გამოთვლა
print(f"Average: {average}") # დაბეჭდავს საშუალოს
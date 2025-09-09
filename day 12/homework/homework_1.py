# ფეხბურთელს შეაყვანინე სახელი გვარი და ასაკი 
# თუ ფეხბურთელი 18 დან 28 წლამდეა დააყენე 1 რიგში - print(”stand in a row”)
# თუ 28 დან 30 მდე - 2 რიგში - print(”stand in 2 row”)

# თუ ფეხბურთელი 18 წლამდეა “Come here when you turn 18”
# თუ ფეხბურთელი 40+ წლისაა “sorry its to late”



footballer = int(input("enter your age: "))  # ეკითხება ასაკს
footballer_1_question = input("enter your name: ") # ეკითხება სახელს

if  18 <= footballer <= 28: # რა მოხდება თუ შეიყვანს 18 დან 28 ამდე ციფრს
    print(f"{footballer_1_question} stand in a row") # ეკრანზე რას დაწერს
elif 28 <= footballer <= 30: # რა მოხდება თუ შეიყვანს 28 დან 30 ამდე ციფრს
    print(f"{footballer_1_question} stand in 2 row") # ეკრანზე რას დაწერს 
elif footballer < 18: # რა მოხდება თუ 18ზე ნაკლებ ციფრს შეიყვანს
    print(f"{footballer_1_question} Come here when you turn 18") # რას დაწერს ეკრანზე
elif footballer > 40: # რა მოხდება თუ 40ზე მეტ ციფრს შეიყვანს
    print(f"{footballer_1_question} sorry its to late") # რას გამოიტანს ეკრანზე
    
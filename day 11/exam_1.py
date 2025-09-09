# მომხმარებელს შეაყვანინე ციფრი და დაწერე პროგრამა რომელიც არკვევს უაროფითია ლუწია თუ დადებითი ლუწი  ან უაროფითია კენტია თუ დადებითი კენტი

number = int(input("enter your number: "))

if number < 0:
    if number % 2 == 0:
        print("negative even")
    else:
        print("negative odd")
else:
    if number % 2 == 0:
        print("positive even")
    else:
        print("positive odd")
           
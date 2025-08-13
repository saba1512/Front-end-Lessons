number = int(input("enter number: "))

if number > 20:
    print("რიცხვი მეტია 20-ზე. ვიყენებთ for loop-ს:")
    for i in range(1, number + 1):
        print(i)
elif number < 20:
    print("რიცხვი ნაკლები ან ტოლია 20-ის. ვიყენებთ while loop-ს:")
    i = 1
    while i <= number:
        print(i)
        i += 1
else:
    print("tolia")
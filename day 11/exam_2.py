# მომხმარებელს შეაყვანინე ციფრი და რამდენსაც შეიყვანს იმდენჯერ დაწერე სიტყვა “Python”, რიცხვი აუცილებლად უნდა იყოს დადებეითი


number = int(input("enter your number: "))
x = 1
if number > 0:
    while x <= number:
        print(x, "python")
        x += 1
else:
    print("enter positive number")
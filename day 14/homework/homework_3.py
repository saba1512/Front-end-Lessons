# პიროვნებას შეაყვანონე რამე ტექსტი და თუ ამ ტექსტში იყო რიცხვები შეიტანე ცალკე სიაში და დაბეჭდე

# მაგ: hello i am 28 yo
# შედეგი: [2, 8]
# მაგ: qwer asd  2 asdas 5 asda 45 dsdfds 97 
# შედეგი: [2, 5, 4, 5, 9, 7]


user = input("enter any text: ")
numbers = []

for i in user:
    if i.isdigit():
        numbers.append(int(i))
print(numbers)
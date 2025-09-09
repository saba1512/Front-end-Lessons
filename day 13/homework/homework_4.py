# მომხმარბეელს შეაყვანინე ციფრები და ამავე დროულად ეს შეყვანილი ციფრები დაჯამდეს, სანამ “exit” არ დაწერს შეეკითხოს და შეაყვანინოს ციფრი

# როცა exit დააწვება გაჩერდეს პროგრამა და აჩვენოს შეყვანილი ციფრების ჯამი
# 👉 მაგალითად:
# Enter number: 5
# Enter number: 8
# Enter number: stop
# Sum: 13

total = 0
while True:
    user_input = input("Enter number: ")
    if user_input.lower() == "exit":
        break
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        total += int(user_input)
    else:
        print("Please enter a valid number or 'exit' to stop.")

print(f"Sum: {total}")
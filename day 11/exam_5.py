# დაწერე პროგრამა რომელიც ადგენს პაროლის სიზუსტეს.

# მაგ: password = “Test123”

# მომხმარებელს შეეკითხე პაროლი მანამ, სანამ სწორად არ შეიყვანს ან არ შეიყვანს “exit”-გამოსვლა


entered_pass = input("enter password: ")
password = "test123"
exit_p = "exit"

while entered_pass != password and entered_pass != exit_p:
    entered_pass = input("enter password: ")

if entered_pass == password:
    print("pass is correct")
if entered_pass == exit_p:
    print("exit program")
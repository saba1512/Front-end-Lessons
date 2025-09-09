# მომხმარებელს შეაყვანინე რამე ტექსტი  ან შენ განსაზღვრე

# ამ ტექსტიდან იპოვე ყველა "d", "g" და "n" ასო და დათვალე რომელი რამდენი ასოა მოცემულ ტექსტში


user = input("enter any word: ")

d_count = 0
g_count = 0
n_count = 0


for i in user.lower():
    if i == "g":
        g_count += 1
    elif i == "d":
        d_count += 1
    elif i == "n":
        n_count += 1

print(f"d: {d_count}")
print(f"g: {g_count}")
print(f"n: {n_count}")
# პიროვნებას შეაყვანონე რამე სიტყვა და დათვალე რამდენი ხმოვანია და თანხომვანი სიტყვაში

# მაგ: if i == "a" or i =="e" or ....

user = input("enter any word: ")

vowel_count = 0
consonant_count = 0
numbers = 0
symbol = 0
for i in user:
    if i in "aeiou":
        vowel_count += 1
    elif i.isalpha():
        consonant_count += 1
    elif i.isdigit():
        numbers += 1
    else:
        symbol += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("numbers: ", numbers)
print("symbol: ", symbol)
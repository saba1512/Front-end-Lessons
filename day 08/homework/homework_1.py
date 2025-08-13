text =  "On a quiet morning, Emma grabbed her bag, put on her favorite shoe, and stepped outside. The sky was painted with clouds, and the sun shone gently over the hill. She walked past the garden, where flowers danced in the wind, and crossed the old bridge over a small river. "
sumer = 0

for i in text:
    if i == "a":
        sumer += 1
print(sumer)

sumer_the = 0

for i in text:
    if i == "the":
        sumer_the += 1
print(sumer)                    


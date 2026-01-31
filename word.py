text = input("Enter some words: ")

words = text.split() #converting into list


word_count = {}

for word in words:
    if word in word_count:
        word_count[word]  += 1

    else:
        word_count[word] = 1


for key, val in word_count.items():
    print(f"{key} = {val}")
word = input("Enter the word in which you wanna count a letter: ")
letter = input("Enter the letter you wanna count: ")
count = 0 
for letter1 in word:
    if letter1 == letter:
        count = count +1
print(count)
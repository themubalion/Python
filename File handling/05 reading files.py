password = open('passwords.txt')
## Printing the lines of the file

# for i in password:
#     print(i)


## Printing the number of lines in the file

# count = 0
# for j in password:
#     count = count + 1
# print(count)


## Making a string out of the text file

# list = password.read()
# print(list)
# list

## Printing the specific lines that starts with G
for list in password:   
    list = list.rstrip()
    if(list.startswith('M')):
        print(list) 
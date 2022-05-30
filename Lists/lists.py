## LIST METHODS:

# You can use dir(list) to find the methods of the list

list = list()

# append method:
def append():
    list.append('Hello World')
    list.append(99)
    print(list)
append()
# sort method:

list2 = [2,234,23,21234,4]  # You will need either only strings or integers in the list to sort them
list2.sort()
print(list2)

## LIST FUNCTIONS:

# len function:

print("len: ",len(list)) 

# max function:

print("Max: ",max(list2)) # int

# min function:

print('len: ',min(list2)) # int

# sum function:

print('sum: ', sum(list2)) # int

# average function:

print(sum(list2)/len(list2)) # int

# average finder program:

def average():
    n = int(input('Enter the total numbers of data of which you wanna find the average: '))
    i = 0
    avg = []
    while i < n:
        num = int(input('Enter the number: '))
        avg.append(num)
        i = i + 1
    print(sum(avg)/n)

# split method used for string:
abc = "Hello There I am Mubashshir Ali"
strlist = abc.split() # You can use split(';') to seperate strings by semi colon or any other thing, by default it is space
print(strlist)
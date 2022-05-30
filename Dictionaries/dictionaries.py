# # Dictionaries syntax

# dict = dict()
# dict['paplu'] = 'a Cockroach name in the Oggy and the Cockcroaches who is really fat.'
# dict['taplu'] = 'a Cockroach name in the Oggy and the Cockcraoches who is small in height.'
# word = input("Enter the word you want to search in the dictionary: ")
# # print(dict)
# # print(dict['Paplu'])
# print(dict[word.lower()])

# ## Counting the repeating names in dictionaries


def nameCount():
    count = dict()
    names = ['Mubashshir','Sufiyan','Mudassir','Mubashshir']
    for i in names:
        if i not in count:
            count[i] = 1
        else:
            count[i] = count[i] + 1
    print(count)

## Verifying if some key is in the dictionary(LONG METHOD)
  
def verification():  
    i = input('Enter your name: ')
    friends = dict()
    if i in friends:
        x = friends[i]
    else:
        x = 'Sorry you are not in the friends list of mine'
    print(x)

## Verifying by short method:
# syntax = dictionary.get(keyname, value)

def get():
    friendcount = dict()
    newFriends = list()
    for j in newFriends:
        friendcount[j] = friendcount.get(j,0) + 1
    print(friendcount)

## Looping through a dictionary


def loop():
    lang = {
        'Mubashshir' : 'Python, C#, PHP',
        'Khubaib' : 'Shell, Python',
        'Adeeb' : 'Python, C#, Java, C++'
    }
    for key in lang:
        print(key+':',lang[key])
    print('Finished')
# loop()

## Get function

fname = open('mbox-short.txt','r')
textfile = fname.read()
di = dict()
textfile.strip()
words = textfile.split()


# for i in words:
#     strip = words[i]
    # words[i] = strip.strip()


for i in words:
    di[i] = di.get(i,0) + 1


    # print(i,di[i])
# print(di)
# print(max(di.items()))


largest = 0
word = None
for k,v in di.items():
    if v > largest:
        largest = v + largest
        word = k
print("The word is '"+word+ "' with the frequency of '" + str(largest)+"'")
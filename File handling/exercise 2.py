from calendar import c


ftext = open('words.txt','r')
text = ftext.read()
ftext.close()
words = text.split()
count = dict()
for i in words:
    if i not in count:
        count[i] = 1
    else:
        count[i] = count[i] + 1
print(count)
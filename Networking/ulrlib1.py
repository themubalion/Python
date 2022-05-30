import urllib.request,urllib.error,urllib.error
link = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in link:
    print(line.decode().strip())
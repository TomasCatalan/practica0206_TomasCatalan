import urllib.request

link = "http://textfiles.com/adventure/aencounter.txt"

x = str(urllib.request.urlopen(link).read())
y = x.split()
z = len(y)

print(z)
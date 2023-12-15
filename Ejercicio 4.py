import urllib.request

link = "http://textfiles.com/adventure/aencounter.txt"

x = urllib.request.urlopen(link)
j = x.read()
y = j.split()
z = len(y)

print("El numero de palabras del fichero es", z)

'''
file = urllib.request.urlopen(link)
text= file.read()
palabras = text.split()
print(len(palabras))
'''
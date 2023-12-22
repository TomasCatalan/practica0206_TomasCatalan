import urllib

x = "https://docs.google.com/spreadsheets/d/1bjm57pQSadS0WBvrB_wt1aowkljr6d5Zsq7OVKACakg/edit?usp=sharing"

openlink = urllib.request.urlopen(x)

openlink.read()
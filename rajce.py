#!/usr/bin/env python
#
# Stazeni fotek z rajce.net
import urllib
import urllib2
import re
import os

path=raw_input("Zadejte adresu galerie (napr. http://autor.rajce.idnes.cz/galerie/):\n")
dir=raw_input("Zadejte slozku, do ktere se fotky stahnou (musi byt prazdna):\n")

# Vytvoreni slozky
try:
    os.mkdir(dir)
except:
    pass

def download(url, local):
    """Copy the contents of a file from a given URL
    to a local file.
    """
    import urllib
    webFile = urllib.urlopen(url)
    localFile = open(local, 'w')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()

f=urllib.urlopen(path)
list=f.read().split("<div id=\"photoList\"")[1].split("<div id=\"clearFloatLine\"")[0].split("\n")


photos=[]
# nalezeni seznamu fotek
for line in list:
    m=re.search(r"<a id=\"p_[0-9]*\" href=\"([^\"]*)\"",line)
    if m:
        photos += [m.group(1)]

i=1
for url in photos:
    file="img_" + "0"*(3-len(str(i))) + str(i) + ".jpg"
    i+=1
    download(url, dir + "/" + file)
    print url + " ... ok"

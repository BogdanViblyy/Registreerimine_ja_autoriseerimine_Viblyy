from os import system
from gtts import *
def loe_failist(fail:str):
    """Loeme failist read ja salvestame j�rjendisse. Funktsioon
      tagastab j�rjend
    :param str fail:
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8") #try
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend



def kirjuta_failisse(fail:str,jarjend=[]):
    """
    """
    n=int(input("Sisesta mitu elemendi: "))
    for i in range(n):
        jarjend.append(input(f"{i+1}. element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

kirjuta_failisse("Text.txt")

def heli(tekst:str,keel:str):
    obj=gTTS(text=tekst, lang=keel, slow=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisesta tekst: ")
heli(tekst,'et')



paevad=loe_failist("Paevad.txt")
print(paevad)


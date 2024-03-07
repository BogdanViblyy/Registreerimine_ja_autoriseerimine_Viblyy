from random import *
from string import *

ascii_letters+digits+punctuation

def random_parool(paroolid:list)->any:
    """

    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) 
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)

    parool = ''.join([random.choice(ls) for x in range(12)])
    return parool






def Registreerimine(kasutajad:list,paroolid:list)->any:
    """


    """
    nimi=input("Sisestage nimi")
    if nimi in kasutajad:
        int(input("Meil juba on kasutaja selle nimega, palun valige midagi muud"))
    elif len(nimi)<50:
        kasutajad.append(nimi)
        input("Sisestage postkasti")
        
        
        
        
        valik2=input("Me oleme varsti valmis! Nüüd te saate mõelda välja parooli(1), või me saaame genereerida parooli ise(2)")
        if valik2==1:
            parool=input("Sisestage oma parooli: ")
            paroolid.append(parool)
        elif valik2==2:
            parool=random_parool()
            print("See on teie parool: "+parool)
            paroolid.append(parool)
        else:
            print("viga")
    else:
        print("viga")


def Autoriseerimine(kasutajad:list,paroolid:list)->any:
    """


    """
    nimi=input("Sisestage nimi")
    if nimi in kasutajad:
        parooli_katse=input("Sisestage oma parooli: ")

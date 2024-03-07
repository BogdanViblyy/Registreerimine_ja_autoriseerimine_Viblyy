from module1 import *
kasutajad=[]
paroolid=[]
post=[]
while True:
    print("Kas tahate registreerida(1),  autoriseerida(2), muutuda nimi(3), muutuda parooli(4), parooli taastamine(5), või lõppetada?")
    valik=int(input())
    if valik==1:
        Registreerimine(kasutajad,paroolid)
        

        
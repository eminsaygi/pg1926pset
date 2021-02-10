tekS=[]
ciftS=[]
ciktiS=[]
sayiS = int(input('Listeye kaç sayı eklenecek: '))
for n in range(sayiS):
    sayi=int(input("{}. sayıyı girin :". format(n+1)))
    if sayi not  in tekS or ciftS:
        if sayi%2==0:
            ciftS.append(sayi)
        else:
            tekS.append(sayi)
cikti=tekS+ciftS
print(cikti)
print("çıktı :", max(tekS))

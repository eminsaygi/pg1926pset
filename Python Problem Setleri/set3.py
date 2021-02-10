sayilar = []
girdiler = int(input("Satır uzunluğunu giriniz: "))
for i in range(girdiler):
    sayi1=int(input("{}. sayıyı girdin :". format(i+1)))
    sayilar+=[sayi1]
print(sayilar)

def yerDegistir(liste):
    Ssifir= []
    dsayilar=list()
    for i in liste:
        if i==0:
            Ssifir.append(i)
        else:
            dsayilar.append(i)
    cikti = Ssifir + dsayilar
    return (cikti)
x=yerDegistir(sayilar)
print(x)
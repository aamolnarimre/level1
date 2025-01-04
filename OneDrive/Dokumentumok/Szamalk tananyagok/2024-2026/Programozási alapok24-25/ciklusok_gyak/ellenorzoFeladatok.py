def huszig():
    for i in range(0,21):
        print(i,end=' ')

def kettesevel():
    for i in  range(20,58,2):
        print(i)
def negyesevel():
    for i in range(77,-77,-4):
        print(i)
def otos():
    szam1 = int(input('Az első szám: '))
    szam2 = int(input('Az második szám: '))

    if szam1 > szam2:
        szam2, szam1 = szam1, szam2  # felcserélem a
    for i in range(szam1, szam2 + 1):
        print(i, end=' ')

def hatos():
    szam1 = int(input('Az első szám: '))
    szam2 = int(input('Az második szám: '))
    if szam1>szam2:
        szam1, szam2 = szam2, szam1
    szorzat = szam1*szam2
    if szorzat > 0:
        for i in range(0,szorzat+1):
            print(i, end=' ')
    elif szorzat < 0:
        for j in range(0,szorzat-1,-1):
            print(j, end=' ')


def hetes():

    szam1 = int(input('Az első szám: '))
    szam2 = int(input('Az második szám: '))

    szam2, szam1 = szam1, szam2
    szamok = []
    szam = 0
    szorzat = szam1*szam2
    if szorzat > 0:
        while szam != szorzat:
            szam+=1
            szamok.append(szam)
        print(szamok)
    elif szorzat < 0:
        while szam >= szorzat:
            szam-=1
            szamok.append(szam)

        print(szamok)


def nyolcas():
    for i in range(1,8):
        if i != 7:
            print(i, end=',')
        else:
            print(i)

def faktorialis():
    szamok = []
    bekertSzam = int(input('Addj meg egy számot: '))
    for i in range(bekertSzam,0,-1):
        szamok.append(i)
    #print(szamok)
    print(f'A(z) {bekertSzam} faktoriálisa a(z): {szamok[0] * szamok[1] * szamok[2] * szamok[3] * szamok[4]}')

def ikszIpsz():
    x = int(input('Addj meg egy számot: '))
    y = int(input('Addj meg egy számot: '))
    print(3*x+y**2)

def negyHarmincegy():
    szamok = []
    x = int(input('Addj meg x értékét: '))
    y = int(input('Addj meg y értékét: '))
    if x > y:
        x, y = y, x
    szamok = []
    parosSzamok = []
    for i in range(x,y):
        szamok.append(i)
        if i % 2 == 0:
            parosSzamok.append(i)
    print(parosSzamok)
    print(f'A páros számok a száma a megadott klét szám között: {len(parosSzamok)}')

def haromszog():
    a = int(input('Add meg a-t: '))
    b = int(input('Add meg b-t: '))
    c = int(input('Add meg c-t: '))

    if a+b > c and a+c > b and b+c > a:
        print('Készíthető háromszög az oldalakból.')
    else:
        print('Nem készíthető háromszög az oldalakból.')

def tizbőlNeagtivokOsszege():
    negativSzam =  0
    for i in range(10):
        szamok = float(input(f'Kérem, adjon meg egy számot: '))
        if szamok < 0:
            negativSzam += szamok
    print(f'A negatív számok összege: {negativSzam}')

def oszthato3al():
    szamok = 0
    while szamok > -99:
        szamok = float(input(f'Kérem, adjon meg egy számot: '))
    print(f' A {szamok} háromjegyú és negatív szám')


def haromjrhxu():

    szamok = 0

    while szamok < 100:
        szamok = float(input(f'Kérem, adjon meg egy számot: '))
    print('Köszi!')

def OtszamOsszeg():
    szam = 0
    for i in range(5):
        szamok = float(input(f'Kérem, adjon meg egy számot: '))
        szam += szamok
    print(szam)

def otSzoveg():
    szovegek = []

    for i in range(5):
        szoveg = input(f'Add meg a(z) {i+1}. szöveget:  ')
        szovegek.append(szoveg)
    print(*szovegek)()

def otSZamLk():
    szamok = []

    for i in range(5):

        szam =  int(input(f'Az {i+1}.  szam legyen a(z): '))
        szamok.append(szam)
    legkisebb = szamok[0]
    for szam in szamok:
        if szam < legkisebb:
            legkisebb = szam
    print(f'A legkisebb szám a(z): {legkisebb}')

def vanEparos():
    parosSzamok = []
    for i in range(5):
        szam = float(input(f'Kérem, adja meg a(z) {i+1}. számot '))
        if szam % 2 == 0:
            parosSzamok.append(szam)
    if len(parosSzamok) > 0:
            print('Van legalább egy páros szám a ,listában')
    else:
            print('Nincs paros szam a lsitában')


def megdParos():
    parosSzamok = []
    for i in range(5):
        szam = float(input(f'A(z) {i+1}. szam a(z):'))
        if szam % 2 == 0:
            parosSzamok.append(szam)
    if len(parosSzamok) > 0:
        print(f'A páros szám(ok) a következők: {parosSzamok}')
    else:
        print('nincsenek páros számok')






























def otSzam():
    szamok = []
    szam = 0
    szam1 = int(input('Add meg az első számot: '))


    szam2 = int(input('Add meg az második számot: '))

    szam3 = int(input('Add meg az harmadik számot: '))
    szam4 = int(input('Add meg az negyedik számot: '))

    szam5 = int(input('Add meg az ötödik számot: '))
    szamok.append(szam1)
    szamok.append(szam2)
    szamok.append(szam3)
    szamok.append(szam4)
    szamok.append(szam5)
    for i in szamok(szam1, szam5):
        print(i)











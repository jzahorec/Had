from random import randrange

had = [[0,0], [0,1], [0,2], [0, 3], [0,4]]
 
def vytvor_hada(had, sirka, vyska):
    radek = [ "." for i in range(sirka) ]
    pole = [ list(radek) for i in range(vyska) ]
    if kontrola_kousnuti(had):
        return 
    for a, b in had:
        if kontrola_hranic(sirka, vyska, a, b):
            pole[a][b] = "o"
        else:
            return        
    return pole
 
def vykresli_pole(pole):
    if not pole:
        print 'NARAZIL!!'
        return
    for radek in pole:
        print ''.join(radek)
    print
 
def doprava(had):
    a,b = had[-1]
    b += 1
    del had[0]
    had.append([a,b])
    return had
 
def doleva(had):
    a,b = had[-1]
    b -= 1
    del had[0]
    had.append([a,b])
    return had
 
def nahoru(had):
    a,b = had[-1]
    a -= 1
    del had[0]
    had.append([a,b])
    return had
 
def dolu(had):
    a,b = had[-1]
    a += 1
    del had[0]
    had.append([a,b])
    return had
 
def kontrola_hranic(sirka, vyska, a, b):
    return a < sirka and b < vyska and a >= 0 and b >= 0
 
def kontrola_kousnuti(had):
    for i, prvek1 in enumerate(had):
        for prvek2 in had[i+1:]:
            if prvek1 == prvek2:
                return True
def l(had):
    for pohyb in [doleva]:
        if had[-1] == had[-2]:
            break
        had = pohyb(had)
        pole_s_hadem = vytvor_hada(had, 10, 10)
        vykresli_pole(pole_s_hadem)
        if not pole_s_hadem:
            break

def p(had):
    for pohyb in [doprava]:
        if had[-1] == had[-2]:
            break
        had = pohyb(had)
        pole_s_hadem = vytvor_hada(had, 10, 10)
        vykresli_pole(pole_s_hadem)
        if not pole_s_hadem:
            break

def n(had):
    for pohyb in [nahoru]:
        if had[-1] == had[-2]:
            break
        had = pohyb(had)
        pole_s_hadem = vytvor_hada(had, 10, 10)
        vykresli_pole(pole_s_hadem)
        if not pole_s_hadem:
            break

def d(had):
    for pohyb in [dolu]:
        if had[-1] == had[-2]:
            break
        had = pohyb(had)
        pole_s_hadem = vytvor_hada(had, 10, 10)
        vykresli_pole(pole_s_hadem)
        if not pole_s_hadem:
            break


pole_s_hadem = vytvor_hada(had, 10, 10)
vykresli_pole(pole_s_hadem)
 
##for pohyb in [dolu, dolu, doleva]:
##    if had[-1] == had[-2]:
##        break
##    had = pohyb(had)
##    pole_s_hadem = vytvor_hada(had, 10, 10)
##    vykresli_pole(pole_s_hadem)
##    if not pole_s_hadem:
##        break

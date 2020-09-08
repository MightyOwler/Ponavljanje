import random
import time
nač=input('izberi način podaje letnic:     1)Kot smo jih jemali\n                                2)Naključno\n')
t0=time.time()
def premešaj(s0):
    s=[]
    while len(s0)!=0:
        r=random.randint(0,len(s0)-1)
        s+=[s0[r]]
        s0=s0[:r]+s0[r+1:]
    return(s)
dogodki0=['razsvetljenstvo od','enciklopedija od','enciklopedija do', 'O duhu zakonov', 'Ruso od', 'Ruso do', 'Družbena pogodba', 'absolutizem od', 'absolutizem do', 'spreminjanje absolutizma ', 'Prusija 1 od 300 enot RNC', 'Friderik 2. Pruski od', 'Marija Terezija od', 'Marija Terezija do', 'Primogenitura', 'Jožef 2. od', 'Jožef 2. do', 'konc osebne odvisnosti kmetov', 'splošni šolski red', 'Jožefinski civilni zakonik ', 'tolerančni patent od', 'tolerančni patent do', 'kraljeva omejitev širjenja kolonij', 'sedemletna vojna od', 'sedemletna vojna do', 'bostonski masaker', 'bostonjska čajanka', 'pritožba za kralja', 'odločitev za prekinitev vezi z VB', 'deklaracijao neodvisnosti', 'vojna od', 'vojna do', 'bitka za brooklyn', 'George Washington 1.', 'George Washington 2.', 'Versajska mirovna pogodba', 'ustanovni akt', 'ustava ZDA', 'bill of rights', 'F.revolucija od', 'F.revolucija do', 'Ludvik 16. od', 'prejšnje zasedanje generalnih stanov', 'zasedanje generalnih stanov', 'priznanje skupščine F.', 'napad na Bastiljo', 'preimenovanje narodne skupščine', 'nočna seja', 'deklaracija o pravicah človeka in državljana', 'kralj ne potrdi ustave', 'kralj potrdi ustavo', 'kralj v pariz', 'kraljev pobeg', 'zaplemba cerkvi', 'revolucionarni denar', 'pozivi evropskih vladarjev proti revoluciji', 'žirondinci vodstvo od 1', 'žirondinci vodstvo od 2', 'žirondinci vodstvo do', 'vojna napoved Avstriji', 'množica zavzame kraljevo palačo', 'vdor pariških množic v zapore od', 'vdor pariških množic v zapore do', 'bitka pri valmyju', 'konc kraljevine', 'revolucionarni koledar', 'obglavljanje kralja', 'obglavljanje kraljice', 'pilniška izjava', 'Jakobinska republika do', 'konec vojne z Avstrijo', 'upor proti revolucionarni vladi', 'sprejeta Jakobinska ustava', 'Robespjer obglavljen', 'termidorjanski udar', 'pokol v Lyonu', 'ustava z akt. In pas. Preb.', 'Prijateljice resnice zahtevajo pravice žensk', 'deklaracija o pravicah ženske in državljanke','1.Direktorij','N.B. poveljnik v Ita.' ,'N.B. konzul','N.B. dosmrtni konzol','N.B. kronan v katedrali notre dome','Invazija na Rusijo','N.B.izgubi v egiptu','Bitka pri Trafalgarju','N.B. ukine rim. nem. ces.','Celinska zapora od','Ilirske province od','Ilirske province do','N.B.razglasi konc F. rev.','Koalicijske vojne od','Koalicijske vojne do','Bitka pri Waterluju','Kodifikacija civilnega prava','Konkordat s cerkvijo','Dunajski kongres od','Dunajski kongres do','Zadnja koal. vojna']
letnice0=['18s','1751', '1783', '1748', '1712', '1778', '1762', '16s', '17s', '18s', '17s', '1740', '1740', '1780', '1635', '1780', '1790', '1781', '1774', '1786', '1781', '1782', '1763', '1756', '1763', '1770', '1773', '1774', '1775', '1776', '1775', '1783', '1776', '1789', '1792', '1783', '1777', '1787', '1791', '1789', '1799', '1774', '1614', '5.5.1789', '17.6.1789', '14.7.1789', '1789', '4.8.1789', '26.8.1789', '3.9.1791', '14.9.1791', '10.1789', '6.1791', '1789', '1790', '8.1791', '1791', '1792', '1797', '20.4.1792', '10.8.1792', '2.9.1792', '5.9.1792', '20.9.1792', '21.9.1792', '22.9.1792', '21.1.1793', '10.1793', '1791', '1793', '1794', '1793', '6.1793', '28.7.1794', '1795', '6.1793', '1791', '1791', '9.1791','1795','1796','1799','1802','1804','1.12.1812','1898','1805','1806','1806','1809','1813','15.12.1799','1792','1815','1815','1804','1801','9.1814','6.1815','1815']
dogodki=[]
if nač=='2':
    letnice=premešaj(letnice0)
else:
    letnice=letnice0
for n in letnice:
    d=letnice0.index(n)
    letnice0=letnice0[:d]+letnice0[d+1:]
    dogodki+=[dogodki0[d]]
    dogodki0=dogodki0[:d]+dogodki0[d+1:]
pravilnost=len(dogodki)*['0']
c='ja'
while c=='ja' or c=='Ja'or c=='JA' or c=='da' or c=='Da' or c=='DA':
    while '0' in pravilnost:
        print('\n\n')
        for n in dogodki:
            if pravilnost[dogodki.index(n)]=='0':
                a=input(n+'\n')
                if len(a)==2:
                    a=b[:-2]+a
                elif len(a)==1:
                    a=b[:-1]+a
                if a==letnice[dogodki.index(n)]:
                    pravilnost[dogodki.index(n)]='1'
                else:
                    print('\n\n\nni %s, je pa              %s\n\n\n'%(a,letnice[dogodki.index(n)]))
                b=a
    c=input('\n\nODLIČNO!\nPritisni enter za končat')
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTO UČENJE LETNIC TI JE UNIČILO %s SEKUND ŽIVLJENJA!'%(str(int(time.time()-t0))))





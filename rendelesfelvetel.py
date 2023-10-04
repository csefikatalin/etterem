import kozos_eljarasok
import etlap

def szamla(leves_nev, leves_ar, foetel_nev, foetel_ar):
    osszeg:float = leves_ar + foetel_ar
    kozos_eljarasok.fejlec("RENDELÉS",50,"♠")
    kozos_eljarasok.tetel("♠",leves_nev,leves_ar,50)
    kozos_eljarasok.tetel("♠",foetel_nev,foetel_ar,50)
    kozos_eljarasok.tetel("♠","Összesen:",osszeg,50)
    kozos_eljarasok.fejlec("Köszönjük, hogy a vendégünk volt!",50,"♠")


def rendeles(leves1,leves2,foetel1,foetel2,leves1_ar,leves2_ar,foetel1_ar,foetel2_ar):
    meret:int= 30
    kar2:str ="♣"
    disz:str="〰"
    leves_nev:str =""
    leves_ar:float=0
    foetel_nev:str =""
    foetel_ar:float=0
    print()
    ker_E:str = input("Kér levest? I/N ")
    if ker_E=="I" or ker_E == "i":
        etlap.leves()       
        leves = int(input("Melyik levest kéri? 1 / 2  "))
        if leves==1:
            leves_nev=leves1
            leves_ar= leves1_ar
        elif leves==2:
            leves_nev=leves2
            leves_ar= leves2_ar
        else:
            print("Ilyen számú leves nincs!")
    print() 
  

    
    
    ker_E:str = input("Kér főételt? I/N ")
    if ker_E=="I" or ker_E == "i":
        etlap.foetel()         
        foetel = int(input("Melyik levest kéri? 1 / 2   "))
        if foetel==1:
            foetel_nev=foetel1
            foetel_ar= foetel1_ar
        elif foetel==2:
            foetel_nev=foetel2
            foetel_ar= foetel2_ar
        else:
            print("Ilyen számú főétel nincs!")
    print() 
    print()
    """számolások"""
    szamla(leves_nev, leves_ar, foetel_nev, foetel_ar)
    
    
    
   
    

import  kozos_eljarasok
leves1:str = "1 - Húsleves gazdagon"
leves2:str = "2 - Gyümölcsleves"
leves1_ar:float = 800
leves2_ar:float = 750
foetel1:str = "1 - Csirkepörkölt galuskával"
foetel2:str = "2 - Sztrapacska"
foetel1_ar:float = 2800
foetel2_ar:float = 1750
meret:int= 30
"""díszítéshez"""

disz:str="〰"
meret:int= 80
kar1:str ="◼"
kar1:str ="🌺"
kar2:str ="♦"
kar1:str ="♣"
kar1:str ="♦"

def leves():
    kozos_eljarasok.cim_szoveg("♨ LEVESEK ♨",meret,kar2)
    kozos_eljarasok.diszvonal(kar2,disz*3,meret)
    kozos_eljarasok.tetel(kar2, leves1,leves1_ar,meret)
    kozos_eljarasok.tetel(kar2, leves2,leves2_ar,meret)

def foetel():
    kozos_eljarasok.cim_szoveg("♨ FŐÉTELEK ♨",meret,kar2)
    kozos_eljarasok.diszvonal(kar2,disz*3,meret)
    kozos_eljarasok.tetel(kar2, foetel1,foetel1_ar,meret)
    kozos_eljarasok.tetel(kar2, foetel2,foetel2_ar,meret)
    
def etlap():
    kozos_eljarasok.fejlec("ÉTLAP",meret, kar1)   
    leves()
    foetel()    
    kozos_eljarasok.diszvonal(kar2,disz*3,meret)
    kozos_eljarasok.fejlec("Jó étvágyat!",meret, kar1)
"""Változók és konstansok deklarálása """
    
    
def tetel(kar:str, tetel:str, ar:float, meret:int): 
    koz:str = "         "
    print(f"{kar}{koz}{tetel}{ar:>{meret - len(kar)*2-len(tetel)-3-2*len(koz)}.2f} Ft{koz}{kar}")
    
def diszvonal( kar:str, disz:str,  meret:int):
      print(f"{kar}{disz:^{meret-len(kar)*5}}{kar}")    
    

def fejlec(szoveg:str, meret:int, kar:str):    
    print(kar*meret)
    cim_szoveg(szoveg, meret, kar)
    print(kar*meret)

def cim_szoveg(szoveg:str, meret:int, kar:str):
    print(f"{kar}{szoveg:^{meret-len(kar)*2}}{kar}")  
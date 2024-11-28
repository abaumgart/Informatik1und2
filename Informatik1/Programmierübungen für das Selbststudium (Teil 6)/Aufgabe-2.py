
def palindrom(s):
    erg = True
    l = len(s)//2
    for i in range(l):
        if s[i]!=s[-i-1]:
            erg=False
        
    return erg

wort = input("Bitte Zeichenkette eingeben: ")
wort = wort.lower()                              
ergebnis = palindrom(wort)                       
if ergebnis == True:                           
    print("Dies ist ein Palindrom!")
else:
    print("Dies ist KEIN Palindrom!")
    


    


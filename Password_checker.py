import re 
from random import choice
from strong_passwords import parollar

print("Parolingiz kuchlimi?")
parol = input("Tekshirish uchun parol kiriting: ")
def cheker(password):
    
    sabablar =[]
    
    if not re.search(r".{8,20}", password):
        sabablar.append("Parol kamida 8 ta belgidan iborat bo'lishi kerak")
    if not re.search(r"[A-Z]", password):
        sabablar.append("Parolda kamida bitta katta harf bo'lishi kerak")
    if not re.search(r"[a-z]", password):
        sabablar.append("Parolda kamida bitta kichik harf bo'lishi kerak")
    if not re.search(r"\d", password):
        sabablar.append("Parolda kamida bitta raqam qatnashgan bo'lishi kerak ")
    if not re.search(r"[!@#$%^&*]", password):
        sabablar.append("Parolda kamida bitta maxsus  qatnashgan bo'lishi kerak!\nMaxsus belgilar: !@#$%^&*  ")
    return sabablar
    
def kuchli_parol():
    parol=choice(parollar)
    return parol        
    
def sabablar_display(password):
    sabablar = cheker(password)
    kuchli_passwd=kuchli_parol()
    if sabablar:
        print(f"Parol zaif: {password}")
        for sabab in sabablar:
            print(f"-{sabab}")
        print(f"Tafsiya qilingan parol: {kuchli_passwd}")
    else: 
        print(f"Parol kuchli: {password}")

sabablar_display(parol)

valamiszám = 4
def kurvaanyja(f_num):
    lista = []
    négyzeteslista = []
    szám = 0
    while True:
        if szám <= f_num:
            szám += 1 
            lista.append(szám)
            négyzetszám = szám **2
            négyzeteslista.append(négyzetszám)
            continue 
        else:
            break

    print(f"Ez a négyzetes lista:{négyzeteslista}"
      f"Ez a sima lista:{lista}")
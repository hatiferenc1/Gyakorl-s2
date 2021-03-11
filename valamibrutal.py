valamiszám = 4
def kurvaanyja(f_num):
    lista = []
    négyzeteslista = []
    for num in range(f_num):
       lista.append(num)
       sqr_num = num ** 2 
       négyzeteslista.append(sqr_num)
    print(f"Ez a négyzetes lista:{négyzeteslista}"
      f"Ez a sima lista:{lista}")


kurvaanyja(f_num=valamiszám)
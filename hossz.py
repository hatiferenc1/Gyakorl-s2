def kurvaanyja():
    szó = input('Adj meg egy szót ')
    hossz = len(szó)
    hossznégyzet = hossz ** 2 
    lista = []
    lista.append(hossznégyzet)
    return lista


print(kurvaanyja())
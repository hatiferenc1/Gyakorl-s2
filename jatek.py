import random as r





player = 0
bot = 0 

while player < 10 and bot < 10:
    print("--------------------------")
    print(f"player pontszáma:{player}")
    print(f"bot pontszáma:{bot}")
    print("--------------------------\n")
    játékcuccok = ["kő","papír","olló"]
    felhkérdés = input("Kő papír vagy olló?: ")
    botchoice = játékcuccok[r.randint(0,2)]
    felhkérdés = felhkérdés.lower()

    if felhkérdés == "kő" and botchoice == "olló":
        player += 1 
        print(f"player nyert:{felhkérdés}")
        print(f"A bot vesztett:{botchoice} \n")
        continue
    elif felhkérdés == "olló" and botchoice == "papír":
        player += 1 
        print(f"player nyert:{felhkérdés}")
        print(f"A bot vesztett:{botchoice} \n")
        continue
    elif felhkérdés == "papír" and botchoice == "kő":
        player += 1 
        print(f"A player nyert:{felhkérdés}")
        print(f"A bot vesztett:{botchoice} \n")
        continue
    elif felhkérdés == botchoice:
        print("Döntetlen, senki nem kap pontot ")
        continue


    else:
        bot += 1
        print(f"A bot nyert:{botchoice} ")
        print(f"A player vesztett:{felhkérdés} \n")
        continue

print("A JÁTÉKOS IDŐNEK VÉGE!!!")
if player == 10:
    print("Nyertél fasz") 
else:
    print("Bot-tól kikapsz...szégyen") 
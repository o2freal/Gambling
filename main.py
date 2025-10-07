import random
import time
nameplayer = str(input("Nom du joueur : "))
solde = int(50)

print("bonjour, ", nameplayer, "votre solde est de : $",solde)
time.sleep(1)

while True :
    continuer = str(input("voulez vous parier ? [y/n] : "))
    time.sleep(0.5)

    if continuer == "n" :
        print("Au revoir !")
        break

    else :
        bet = int(input("Entrée votre mise : "))

    if bet > solde :
        print("Vous n'avez pas cette somme")


    else :
        def gambling(a, b):
            cpu = random.randint(1, 12)
            player = random.randint(1, 12)

            if cpu > player :
                return "l'ordinateur a gagné"
            else :
                return "vous avez gagné"

        paris = gambling(bet, solde)
        print(paris)
        time.sleep(1.5)

        if paris == "l'ordinateur a gagné":
            solde = solde - bet

        else :
            solde = solde + bet

        if solde == 0 :
            print("vous avez perdu ! vous etes maintenant pauvre.")
            time.sleep(0.5)
            break

        else :
            print(nameplayer, "votre nouvelle solde est de : $",solde)
            time.sleep(0.5)



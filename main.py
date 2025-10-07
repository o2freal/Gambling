import random

nameplayer = str(input("Nom du joueur : "))
solde = int(50)

print("bonjour, ", nameplayer, "votre solde est de : ", solde)

while True :
    continuer = str(input("voulez vous pariez ? [y/n] : "))

    if continuer == "n" :
        print("En revoir !")
        break

    else :
        bet = int(input("Enter votre mise : "))

    if bet > solde :
        print("Vous n'avez pas cette somme")


    else :
        def gambling(a, b):
            cpu = random.randint(1, 24)
            player = random.randint(1, 24)

            if cpu > player :
                return "l ordinateur a gagner"
            else :
                return "vous avez gagner"

        paris = gambling(bet, solde)
        print(paris)

        if paris == "l ordinateur a gagner":
            solde = solde - bet

        else :
            solde = solde + bet

        if solde == 0 :
            print("vous avez perdu ! ")
            break

        else :
            print(nameplayer, "votre nouvelle solde est de : ", solde)



'''ici on importe les libraries que l'on va utiliser'''

import random
import time
import colorama
from colorama import Fore, Style, init

init(autoreset=True) # Ici on rend les couleurs compatible avec windows

'''on definie l'interface de base'''

nom_du_joueur = str(input("Nom du joueur : "))
solde = int(50)

print("bonjour, ", nom_du_joueur, "votre solde est de : ", solde)
time.sleep(1)



def demande_continuer(a) :

    '''on demande a l'utilisateur si oui ou non il veut parier si non cela renvoie false si oui cela renvoie true en cas d'erreur il renvoie valuerror'''

    if a == "n" or a == "N" :
        return False

    elif a == "y" or a == "Y":
        return True

    else :
        return ValueError

'''on definie la fonction qui effectue le paris'''

def paris():
    '''on effectue la demande de deux nombres aleatoires ( a l'aide de la librairie "randome ) l'un pour l'ordinateur l'autre pour le joueur si celui du joueur est superieur on dira qu'il a gagner si celui du pc est superieur on dira que len joueur a perdu si ils sont egal alors cela renvoi execaux'''

    cpu = random.randint(1, 12)
    player = random.randint(1, 12)

    print("Valeur de l'ordinateur : ", cpu)
    time.sleep(1.5)
    print("Valeur du joueur : ", player)

    if cpu > player :
        return "Victoire de l'ordianteur"

    elif player == cpu :
        return "execaux"

    else :
        return "Victoire du joueur"



'''on commence le programme en demandans si le joueur veut parier'''

continuer = demande_continuer(str(input("Voulez vous pariez ? [y/n] : ")))
time.sleep(1)

'''si il ne veut pas on arrete le programme'''


if continuer == ValueError :
    while continuer == ValueError :
        print("Valeur incorrecte")
        continuer = demande_continuer(str(input("Voulez vous pariez ? [y/n] : ")))
        time.sleep(1)
    if continuer == False :
        print("Au revoir !")

elif continuer == False :
    print("Au revoir !")


if continuer == True :

    '''on va demander au joueur sa mise avec "bet"
    puis on effectuera le pick des deux nombres
    puis on modifie la solde selon le resultat tout en redonnant au joueur sa solde
    et enfin on lui redemande si il veut reparier'''


    while continuer :

        a = True

        while a :
            '''Ici on verifie bien que la valeur de la mise (ici "bet") soit bien un entier et que si le joueur ne rentre pas une bonne valeur cela continue de lui demander la valeur en boucle'''
            try :
                bet = int(input("Entrer Votre mise : "))
                time.sleep(0.5)
                a = False
            except ValueError :
                print("Valeur incorrecte, Entrer un nombre.")

        if bet > solde :
            print("Vous n'avez pas cette somme")

        else :
            resultat = paris()

'''ici on affiche si l'ordinateur a gagner ou non et on print dans une couleur differentes selon la victoire et la defaite avec la librairie "colorama'''
            if resultat == "Victoire de l'ordianteur":
                time.sleep(1)
                print(Fore.RED + resultat)

            elif resultat == "Victoire du joueur" :
                time.sleep(1)
                print(Fore.GREEN + resultat)
            else :
                time.sleep(1)
                print(resultat)

'''ici on calcul la nouvelle solde selon le resultat du paris'''
            if resultat == "execaux" :
                solde = solde
            elif resultat == "Victoire de l'ordianteur" :
                solde = solde - bet

            else :
                solde = solde + bet

            if solde == 0 :
                print(Fore.RED + "vous avez perdu ! vous etes maintenant pauvre.")
                time.sleep(0.5)
                break # on arrete le programme si le joueur n'as plus de crédit

            else :
                print(nom_du_joueur, "votre nouvelle solde est de : ", solde) #on affiche la nouvelle solde du joueur
                time.sleep(1.5)

''' Ici on redemande si le joueur souhaite continuer ou pas comme au debut du programme '''
            continuer = demande_continuer(str(input("Voulez vous pariez ? [y/n] : ")))

            if continuer == ValueError :
                while continuer == ValueError :
                    print("Valeur incorrecte")
                    continuer = demande_continuer(str(input("Voulez vous pariez ? [y/n] : ")))
                    time.sleep(1)
                if continuer == False :
                    print("Au revoir !")
                    time.sleep(0.5)

            elif continuer == False :
                print("Au revoir !")
                time.sleep(0.5)
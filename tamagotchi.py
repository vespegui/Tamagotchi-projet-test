import time
from os import system

def main():
    system ('cls')
    global faim, energie, amusement, propreté, vivant
    faim = 50
    energie = 50
    amusement = 50
    propreté = 50
    vivant = True
    print("""    
    Un Tamagotchi est un animal de compagnie virtuel.
    Le jeu consiste à prendre soin de votre animal à travers la console de commande.
    Il ou elle nécessitera de manger, de dormir, de s'amuser ou de se laver pour rester en bonne santé.
           """)
    nom=input("""
    Comment voulez-vous appeler votre Tamagotchi cette fois-ci ?
            
            >""")
    print(" ")
    print(str(nom)," démarre avec:")
    print(" ")
    
    def manger():
        global faim, energie, amusement, propreté, vivant
        faim += 5
        energie -= 1
        amusement -= 1
        propreté -= 2
        if faim > 100:
            faim = 100
            print(str(nom)," est rassasié et n'a pas besoin de manger pour le moment !")
            energie += 1
            amusement += 1
            propreté += 2
        
    def dormir():
        global faim, energie, amusement, propreté, vivant
        faim -= 1
        energie += 5
        amusement -= 2
        propreté -= 1
        if energie > 100:
            energie = 100
            print(str(nom)," est pleinement reposé et n'a pas besoin de dormir pour le moment !")
            faim +=1
            amusement += 2
            propreté += 1

    def jouer():
        global faim, energie, amusement, propreté, vivant
        faim -= 1
        energie -= 2
        amusement += 5
        propreté -= 1
        if amusement > 100:
            amusement = 100
            print(str(nom)," est pleinement heureux et n'a pas besoin de s'amuser pour le moment !")
            faim +=1
            energie += 2
            propreté += 1

    def se_laver():
        global faim, energie, amusement, propreté, vivant
        faim -= 2
        energie -= 1
        amusement -= 1
        propreté += 5  
        if propreté > 100:
            propreté = 100
            print(str(nom)," est tout beau tout propre et n'a pas besoin de se laver pour le moment !")
            faim += 2
            energie += 1
            amusement += 1
            

    def print_etat():
        print("Faim", str(faim)+"/100")
        print("Energie:", str(energie)+"/100")
        print("Amusement:", str(amusement)+"/100")
        print("Propreté:", str(propreté)+"/100")

    while vivant == True:
        print_etat()
        verbe = input(f""" 
        Que veux faire {nom} ?

        1. Manger    2. Dormir    3. Jouer    4. Se laver   5. Quitter le jeu

        >   """)

        if verbe == "1":
            manger()        
        elif verbe == "2":
            dormir()
        elif verbe == "3":
            jouer()
        elif verbe == "4":
            se_laver()
        elif verbe =="5":
            print("Merci d'avoir joué au Tamagotchi. A très bientôt !")
            exit()
        else:
            print("choix invalide, veuillez réessayer")

        if faim <= 0:
            print(f"{nom} est mort de faim.")
            vivant = False
            replay = input("Votre tamagotchi est mort. Voulez-vous rejouer ?  1.Oui    2.Non ")          
        elif energie <= 0:
            print(f"{nom} est mort de fatigue.")
            vivant = False
            replay = input("Votre tamagotchi est mort. Voulez-vous rejouer ?  1.Oui    2.Non ")    
        elif amusement <= 0:
            print(f"{nom} est mort d'ennui.")
            vivant = False
            replay = input("Votre tamagotchi est mort. Voulez-vous rejouer ?  1.Oui    2.Non ")    
        elif propreté <= 0:
            print(f"{nom} est mort de malpropreté.")
            vivant = False
            replay=input("""
            Votre tamagotchi est mort. Voulez-vous rejouer ?  1.Oui    2.Non   

            >""")
    if replay == "1":
        main()
    elif replay == "2":
        print("Merci d'avoir joué au Tamagotchi. A très bientôt !")
        exit()
    else:
        print("choix invalide, veuillez réessayer")

main()
        
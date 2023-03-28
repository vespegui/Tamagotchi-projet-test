from os import system       #nécessaire pour effacer l'écran via 'cls' - à noter que cette commande varie en fonction du système d'exploitation. 'cls' fonctionne sous Windows.

def main():                                     #fonction qui englobe le reste, pour offrir la possibilité de rejouer dès la mort du tamagotchi
    system ('cls')          #effacer l'écran
    global faim, énergie, amusement, propreté, vivant, rejouer      #déclarer les variables nécessaires au programme
    faim = 50
    énergie = 50
    amusement = 50
    propreté = 50                             #ces 4 variables seront plus tard comprises entre 0 et 100 inclus.
    vivant = True                             # True = Vivant / False = mort
    rejouer = None                            # nécessaire pour rejouer après la mort du tamagotchi
    print("""    
    Un Tamagotchi est un animal de compagnie virtuel.
    Le jeu consiste à prendre soin de votre animal à travers la console de commande.
    Il ou elle nécessitera de manger, de dormir, de s'amuser ou de se laver pour rester en bonne santé.
           """)
    nom=input("""
    Comment voulez-vous appeler votre Tamagotchi cette fois-ci ?
            
    > """)
    print(" ")                              #les print(" ") ajoutent des lignes vides et aèrent le texte pour plus de lisibilité
    print(str(nom),"démarre avec:")
    print(" ")
    
    def manger():                           #manger donne 5 points de faim et retire 2 points d'énergie, 1 point d'amusement et 3 points de propreté
        global faim, énergie, amusement, propreté, vivant
        faim += 5
        énergie -= 2
        amusement -= 1
        propreté -= 3
        if faim > 100:                                 #bloquer la variable faim à 100 points maximum
            faim = 100
            print(" ")
            print(str(nom),"est rassasié et n'a pas besoin de manger pour le moment !")    #avec une phrase pour expliquer à l'utilisateur ce qui se passe
            print(" ")
            énergie += 2                  #remettre les points perdus lors de l'action bloquée par l'arrivée à 100 poins de faim
            amusement += 1                
            propreté += 3
        
    def dormir():                           #dormir donne 5 points d'énergie et retire 2 points de faim, 3 points d'amusement et 1 point de propreté
        global faim, énergie, amusement, propreté, vivant
        faim -= 2
        énergie += 5
        amusement -= 3
        propreté -= 1
        if énergie > 100:                            #bloquer la variable énergie à 100 points maximum
            énergie = 100
            print(" ")
            print(str(nom),"est pleinement reposé et n'a pas besoin de dormir pour le moment !")
            print(" ")
            faim += 2                     #remettre les points perdus lors de l'action bloquée par l'arrivée à 100 points d'énergie
            amusement += 3
            propreté += 1

    def jouer():                                        #même principe que les fonctions manger() et dormir()
        global faim, énergie, amusement, propreté, vivant
        faim -= 2
        énergie -= 3
        amusement += 5
        propreté -= 1
        if amusement > 100:
            amusement = 100
            print(" ")
            print(str(nom),"est pleinement heureux et n'a pas besoin de s'amuser pour le moment !")
            print(" ")
            faim += 2
            énergie += 3
            propreté += 1

    def se_laver():                                     #même principe que les fonctions manger() et dormir()
        global faim, énergie, amusement, propreté, vivant
        faim -= 2
        énergie -= 1
        amusement -= 3
        propreté += 5  
        if propreté > 100:
            propreté = 100
            print(" ")
            print(str(nom),"est tout beau tout propre et n'a pas besoin de se laver pour le moment !")
            print(" ")
            faim += 2
            énergie += 1
            amusement += 3
            

    def print_state():                              #suivre la progression des points après chaque action de l'utilisateur
        print(" ")
        print("faim", str(faim)+"/100")
        print("énergie:", str(énergie)+"/100")
        print("amusement:", str(amusement)+"/100")
        print("propreté:", str(propreté)+"/100")

    while vivant == True:             #boucle tant que le tamagotchi est en vie, les actions sont possibles
        print_state()
        verb = input(f""" 
        Que veux faire {nom} ?

        1. Manger    2. Dormir    3. Jouer    4. Se laver   5. Quitter le jeu

        >   """)

        if verb == "1":
            manger()         #appeler les fonctions conformément au choix numérique de l'utilisateur
        elif verb == "2":
            dormir()
        elif verb == "3":
            jouer()
        elif verb == "4":
            se_laver()
        elif verb =="5":
            print(" ")
            print("Merci d'avoir joué au Tamagotchi. A très bientôt !")
            exit()
        else:                   #prévoir l'erreur de saisie et la possibilité de se rattraper.
            print(" ")
            print("choix invalide, veuillez réessayer")       

        if faim <= 0:
            print(" ")
            print(f"{nom} est mort de faim.")       #f-string pour test
            vivant = False                       #les False sortent de la boucle et amènent à la suite du programme
       
        elif énergie <= 0:
            print(" ")
            print(f"{nom} est mort d'épuisement.")
            vivant = False
 
        elif amusement <= 0:
            print(" ")
            print(f"{nom} est mort d'ennui.")
            vivant = False
    
        elif propreté <= 0:
            print(" ")
            print(f"{nom} est mort de malpropreté.")
            vivant = False
 
    while rejouer != "1" and rejouer != "2":                          #boucle pour recommencer la partie
        rejouer = input("""
            Votre tamagotchi est mort. Voulez-vous rejouer ?  1.Oui    2.Non

            > """)
        
        if rejouer == "1":
           main()                        #retour en début de programme
        elif rejouer == "2":
            print(" ")
            print("Merci d'avoir joué au Tamagotchi. A très bientôt !")
            exit()                       #quitter le programme
        else:
            print (" ")
            print("choix invalide, veuillez réessayer")             

main()
        
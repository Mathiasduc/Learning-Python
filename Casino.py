from random import randrange
import math

print("Bienvenue dans ce casino! Notre Roulette comporte 50 cases, de 0 a 49. Les cases Pairs sont noirs"
      "\net les impairs rouges.")
cash_pool = 1000
while True:
    cash_pool = math.ceil(cash_pool)
    print("Vous disposez de", cash_pool, "jetons dans votre pot.")
    erreur = True

    while (erreur == True):
        erreur = False
        try:
            case_num = input("Sur quelle case souhaiter vous miser?")
            case_num = int(case_num)
            assert case_num >= 0 and case_num <= 49
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            erreur = True
        except AssertionError:
            print("Choisissez un nombre entre 0 et 49 pour jouer!")
            erreur = True
    if case_num % 2 != 0:
        pair_num = False
    else:
        pair_num = True

    erreur_somme = True

    while (erreur_somme == True):
        erreur_somme = False
        try:
            somme_mise = input("Quelle somme voulez vous miser?")
            somme_mise = int(somme_mise)
            assert somme_mise <= cash_pool
        except ValueError:
            print("Vous n'avez pas saisi un nombre.")
            erreur_somme = True
        except AssertionError:
            print("Ne misez pas plus que votre pot.")
            erreur_somme = True
    if pair_num == True:
        print("Vous miser", somme_mise, "sur la case", case_num, "noir.")
    else:
        print("Vous miser", somme_mise, "sur la case", case_num, "rouge.")
    cash_pool = cash_pool - somme_mise
    print("Les jeux sont faits , rien ne vas plus!")

    case_random = randrange(50)
    if case_random % 2 != 0:
        pair_random = False
    else:
        pair_random = True
    if pair_random == True:
        print("Le", case_random, "noir sort.")
    else:
        print("Le", case_random, "rouge sort.")

    if case_random == case_num:
        cash_pool += somme_mise * 3
        print("Vous avez gagné! Vous remporter 3 fois votre mise!")
    elif pair_num is True and pair_random is True:
        cash_pool += somme_mise * 0.5
        print("Vous avez la couleur correspondante, recuperez la moitier de votre mise.")
    elif pair_num is False and pair_random is False:
        cash_pool += somme_mise * 0.5
        print("Vous avez la couleur correspondante, recuperez la moitier de votre mise.")
    else:
        print("Vous avez perdu. Plus de chance la prochaine fois")

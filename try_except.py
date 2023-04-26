nom= input("quel est votre nom ?")
age = input ("quel est votre age ?")
try:
    age_prochain= int(age)+1
    # il faut convertir age en entier pour effectuer l'operation
except:
    print("erreur !! vous devez rentrer un nombre pour l'age")
else:
    # fait attention la concatenation sefait qu'avec des caine de caracter
    # pour ce la il faut convertir l'age de type entier en une chaine de caractaire
    #  a l'aide de la fonction str (age)
    print( "vous vous appelez"+nom +", vous avez " + str(age)+ " ans .")
    print("l'an prochain  vous aurez "+ str(age_prochain)+"ans")
print("Choissisez un mode ! (1:Encryptage-décryptage, 2: Jeu !)")
mode = int(input())

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def inliste(liste,letrre):
    # Vérifie si un caractère "letrre" est dans une liste
    # Admet un str de longueur 1 et ladite liste et retourne un booléen
    for caractere in liste:
        if letrre == caractere:
            return True
    return False

def check1(mot):
    # Utilise la fonction inliste pour vérifier si un mot est valide
    # Admet un Str et retourne un booléen
    global alphabet
    for lettre in mot:
        if not(inliste(alphabet,lettre)):
            print("Entrez une suite de caracteres sans accents,sans majusucle et sans espaces")
            return False
    return True

def check2(chiffre):
    # Utilise la fonction inliste pour vérifier si un décalage est valide
    # Admet un Int et renvoie un booléen
    for ch in chiffre:
        if not(inliste(["1","2","3","4","5","6","7","8","9","0","-"],ch)):
            print("Entrez un entier naturel")
            return False
        return True
        
mot_decode = "#"
code_decalage = "#"

while not(check1(mot_decode)):
    mot_decode = input("Entrez le mot à encoder => ")
    
while not(check2(code_decalage)):
    code_decalage = input("Entrez le décalage => ")

#Et paf ça fait Le Str devient Int
code_decalage = int(code_decalage)
    
int(code_decalage)
def transliste(mot):
    #Transforme un Str en liste
    liste = []
    for lettre in mot_decode:
        liste.append(lettre)
    return liste

def indexfindr(alphabet,lettre_decod):
    # Trouve l'index de la lettre concernée dans l'alphabet
    count = 0
    for lettre in alphabet:
        if lettre_decod == lettre:
            return count
        count += 1

def affichage_sympa(ls_mot_decode):
    #Transforme une liste en Str
    mot_sympa = ""
    for lettre in ls_mot_decode:
        mot_sympa = mot_sympa+lettre
    return mot_sympa

def adapt(index):
    #Adapte les décalages au dessus de 26 (27 => 1)
    global alphabet
    return index%len(alphabet)

def cesar(mot_decode,code_decalage):
    #Fonction principale : admet un mot et un code de décalage et renvoie un str
    global alphabet
    ls_mot_a_decod = transliste(mot_decode)
    ls_mot_decode = []
    for lettre in ls_mot_a_decod:
        ls_mot_decode.append(alphabet[adapt(indexfindr(alphabet,lettre)+code_decalage)])
    return affichage_sympa(ls_mot_decode)

if mode == 1:
    mot_decode = "#"
    code_decalage = "#"
    while not(check1(mot_decode)):
        mot_decode = input("Entrez le mot à encoder => ")
    while not(check2(code_decalage)):
        code_decalage = input("Entrez le décalage => ")
    print(cesar(mot_decode,code_decalage))
    #Et paf ça fait Le Str devient Int
    code_decalage = int(code_decalage)

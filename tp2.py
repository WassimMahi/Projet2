#Wassim Mahieddine 20142332 29-04-2024

#Ce programme donne le jeu « Cueillette de sous ». Le but du jeu est de cliquer sur les cases pour trouver les pièces cachées.
# Si une pièce est trouvée, elle est affichée. Si une case vide est cliquée, un compteur d'erreurs est incrémenté.
# Le jeu est gagné lorsque toutes les pièces sont trouvées, et perdu lorsque le compteur d'erreurs atteint 3.




def init():
    global errorCounter, piecesRestantes
    errorCounter = 0  # Initialise le compteur d'erreurs
    piecesRestantes = 0  # Initialise le nombre de pieces restantes
    main = document.querySelector("#main")
    main.innerHTML = """
      <button onclick="nouvellePartie()" class="centeredButton">Nouvelle partie</button>
      <div id="styleJouer">Jouer !</div> <!-- affichage des erreurs -->
      <div id="styleErreurs">Erreurs: 0</div> <!-- affichage des erreurs -->
      <div id="stylePiecesRestantes">Nombre des sous cachés: 0</div> <!-- affichage des pieces restantes -->
      <div id="jeu" class="centered">
      <!-- Table content -->
      <table>
      <tr>                                            
        <td id="case0" onclick="clic(0)"></td>
        <td id="case1" onclick="clic(1)"></td>
        <td id="case2" onclick="clic(2)"></td>
        <td id="case3" onclick="clic(3)"></td>
        <td id="case4" onclick="clic(4)"></td>
        <td id="case5" onclick="clic(5)"></td>
        <td id="case6" onclick="clic(6)"></td>
        <td id="case7" onclick="clic(7)"></td>
        <td id="case8" onclick="clic(8)"></td>
        <td id="case9" onclick="clic(9)"></td>
      </tr>
      <tr>
        <td id="case10" onclick="clic(10)"></td>
        <td id="case11" onclick="clic(11)"></td>
        <td id="case12" onclick="clic(12)"></td>
        <td id="case13" onclick="clic(13)"></td>
        <td id="case14" onclick="clic(14)"></td>
        <td id="case15" onclick="clic(15)"></td>
        <td id="case16" onclick="clic(16)"></td>
        <td id="case17" onclick="clic(17)"></td>
        <td id="case18" onclick="clic(18)"></td>
        <td id="case19" onclick="clic(19)"></td>
      </tr>
      <tr>
        <td id="case20" onclick="clic(20)"></td>
        <td id="case21" onclick="clic(21)"></td>
        <td id="case22" onclick="clic(22)"></td>
        <td id="case23" onclick="clic(23)"></td>
        <td id="case24" onclick="clic(24)"></td>
        <td id="case25" onclick="clic(25)"></td>
        <td id="case26" onclick="clic(26)"></td>
        <td id="case27" onclick="clic(27)"></td>
        <td id="case28" onclick="clic(28)"></td>
        <td id="case29" onclick="clic(29)"></td>
      </tr>
      <tr>
        <td id="case30" onclick="clic(30)"></td>
        <td id="case31" onclick="clic(31)"></td>
        <td id="case32" onclick="clic(32)"></td>
        <td id="case33" onclick="clic(33)"></td>
        <td id="case34" onclick="clic(34)"></td>
        <td id="case35" onclick="clic(35)"></td>
        <td id="case36" onclick="clic(36)"></td>
        <td id="case37" onclick="clic(37)"></td>
        <td id="case38" onclick="clic(38)"></td>
        <td id="case39" onclick="clic(39)"></td>
      </tr>
      <tr>
        <td id="case40" onclick="clic(40)"></td>
        <td id="case41" onclick="clic(41)"></td>
        <td id="case42" onclick="clic(42)"></td>
        <td id="case43" onclick="clic(43)"></td>
        <td id="case44" onclick="clic(44)"></td>
        <td id="case45" onclick="clic(45)"></td>
        <td id="case46" onclick="clic(46)"></td>
        <td id="case47" onclick="clic(47)"></td>
        <td id="case48" onclick="clic(48)"></td>
        <td id="case49" onclick="clic(49)"></td>
      </tr>
      <tr>
        <td id="case50" onclick="clic(50)"></td>
        <td id="case51" onclick="clic(51)"></td>
        <td id="case52" onclick="clic(52)"></td>
        <td id="case53" onclick="clic(53)"></td>
        <td id="case54" onclick="clic(54)"></td>
        <td id="case55" onclick="clic(55)"></td>
        <td id="case56" onclick="clic(56)"></td>
        <td id="case57" onclick="clic(57)"></td>
        <td id="case58" onclick="clic(58)"></td>
        <td id="case59" onclick="clic(59)"></td>
      </tr>
      <tr>
        <td id="case60" onclick="clic(60)"></td>
        <td id="case61" onclick="clic(61)"></td>
        <td id="case62" onclick="clic(62)"></td>
        <td id="case63" onclick="clic(63)"></td>
        <td id="case64" onclick="clic(64)"></td>
        <td id="case65" onclick="clic(65)"></td>
        <td id="case66" onclick="clic(66)"></td>
        <td id="case67" onclick="clic(67)"></td>
        <td id="case68" onclick="clic(68)"></td>
        <td id="case69" onclick="clic(69)"></td>
      </tr>
      <tr>
        <td id="case70" onclick="clic(70)"></td>
        <td id="case71" onclick="clic(71)"></td>
        <td id="case72" onclick="clic(72)"></td>
        <td id="case73" onclick="clic(73)"></td>
        <td id="case74" onclick="clic(74)"></td>
        <td id="case75" onclick="clic(75)"></td>
        <td id="case76" onclick="clic(76)"></td>
        <td id="case77" onclick="clic(77)"></td>
        <td id="case78" onclick="clic(78)"></td>
        <td id="case79" onclick="clic(79)"></td>
      </tr>
      <tr>
        <td id="case80" onclick="clic(80)"></td>
        <td id="case81" onclick="clic(81)"></td>
        <td id="case82" onclick="clic(82)"></td>
        <td id="case83" onclick="clic(83)"></td>
        <td id="case84" onclick="clic(84)"></td>
        <td id="case85" onclick="clic(85)"></td>
        <td id="case86" onclick="clic(86)"></td>
        <td id="case87" onclick="clic(87)"></td>
        <td id="case88" onclick="clic(88)"></td>
        <td id="case89" onclick="clic(89)"></td>
      </tr>
      <tr>
        <td id="case90" onclick="clic(90)"></td>
        <td id="case91" onclick="clic(91)"></td>
        <td id="case92" onclick="clic(92)"></td>
        <td id="case93" onclick="clic(93)"></td>
        <td id="case94" onclick="clic(94)"></td>
        <td id="case95" onclick="clic(95)"></td>
        <td id="case96" onclick="clic(96)"></td>
        <td id="case97" onclick="clic(97)"></td>
        <td id="case98" onclick="clic(98)"></td>
        <td id="case99" onclick="clic(99)"></td>
      </tr>
      </table>
      </div>"""

import random
import time

def nbPieces():
    return int(random.random() * 6) + 15   # Genere le nombre de pieces cachées entre 15 et 20


def verifVoisins(index, pieces):# Pour s'assurer qu'il n'y a pas de pieces qui se touchent
    voisins = [index - 1, index + 1, 
                 index - 9, index - 10, index - 11,
                 index + 9, index + 10, index + 11] # Les indices des cases voisines a la case [index]
    for voisin in voisins:
        if 0 <= voisin < 100 and pieces[voisin] == 1: # Verifie si la case voisine est valide et contient une piece
            return False
    return True


def initPieces(): # Initialise les pieces cachées
    global pieces, piecesRestantes
    pieces = [0] * 100 
    piecesCount = nbPieces()
    piecesRestantes = piecesCount # Nombre de pieces restantes
    document.querySelector("#stylePiecesRestantes").innerHTML = "Nombre des sous cachés: " + str(piecesCount)
    essais = 0
    essaisMax = 500  # Nombre d'essais maximum pour placer les pieces, sans quoi la boucle pourrait tourner indéfiniment

    while piecesCount > 0 and essais < essaisMax: # Tant qu'il reste des pieces a placer
        index = int(random.random() * 100)
        if pieces[index] == 0 and verifVoisins(index, pieces):
            pieces[index] = 1
            piecesCount -= 1
        essais += 1 

    return pieces


def clic(index): # Fonction qui s'execute lorsqu'on clique sur une case
    global errorCounter, piecesRestantes
    case = document.querySelector("#case" + str(index)) # La case sur laquelle on a cliqué
    if pieces[index] == 1: # Si la case contient une piece
      if case.innerHTML == "": #Pour s'assurer de ne pas changer le compteur si on clique sur une case déjà découverte
        case.innerHTML = '<img src="coste.svg" alt="Your image">' # Affiche l'image de la piece
        piecesRestantes -= 1 # Decremente le nombre de pieces restantes
        if piecesRestantes == 0:# Si le nombre de pieces restantes est nul, on a gagné
          document.querySelector("#stylePiecesRestantes").innerHTML = "Nombre des sous cachés: " + str(piecesRestantes)
          document.querySelector("#styleJouer").innerHTML = "Vous avez gagné !"
          time.sleep(10)# Preserver l'image 10 secondes
          nouvellePartie()# Reinitialise le jeu
        else:
          document.querySelector("#stylePiecesRestantes").innerHTML = "Nombre des sous cachés: " + str(piecesRestantes) # Met a jour le nombre de pieces restantes
    else:
        if case.innerHTML == "": #si la case est vide
            errorCounter += 1  # Incremente le compteur d'erreurs
            if errorCounter == 3:# Si le nombre d'erreurs atteint 3 on a perdu
              document.querySelector("#styleErreurs").innerHTML = "Erreurs: " + str(errorCounter)  # Update le compteur d'erreurs
              document.querySelector("#styleJouer").innerHTML = "Vous avez perdu!"
              time.sleep(10)  # Preserver l'image 10 secondes
              nouvellePartie()  # Reinitialise le jeu
            else:
              document.querySelector("#styleErreurs").innerHTML = "Erreurs: " + str(errorCounter)


def calculerChiffres(pieces):# Calcule le nombre de pieces cachées autour de chaque case
  for i in range(100):
    if pieces[i] == 1:
      continue # Si la case contient une piece, on passe a la case suivante
    voisins = [] # Les indices des cases voisines a la case i
    if i % 10 != 9:  # Verifie si on est pas a l'extreme droite
      voisins.append(i + 1)
      if i % 10 != 0 and i - 9 >= 0:  # Verifie si on est pas a l'extreme gauche et si i-9 est un index valide
        voisins.append(i - 9)
      if i % 10 != 0 and i + 11 < 100:  # Verifie si on est pas a l'extreme gauche et si i+11 est un index valide
        voisins.append(i + 11)
    if i % 10 != 0:  # Verifie si on est pas a l'extreme gauche
      voisins.append(i - 1)
      if i % 10 != 9 and i - 11 >= 0:  # Verifie si on est pas a l'extreme droite et si i-11 est un index valide
        voisins.append(i - 11)
      if i % 10 != 9 and i + 9 < 100:  # Verifie si on est pas a l'extreme droite et si i+9 est un index valide
        voisins.append(i + 9)
    voisins.extend([i - 10, i + 10])
    count = 0
    case = document.querySelector("#case" + str(i)) 
    case.innerHTML = ""
    if i % 10 == 0:  # Verifie si on est a l'extreme gauche
      if i - 9 >= 0:  # Verifie si i-9 est un index valide
        voisins.append(i - 9)
      if i + 11 < 100:  # Verifie si i+11 est un index valide
        voisins.append(i + 11)
    if i % 10 == 9:  # Verifie si on est a l'extreme droite
      if i - 11 >= 0:  # Verifie si i-11 est un index valide
        voisins.append(i - 11)
      if i + 9 < 100:  # Verifie si i+9 est un index valide
        voisins.append(i + 9)
    if i < 10:  # Verifie si on est dans la premiere rangee
      if i == 0:  # Cas spécial pour i=0
        voisins.remove(1)  # Supprime l'indice 1 de la liste des voisins
      if i == 9:  # Cas spécial pour i=9
        voisins.remove(8)  # Supprime l'indice 8 de la liste des voisins
    if i >= 90:  # Verifie si on est dans la derniere rangee
      if i == 90:  # Cas spécial pour i=90
        voisins.remove(91)  # Supprime l'indice 91 de la liste des voisins
      if i == 99:  # Cas spécial pour i=99
        voisins.remove(98)  # Supprime l'indice 98 de la liste des voisins
    for voisin in voisins:
      if 0 <= voisin < 100 and pieces[voisin] == 1:
        count += 1
    if count > 0:
      case.innerHTML = str(count)


def nouvellePartie():# Fonction qui s'execute lorsqu'on clique sur le bouton "Nouvelle partie" 
    init() # Initialise le jeu
    pieces = initPieces() # Initialise les pieces cachées
    calculerChiffres(pieces) # Calcule le nombre de pieces cachées autour de chaque case



##########################
####FONCTIONS DE TESTS####
##########################


def testNbPieces():
    # Verifier que la valeur retournée est dans l'intervalle spécifié
    result = nbPieces()
    assert result >= 15 and result <= 20

def testverifVoisins():
    # verifier si valeur correct est retournee dans l'absence d'element voisin
    pieces = [0] * 100
    assert verifVoisins(0, pieces)

    # verifier si valeur non correct est retournee quand il y'a element voisin
    pieces[1] = 1
    assert not verifVoisins(0, pieces)

def testInitPieces():
    # on verifie si tableau a le nombre correct de pieces
    global pieces, piecesRestantes
    pieces = 0           # initialisation avant debut des tests
    piecesRestantes = 0  
    initPieces()
    
    # # On verifie si le tableau a 100 elements
    assert len(pieces) == 100

    # on verifie que piecesRestantes est initialisée correctement
    assert piecesRestantes >= 15 and piecesRestantes <= 20

    # on verifie que l'affichage est effectué correctement
    assert document.querySelector("#stylePiecesRestantes").innerHTML == "Nombre des sous cachés: " + str(piecesRestantes)
    
    # On verifie que la fonction genere des pieces sans pieces adjacentes
    for i in range(100):
        if pieces[i] == 1:
            assert verifVoisins(i, pieces) == True
    
    
    

def testCalculerChiffres():
    # on teste si la fonction calcule les nombres correct pour une case sans pièces adjacentes
    global pieces
    pieces = [0] * 100
    pieces[0] = 0                   # n'a pas de pieces adjacentes
    calculerChiffres(pieces)
    contenuCase0 = document.querySelector("#case0").innerHTML
    assert contenuCase0 == ""      #vide car n'a pas de pièces adjaventes
    

    
    
# Lancer les tests
testNbPieces()
testverifVoisins()
testInitPieces()
testCalculerChiffres()


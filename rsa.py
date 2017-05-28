from list import liste
import random

# Fonction qui choisit un nombre premier different d'un autre
def nbPremierDiff(src) :
  dest = liste[r.randrange(len(liste))]
  while src == dest:
    dest = liste[r.randrange(len(liste))]
  return dest
# Algorithme d'Euclide pour le pgcd 
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
# Conversion message equivalent ascii
def convert_ascii(message) :
  i = 0
  message_ascii = ""
  bigger = 0
  while i != len(message):
    c = ord(message[i])
    if c > bigger :
      bigger = c
    message_ascii = message_ascii + str(c)
    i = i + 1
  return [bigger, message_ascii]
######## Menu ########
choix = input('Salut a toi utilisateur, dis moi ce que je dois faire : \n1.Chiffrer\n2.Dechiffrer\nEntre une option du menu : ')
while choix != 1 and choix != 2 :
  choix = input('\nErreur, entrez soit 1 ou 2 : ')
######## Chiffrement ########
if choix==1:
  message = raw_input('\nOk, saisis le message que tu veux chiffrer : ')
  mm = convert_ascii(message)
  bigger = mm[0]
  message_ascii = mm[1]
  print "\n...\n"
  ####### Generation de p et q ########
  r = random.SystemRandom()
  p =liste[r.randrange(len(liste))]
  q = nbPremierDiff(p)
  n = p * q
  phi_n = (p-1)*(q-1)
  #print p, " ", q, " ", n, " ", phi_n
  ######## Choix d'un exposant e et calcul de son inverse d ########
  e = r.choice(liste)
  d = 1 
  temp = (e*d)%phi_n
  while(temp != 1):
    d = d+1
    temp = (e*d)%phi_n
  #print e, " ", d, " "
  print "Cle publique :", e, "\nModulo :", n,"\nCle prive :", d
  # n et e = cle publique
  # d = cle prive
  i = 0
  message_chiffre = ""
  while i != len(message_ascii) :
    message_chiffre = message_chiffre + str(pow(int(message_ascii[i]), e)%n)
    i = i + 1
  print "\nEt voila le travail :\n", message_chiffre
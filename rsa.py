from list import liste
import random

######## Generation de p et q ########
r = random.SystemRandom()
p =liste[r.randrange(len(liste))]
q = liste[r.randrange(len(liste))]
while p == q:
  q = liste[r.randrange(len(liste))]
n = p * q
phi_n = (p-1)*(q-1)
######## Choix d'un exposant e et calcul de son inverse d ########
e = r.choice(liste)
print pgcd(e, phi_n)
d = 1 
temp = (e*d)%phi_n
while(temp != 1):
  d = d+1
  temp = (e*d)%phi_n
# n et e = cle publique
# d = cle prive
######## Chiffrement ########
m = 10
x = pow(m, e)%n
print x
######## Dechiffrement ########
m = pow(x, d)%n
print m
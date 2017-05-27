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
######## Preparation des clefs ########
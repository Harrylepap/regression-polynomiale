#!/bin/python

import numpy as np
import matplotlib.pyplot as plt

#initialisation du générateur 
np.random.seed(2)

# génération de 1000 nombres aléatoires distribués selon la loi normale X ~ N(3, 1)
# en d'autre terme, les pages chargeront en moyenne en 3 secondes et un ecart-type de 1 seconde.
tempsChargementPages = np.random.normal(3.0, 1.0, 1000)
génération aléatoires de montants d'achat corrélés aux temps de chargement
montantAchat = np.random.normal(50.0, 10.0, 1000) / (tempsChargementPages * tempsChargementPages)


axes = plt.axes()
axes.grid()
plt.xlabel('temps de chargement en secondes')
plt.ylabel('montant des achats euros')
plt.scatter(tempsChargementPages, montantAchat)
plt.show()

# le temps de chargement de la page est notre variable prédictive
x = np.array(tempsChargementPages)
# montantAchat est la variable cible (qu'on cherche à prédire)
y = np.array(montantAchat)

p4 = np.poly1d(np.polyfit(x, y, 4))
#print p4
xp = np.linspace(0, 7, 100)
plt.scatter(c, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

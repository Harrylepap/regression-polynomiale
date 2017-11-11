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

# le temps de chargement de la page est notre variable prédictive
x = np.array(tempsChargementPages)
# montantAchat est la variable cible (qu'on cherche à prédire)
y = np.array(montantAchat)

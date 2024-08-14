# Description
Ce script Python calcule le Métabolisme de Base (MB) ajusté en fonction du poids, de la taille, de l'âge et du nombre d'entraînements par semaine. Le MB est une mesure du nombre de calories que le corps dépense au repos pour maintenir ses fonctions vitales.

La formule utilisée est la formule Harris-Benedict pour les hommes, et un facteur d'activité est appliqué pour tenir compte de l'exercice physique.

# Fonctionnalité
La fonction `calculer_mb` prend les paramètres suivants :
- `poids (en kg)` : poids de la personne.
- `taille (en cm)` : taille de la personne.
- `age (en années)` : âge de la personne.
- `entrainements_par_semaine` : nombre d'entraînements par semaine (entier).

Elle retourne le Métabolisme de Base ajusté en fonction du niveau d'activité physique.

# Formule de Calcul

Métabolisme de Base (MB) : Calculé avec la formule Harris-Benedict pour les hommes :

MB=88.362+(13.397×poids)+(4.799×taille)−(5.677× âge)

## Facteur d'activité :

0 entraînement par semaine : 1.2

- 1 à 2 entraînements par semaine : 1.375
- 3 à 4 entraînements par semaine : 1.55
- 5 à 6 entraînements par semaine : 1.725
- Plus de 6 entraînements par semaine : 1.9

MB ajusté = MB×facteur d’activité

# Notes
Le calcul du MB est basé sur la formule Harris-Benedict pour les hommes. Pour les femmes, une formule différente serait nécessaire.
Les ajustements de 300 à 500 calories par jour sont des recommandations générales pour atteindre des objectifs de perte ou de prise de poids.

# Auteur
Ce script a été développé pour fournir une estimation simple du Métabolisme de Base et de ses besoins énergétiques ajustés.
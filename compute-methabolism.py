def calculer_mb(poids, taille, age, entrainements_par_semaine):
    # Calcul du MB de base pour un homme avec la formule Harris-Benedict
    mb_base = 88.362 + (13.397 * poids) + (4.799 * taille) - (5.677 * age)
    
    facteur_activite = 0

    if entrainements_par_semaine == 0:
        facteur_activite = 1.2
    elif entrainements_par_semaine <= 2:
        facteur_activite = 1.375
    elif entrainements_par_semaine <= 4:
        facteur_activite = 1.55
    elif entrainements_par_semaine <= 6:
        facteur_activite = 1.725
    else:
        facteur_activite = 1.9
    
    mb_ajuste = mb_base * facteur_activite
    
    return mb_ajuste

# Exemple d'utilisation
poids = 115  # kg
taille = 180  # cm
age = 21  # années
entrainements_par_semaine = 4  # nombre d'entraînements par semaine

mb = calculer_mb(poids, taille, age, entrainements_par_semaine)
print(f"Le Métabolisme de Base ajusté est de : {mb:.2f} kcal/jour sans objectifs. ")
print(f"Pour un objectif de perte de poids, il faudra réduire ce nombre de 300 - 500 calories par jour. (ex: {mb - 500:.2f} kcal/jour)")
print(f"Pour un objectif de prise de poids ou de maintien, il faudra augmenter ce nombre de 300 - 500 calories par jour. (ex: {mb + 500:.2f} kcal/jour)")
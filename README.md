## Résumé de notre travail sur le TP
### Arielle Gantelet & Mathilde Cadon

### Exercice 1 :  Le jeu de la vie

Dans ce premier exercice, on découvre le jeu de la vie. Ce jeu simule, dans une grille, à partir d'un état initial, l'évolution de la vie de cellues, selon le nombre de voisins qu'elles ont, certaines meurent, certaines naissent et certaines se stabilisent.

Nous avons, à l'aide de codes donnés et d'un état inital donné (matrice Z), calculer le nombre de voisins des cellules, ce qui nous donne alors les informations suffisantes pour connaître son état à l'itération du jeu suivante. 
Ensuite, on a simulé l'évolution du jeu de la vie sur 10 états. On a pu remarquer des similitudes sur les 5 premiers états et une stabilisation sur les 3 derniers.
Egalement, nous avons repris les fonctions précédentes avec la compilation "jit", pour comparer le temps d'execution avec et sans cette compilation. Ainsi, on a pu constater qu'avec celle-ci, les codes s'exécutaient de manière bien plus rapide.
Enfin, nous avons créé un widget, pour faire varier le nombre d'itérations du jeu de la vie.

### Exercice 2 : Regression Logistique

Dans cet exercice, nous avons exploité le jeu de données MNIST. Celui-ci contient une matrice codant des images et un vecteur  associé pour expliciter le chiffre que codé.

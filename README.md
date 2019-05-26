## Résumé de notre travail sur le TP
### Arielle Gantelet & Mathilde Cadon


### Exercice 1 :  Le jeu de la vie

Dans ce premier exercice, on découvre le jeu de la vie. Ce jeu simule, dans une grille, à partir d'un état initial, l'évolution de la vie de cellues, selon le nombre de voisins qu'elles ont, certaines meurent, certaines naissent et certaines se stabilisent.

Nous avons, à l'aide de codes donnés et d'un état inital donné (matrice Z), calculer le nombre de voisins des cellules, ce qui nous donne alors les informations suffisantes pour connaître son état à l'itération du jeu suivante. 
Ensuite, on a simulé l'évolution du jeu de la vie sur 10 états. On a pu remarquer des similitudes sur les 5 premiers états et une stabilisation sur les 3 derniers.
Egalement, nous avons repris les fonctions précédentes avec la compilation "jit", pour comparer le temps d'execution avec et sans cette compilation. Ainsi, on a pu constater qu'avec celle-ci, les codes s'exécutaient de manière bien plus rapide.
Enfin, nous avons créé un widget, pour faire varier le nombre d'itérations du jeu de la vie.

### Exercice 2 : Regression Logistique

Dans cet exercice, nous avons exploité le jeu de données MNIST. Celui-ci contient une matrice (que nous appelerons X) ayant pour éléments des matrices codant des images, et un vecteur (y) associé pour expliciter le chiffre codé par un élément de X.

Tout d'abord, nous avons trié notre jeu de données MNIST, pour ne garder que dans la matrice que les éléments codant des 3 et des 7. De même, nous gardons le vecteur nous permettant de connaître le chiffre codé, 3 ou 7.
Nous avons procédé à une régression linéaire sur ce jeu de données réduit, pour obtenir notre vecteur des coefficients (w) dans un modèle de prédiction de la classe de l'image. Nous nous sommes servies de ce vecteur des coefficents pour transformer une image, à l'aide d'une formule donnée que nous avons implémenté dans notre fichier "utils". Nos images seront maintenant représentées sous la forme de vecteur.
Pour observer, l'influencce du paramètre $\alpha$ sur la transformation de notre image, nous avons créé un widget nous permettant de faire varier la valeur de ce paramètre. Afin d'avoir une meilleure observation sur l'évolution de la transformation de l'image selon le paramètre $\alpha$, nous avons créé un film avec $\alpha$ variant de 0,1 à 100 de 0,1 en 0,1.
Nous pourrons donc constater l'influence de ce paramètre sur l'ampleur de la transformation de l'image, plus $\alpha$ augmente, plus la transformation de l'image est importante.
Et pour terminer, nous avons procédé, toujours sur ce nouveau jeu de données, à une ACP. Par curiosité, nous procèderons également à une ACP sur le jeu complet.

Exercices de programmation en Python
====================================

1. Lisez le chapitre 3 de _Invent your own games with Python_ https://inventwithpython.com/invent4thed/chapter3.html où
l'auteur présente un jeu dans lequel l'ordinateur choisit un nombre au hasard que l'utilsateur doit deviner.
Assurez-vous de bien comprendre le programme proposé.  Votre mission consiste à ecrire un script python qui joue le jeu "inverse", c-à-d où c'est l'utilisateur qui pense à un nombre (par exemple entre 1 et 100) et c'est l'ordinateur qui doit le deviner.

2. Ecrire un programme qui affiche tous les nombres premiers compris entre 1 et 10000 (On rappelle qu'un nombre premier est un nombre entier qui n'admet pas d'autres diviseurs que lui même et 1). Il y a plusieurs approches possibles. Vous pouvez par exemple vous aider de la fonction:

    ---
    def is_divisor(a, b):
        """ Args: a, b integers;
             Return True if b is a divisor of a, else False"
        return a % b == 0
    ---

3. Ecrire un programme qui affiche les premières lignes du triangle de Pascal (see https://www.youtube.com/watch?v=XMriWTvPXHI). Par exemple:

    ---
    %run triangle-de-Pascal.py
    1 
    1   1 
    1   2   1 
    1   3   3   1 
    1   4   6   4   1 
    1   5  10  10   5   1 
    1   6  15  20  15   6   1 
    1   7  21  35  35  21   7   1 
    1   8  28  56  70  56  28   8   1 
    1   9  36  84 126 126  84  36   9   1 
    ---

Pour résoudre ce problème, une solution consiste à stocker les valeurs de la ligne courante dans une liste Python, et d'écrire une fonction qui étant donnée une liste en argument, calcule et renvoit la ligne suivante dans une nouvelle liste.


4. Lisez le chapitre 8 de _Automate the boring stuff_ (http://automatetheboringstuff.com/chapter8/). Ecrire un programme qui ouvre et lit un fichier texte, puis affiche toutes les lignes qui contiennent un mot donné, par exemple "Cogmaster". 


5. (optionnel: seulement pour ceux qui se sentent capables et sont motivés) Ecrire un programme qui simule une machine RodRego à 10 registres (http://sites.tufts.edu/rodrego/). Le programme est stocké dans un fichier texte qui est lu, puis executé.  Votre programme doit contenir une fonction qui etant donnée les 10 valeurs initiales des registres, et le programme, renvoit les nouvelles valeurs des registres quand l'instruction END est atteinte.






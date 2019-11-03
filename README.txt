*** README.md ***
*****************

<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/a/a2/Pac-Man_Logo.svg/1280px-Pac-Man_Logo.svg.png" alt="PacMan" />

<h1>Introduction</h1>


<p> Ce projet IN104 concerne le développement d'une version du jeu PacMan.</p>

<p>l'agent PacMan est commandé par l'utilisateur à travers une interface graphique créée à partir de l'extension Pygame de Python. Il doit se déplacer dans un "labyrinthe" en faisant face à des agents fantômes,dont les comportements ont été créés à partir d'une IA ET d'algorithmes de recherche de chemin.</p>

<h1>Equipe</h1>
 

<p> <em>Khaoula Belahsen</em> : khaoula.belahsen@ensta-paristech.fr </p>
<p><em>Corentin Giguet</em> : corentin.giguet@ensta-paristech.fr </p>



<br/><p><em>Sous l'encadrement de : Leandro Batista</em></p>

## Motivation

<p>L'objectif de notre projet est de réaliser un jeu de labyrinthe de type Pac-Man.</p>
<p>La réalisation de ce jeu s'inscrit dans le cadre du projet IN104 du cursus de 1ère année de l'ENSTA ParisTech.</p>

<p>Il vise à nous familiariser avec le développement d'une intelligence artificielle au service d'un jeu.</p>

### Prérequis de fonctionnement
------------------------------

<p>Pour pouvoir exécuter le jeu correctement, vous devez avoir installé Pygame sur votre machine.</p>
<p> Voici un lien qui montre comment l'<a href="https://www.pygame.org/wiki/GettingStarted">installer</a> sinon. 


<p> <em>Commande pour commencer le jeu :</em> </p>

<pre><code>  python3 game.py </code></pre>

#### Commandes importantes
-------------------------

<ol>
   <li> <em>Flèche haut</em> : déplacement en haut </li>
   <li> <em>Flèche bas</em> : déplacement vers le bas </li>
   <li> <em>Flèche droite</em> : déplacement vers la droite </li>
   <li> <em>Flèche gauche</em> : déplacement vers la gauche </li>
   <li> <em>Enter</em> : Commencer le jeu </li>
   <li> <em>Delete</em> : revenir au menu principal </li>
   <li> <em>Escape</em> : Sortir du jeu </li>
</ol>



### Liste des fichiers 
----------------------
<ol>
   <li> <em>classe_labyrinthe.py<em> : Classe Labyrinthe, Niveau du jeu Pacman. </li>   
   <li> <em>classe_pacman.py<em> : Classe du perso Pacman du jeu Pacman. </li>
   <li> <em>classe_ghost.py<em> : Classe des persos fantôme du jeu Pacman. </li>
   <li> <em>classe_gums.py<em> : Classe des pac-gommes du jeu Pacman. </li>
   <li> <em>classe_bonus.py<em> : Classe des bonus fruits du jeu Pacman. </li>
   <li> <em>constantes.py<em> : fichier contenant toutes les constantes du jeu. </li>
   <li> <em>pacman.py<em> : code de jeu du pacman seul sur la maze. </li> 
   <li> <em>level.txt<em> : reporésentation de la matrice du labyrinthe. </li>

</ol>


<br/><p>Pour plus de détails, cliquez <a href="https://gitlab.data-ensta.fr/belahsen/IN104/tree/master/progs">ici</a> </p>

### Comportement des agents fantômes "ghosts"
--------------------------------------------

<p>Les fantômes doivent se mouvoir dans le labyrinthe dans respectant les couloirs autorisés. Ils peuvent être soit aléatoires ou suivre un comportement basé sur des algorithmes de PathFinding et de search. </p>

<p> Les détails du comportement des ghosts ou fantômes se trouve <a href="https://gitlab.data-ensta.fr/belahsen/IN104/blob/master/Ghosts%20behaviour.docx">ici</a></p>

#### Méthode Find 
-----------------

Méthode de la classe Ghost qui se trouve dans le fichier <a href="https://gitlab.data-ensta.fr/belahsen/IN104/blob/master/progs/classes.py">classes.py</a></p> 

<pre><code>
	def find(self, x, y):
	.
	.
	   return set(possible)
</code></pre>
<p> Cette méthode retourne les directions à prendre pour aller vers le quart de maze où se trouve le pacman.</p>

#### Méthode de déplacement 
---------------------------

<p>Les Ghosts ont deux modes de déplacement Scatter et Hunt, gérés par un timer.</p>

<pre><code>
	def deplacer_continu(self, direction_continu, x, y, hunt):
</code></pre>



     
### Tests
---------



###### Test 1 : 

<p> À partir du fichier <a href="https://gitlab.data-ensta.fr/belahsen/IN104/blob/master/progs/tests/test.py">test.py</a>

<p> Pour run le jeu, essais sur le son etc..  :</p>

<pre><code>  python3 test.py </code></pre>

###### Test 2 : 

<p> À partir du fichier <a href="https://gitlab.data-ensta.fr/belahsen/IN104/blob/master/progs/tests/pacman.py">pacman.py</a>

<p> Pour run le Pac-Man tout seul sur la maze :</p>

<pre><code>  python3 pacman.py </code></pre>

###### Test 3 : 

<p> À partir du fichier <a href="https://gitlab.data-ensta.fr/belahsen/IN104/blob/master/progs/tests/ghost.py">ghost.py</a>

<p> Pour run le Ghost tout seul sur la maze :</p>

<pre><code>  python3 ghost.py </code></pre>





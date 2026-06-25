# Progression annuelle NSI Terminale - Tunisie 2026-2027

- Statut : prototype annuel non publiable.
- Base horaire : calendrier scolaire Tunisie 2026-2027, voir `calendar_2026_2027_tunisia.md`.
- Hypothèse horaire NSI Terminale : 210 h annuelles, soit environ 6 h hebdomadaires sur les 898 h de classe.
- Projet exigé : au moins 25 % de l'horaire, soit 52,5 h.
- Projet planifié : 60 h, soit 28,6 %.
- Décision pédagogique : aucune ressource n'est publiée ; aucune capacité n'est déclarée `covered` par cette progression.
- Séquence pilote existante : `terminale/sequences/s01_structures_donnees_interfaces_implementations/` conservée comme prototype à découper.

## Répartition annuelle

| Séquence | Mois dominant | Volume | Projet | Capacités principales | Évaluation prévue | Période sensible |
|---|---:|---:|---:|---|---|---|
| T00 - Reprise Python, tests, complexité de base | septembre | 8 h | 2 h | T-HIST-01, T-LANG-03, T-LANG-05 | diagnostic + mini-problème | reprise |
| T01 - Structures abstraites, interface, implémentation | septembre | 10 h | 2 h | T-STRUCT-01 | analyse courte | favorable |
| T02 - POO utile : classes, attributs, méthodes | septembre-octobre | 10 h | 2 h | T-STRUCT-02, T-LANG-04 | programmation guidée | favorable |
| T03 - Piles, files, dictionnaires, choix de structure | octobre-novembre | 12 h | 3 h | T-STRUCT-03 | TP noté court | favorable |
| T04 - Récursivité et preuves de terminaison | novembre | 10 h | 2 h | T-LANG-02 | devoir court | favorable |
| T05 - Arbres binaires, taille, hauteur, parcours | novembre | 10 h | 2 h | T-STRUCT-04, T-ALGO-01 | exercices + code | favorable |
| T06 - Arbres binaires de recherche | décembre | 10 h | 2 h | T-ALGO-01 | TP + analyse | fin de période |
| T07 - Graphes : modélisation, listes/matrices | janvier | 10 h | 3 h | T-STRUCT-05 | modélisation | favorable |
| T08 - Graphes : BFS, DFS, cycles, chemins | janvier | 12 h | 3 h | T-ALGO-02 | TP + sujet pratique | favorable |
| T09 - Bases de données relationnelles : modèle, clés, contraintes | janvier-février | 12 h | 3 h | T-BDD-01, T-BDD-02 | étude de schéma | Ramadan à partir du 8 février |
| T10 - SQL : SELECT, WHERE, JOIN, ORDER BY, INSERT, UPDATE, DELETE | février-mars | 12 h | 4 h | T-BDD-03 | pratique SQL | Ramadan et Aïd al-Fitr |
| T11 - Systèmes : SoC, processus, ordonnancement, interblocage | mars | 10 h | 2 h | T-ARCH-01, T-ARCH-02 | analyse de situations | reprise après Aïd |
| T12 - Réseaux : routage RIP/OSPF, lien avec graphes | mars-avril | 10 h | 3 h | T-ARCH-03 | exercice réseau | favorable |
| T13 - Sécurité : chiffrement symétrique/asymétrique, HTTPS | avril | 10 h | 3 h | T-ARCH-04 | étude de protocole | favorable |
| T14 - Langages : modularité, API, paradigmes, bugs | avril-mai | 10 h | 3 h | T-LANG-03, T-LANG-04, T-LANG-05 | revue de code | Aïd al-Adha en mai |
| T15 - Calculabilité, programme comme donnée, arrêt | mai | 8 h | 1 h | T-LANG-01 | questions argumentées | période sensible |
| T16 - Diviser pour régner, tri fusion | mai | 10 h | 3 h | T-ALGO-03 | devoir algorithmique | période sensible |
| T17 - Programmation dynamique | mai-juin | 10 h | 3 h | T-ALGO-04 | problème guidé | favorable après Aïd |
| T18 - Boyer-Moore | juin | 8 h | 2 h | T-ALGO-05 | analyse d'algorithme | fin d'année |
| T19 - Bac écrit, pratique, Grand Oral, projet final | juin | 18 h | 12 h | synthèse T-HIST-01 à T-ALGO-05 | entraînements écrits et pratiques | synthèse |
| **Total** | année | **210 h** | **60 h** | toutes les capacités identifiées | évaluations réparties | marge intégrée |

## T00 - Reprise Python, tests, complexité de base

- Mois : septembre.
- Volume horaire : 8 h, dont 2 h de projet.
- Capacités officielles : T-HIST-01, T-LANG-03, T-LANG-05.
- Documents à produire : fiche reprise Python, fiche tests, fiche complexité intuitive, mini-guide d'organisation du code.
- TD : lecture de fonctions, cas limites, estimation du nombre d'opérations.
- TP : reprendre un petit programme de Première, ajouter tests et messages d'erreur.
- Évaluation : diagnostic sans note lourde, puis mini-problème de programmation.
- Sujet pratique : fonctions pures, tests unitaires simples, séparation entrée-traitement-sortie.
- Projet : mise en place du carnet de bord et du dépôt de groupe.
- Différenciation : rappels Python guidés pour élèves fragiles ; analyse de complexité comparative pour élèves avancés.
- Ressources Drive candidates : rechercher fiches Python, tests, complexité, sujets pratiques d'introduction.
- Lien bac écrit : analyse de code et justification de complexité simple.
- Lien bac pratique : qualité des fonctions et tests.
- Lien Grand Oral : expliquer un bug, une hypothèse de test ou un choix de structure.

## T01 - Structures abstraites, interface, implémentation

- Mois : septembre.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-STRUCT-01.
- Documents à produire : cours sur type abstrait, interface, implémentation ; TD de choix de représentation ; TP court de structure abstraite.
- TD : identifier opérations, préconditions, postconditions et invariants d'une structure.
- TP : écrire deux implémentations d'une même interface très simple.
- Évaluation : analyse courte d'une interface et de deux implémentations proposées.
- Sujet pratique : mini-bibliothèque Python avec tests d'interface.
- Projet : choisir l'interface d'un composant du projet annuel.
- Différenciation : tableaux d'opérations fournis pour certains élèves ; extension sur coût asymptotique.
- Ressources Drive candidates : supports sur structures abstraites, piles, files, API.
- Lien bac écrit : distinguer interface et représentation interne.
- Lien bac pratique : respecter une spécification sans dépendre de l'implémentation.
- Lien Grand Oral : justifier un choix technique par les usages attendus.

## T02 - POO utile : classes, attributs, méthodes

- Mois : septembre-octobre.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-STRUCT-02, T-LANG-04.
- Documents à produire : cours POO utile, fiche méthode `__init__`, TD de lecture de classe, TP objet simple.
- TD : distinguer attribut de classe, attribut d'instance, méthode et fonction externe.
- TP : créer une classe contrôlée par tests.
- Évaluation : programmation guidée avec contraintes d'interface.
- Sujet pratique : créer une classe représentant un objet métier simple.
- Projet : définir les objets utiles du projet annuel sans surconcevoir.
- Différenciation : squelette de classe pour élèves fragiles ; variantes avec invariants pour élèves avancés.
- Ressources Drive candidates : anciens TP classes, exercices d'objets, mini-projets.
- Lien bac écrit : prédire l'état d'un objet après appels de méthodes.
- Lien bac pratique : écrire une classe conforme à une spécification.
- Lien Grand Oral : expliquer l'intérêt d'encapsuler un état.

## T03 - Piles, files, dictionnaires, choix de structure

- Mois : octobre-novembre.
- Volume horaire : 12 h, dont 3 h de projet.
- Capacités officielles : T-STRUCT-03.
- Documents à produire : cours pile-file-dictionnaire, TD progressif, TP simulateur, fiche erreurs fréquentes.
- TD : choisir entre pile, file, tableau et dictionnaire selon opérations dominantes.
- TP : simuler une file d'attente et une pile d'annulation.
- Évaluation : TP noté court avec justification du choix de structure.
- Sujet pratique : implémenter une pile ou une file avec tests de cas limites.
- Projet : intégrer une pile, une file ou un dictionnaire dans un micro-projet.
- Différenciation : opérations fournies sous forme de cartes ; extension sur coût des opérations.
- Ressources Drive candidates : exercices piles/files, scripts dictionnaires, sujets pratiques.
- Lien bac écrit : raisonner sur états successifs d'une structure.
- Lien bac pratique : manipuler une structure avec tests d'erreur.
- Lien Grand Oral : relier structure de données et usage concret.

## T04 - Récursivité et preuves de terminaison

- Mois : novembre.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-LANG-02.
- Documents à produire : cours récursivité, fiche méthode cas de base, TD arbre d'appels, TP fonctions récursives.
- TD : identifier cas de base, appel récursif et variant de terminaison.
- TP : écrire et tester des fonctions récursives simples puis imbriquées.
- Évaluation : devoir court avec trace d'exécution et justification de terminaison.
- Sujet pratique : récursivité sur liste ou chaîne.
- Projet : utiliser récursivité seulement si le problème s'y prête.
- Différenciation : schémas d'appels guidés ; extension sur récursivité terminale comme culture.
- Ressources Drive candidates : fiches récursivité, exercices arbres d'appels.
- Lien bac écrit : démontrer une terminaison simple.
- Lien bac pratique : coder une fonction récursive correcte sur cas limites.
- Lien Grand Oral : expliquer le lien entre définition récursive et programme.

## T05 - Arbres binaires, taille, hauteur, parcours

- Mois : novembre.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-STRUCT-04, T-ALGO-01.
- Documents à produire : cours arbres, TD représentations, TP parcours, fiche vocabulaire.
- TD : calculer taille, hauteur, feuilles et nœuds internes.
- TP : représenter un arbre et écrire des parcours simples.
- Évaluation : exercices + code court.
- Sujet pratique : parcourir un arbre fourni.
- Projet : représenter une hiérarchie simple.
- Différenciation : arbres dessinés et complétés ; extension sur coût des parcours.
- Ressources Drive candidates : supports arbres, exercices parcours.
- Lien bac écrit : lire et compléter un arbre.
- Lien bac pratique : coder un parcours sur structure fournie.
- Lien Grand Oral : expliquer pourquoi un arbre convient à une hiérarchie.

## T06 - Arbres binaires de recherche

- Mois : décembre.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-ALGO-01.
- Documents à produire : cours ABR, TD insertion/recherche, TP recherche dans ABR, fiche limites.
- TD : vérifier la propriété d'un ABR, insérer une valeur, repérer un arbre dégénéré.
- TP : coder recherche et insertion avec tests.
- Évaluation : TP + analyse de cas.
- Sujet pratique : recherche dans un ABR.
- Projet : utiliser ABR seulement si l'ordre et les recherches le justifient.
- Différenciation : valeurs guidées ; extension sur équilibre non exigé.
- Ressources Drive candidates : exercices ABR, scripts arbres.
- Lien bac écrit : appliquer la propriété d'ordre.
- Lien bac pratique : manipuler un ABR simple.
- Lien Grand Oral : expliquer les limites d'un ABR non équilibré.

## T07 - Graphes : modélisation, listes/matrices

- Mois : janvier.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-STRUCT-05.
- Documents à produire : cours graphes comme structures relationnelles, TD modélisation, TP listes et matrices d'adjacence.
- TD : choisir sommets, arêtes, orientation, pondération et représentation.
- TP : convertir entre liste d'adjacence et matrice d'adjacence.
- Évaluation : modélisation de problème et choix de représentation.
- Sujet pratique : construire un graphe depuis des données simples.
- Projet : modéliser le domaine du projet sous forme de graphe si pertinent.
- Différenciation : graphes dessinés ; extension sur mémoire et coût des représentations.
- Ressources Drive candidates : supports graphes, activités réseaux, cartes.
- Lien bac écrit : comparer représentations.
- Lien bac pratique : construire et interroger une représentation.
- Lien Grand Oral : justifier un modèle relationnel.

## T08 - Graphes : BFS, DFS, cycles, chemins

- Mois : janvier.
- Volume horaire : 12 h, dont 3 h de projet.
- Capacités officielles : T-ALGO-02.
- Documents à produire : cours parcours de graphes, TD traces BFS/DFS, TP chemin, fiche cas limites.
- TD : tracer BFS et DFS, distinguer pile et file, identifier sommets visités.
- TP : implémenter parcours sur listes d'adjacence et traiter absence de chemin.
- Évaluation : TP + sujet pratique.
- Sujet pratique : parcourir un graphe et répondre à une question de connexité ou chemin.
- Projet : ajouter un parcours limité à un problème choisi.
- Différenciation : graphes de petite taille ; extension sur cycles et composantes.
- Ressources Drive candidates : sujets pratiques graphes, exercices parcours.
- Lien bac écrit : expliquer un ordre de visite.
- Lien bac pratique : coder BFS ou DFS sur graphe fourni.
- Lien Grand Oral : relier parcours et problème réel.
- Décision : cette progression isole BFS/DFS ici ; la séquence pilote Terminale ne suffit pas à elle seule.

## T09 - Bases de données relationnelles : modèle, clés, contraintes

- Mois : janvier-février.
- Volume horaire : 12 h, dont 3 h de projet.
- Capacités officielles : T-BDD-01, T-BDD-02.
- Documents à produire : cours modèle relationnel, fiche clés, TD schémas, TP SQLite lecture.
- TD : repérer relation, attribut, domaine, clé primaire et clé étrangère.
- TP : inspecter une base simple sans données personnelles.
- Évaluation : étude de schéma et contraintes.
- Sujet pratique : requêtes simples de consultation.
- Projet : concevoir un petit schéma avec données fictives.
- Différenciation : schéma annoté ; extension sur anomalies de mise à jour.
- Ressources Drive candidates : anciens supports SQL, bases exemples.
- Lien bac écrit : analyser schéma et contraintes.
- Lien bac pratique : interroger une base SQLite.
- Lien Grand Oral : expliquer pourquoi structurer les données.

## T10 - SQL : SELECT, WHERE, JOIN, ORDER BY, INSERT, UPDATE, DELETE

- Mois : février-mars.
- Volume horaire : 12 h, dont 4 h de projet.
- Capacités officielles : T-BDD-03.
- Documents à produire : cours SQL, TD requêtes progressives, TP base projet, fiche erreurs SQL.
- TD : écrire SELECT, filtrer, trier, joindre, insérer, mettre à jour, supprimer.
- TP : manipuler une base de données fictive avec tests de requêtes.
- Évaluation : pratique SQL en période Ramadan, sans charge excessive.
- Sujet pratique : requêtes SQL sur schéma fourni.
- Projet : alimenter et interroger la base du projet.
- Différenciation : requêtes à trous ; extension sur jointures multiples.
- Ressources Drive candidates : bases SQLite, listes de requêtes, sujets pratiques.
- Lien bac écrit : justifier une jointure et une condition.
- Lien bac pratique : écrire des requêtes fiables.
- Lien Grand Oral : discuter données, qualité et limites.

## T11 - Systèmes : SoC, processus, ordonnancement, interblocage

- Mois : mars.
- Volume horaire : 10 h, dont 2 h de projet.
- Capacités officielles : T-ARCH-01, T-ARCH-02.
- Documents à produire : cours systèmes sur puce, processus, ordonnancement, interblocage ; TD diagrammes ; TP observation système.
- TD : lire des états de processus et repérer un risque d'interblocage.
- TP : observer processus et ressources dans un environnement contrôlé.
- Évaluation : analyse de situations.
- Sujet pratique : simulation simple d'ordonnancement.
- Projet : documenter les contraintes système d'une application.
- Différenciation : scénarios guidés ; extension sur politiques d'ordonnancement.
- Ressources Drive candidates : supports OS, scripts processus.
- Lien bac écrit : raisonner sur processus et ressources.
- Lien bac pratique : interpréter une simulation.
- Lien Grand Oral : expliquer les effets visibles d'un système invisible.

## T12 - Réseaux : routage RIP/OSPF, lien avec graphes

- Mois : mars-avril.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-ARCH-03.
- Documents à produire : cours routage, TD tables, TP simulation de graphe réseau.
- TD : construire une table de routage simple, comparer distance et état de lien.
- TP : simuler une propagation d'information de routage.
- Évaluation : exercice réseau.
- Sujet pratique : calcul de chemins sur petit réseau.
- Projet : relier graphe et réseau dans une note technique.
- Différenciation : réseau à quatre nœuds ; extension sur convergence.
- Ressources Drive candidates : activités réseau, graphes pondérés.
- Lien bac écrit : expliquer RIP et OSPF à partir d'un exemple.
- Lien bac pratique : appliquer un parcours ou coût sur graphe.
- Lien Grand Oral : expliquer comment Internet choisit des routes.

## T13 - Sécurité : chiffrement symétrique/asymétrique, HTTPS

- Mois : avril.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-ARCH-04.
- Documents à produire : cours chiffrement, TD protocoles, TP échange simulé, fiche limites.
- TD : distinguer confidentialité, authentification, intégrité et échange de clé.
- TP : simuler chiffrement symétrique et principe de clé publique sans données sensibles.
- Évaluation : étude de protocole.
- Sujet pratique : analyser un scénario HTTPS simplifié.
- Projet : rédiger la partie sécurité et RGPD du projet.
- Différenciation : schémas étapes ; extension sur attaque homme-du-milieu.
- Ressources Drive candidates : activités sécurité, supports HTTPS.
- Lien bac écrit : expliquer rôles des clés.
- Lien bac pratique : manipuler un exemple pédagogique.
- Lien Grand Oral : discuter confiance et sécurité.

## T14 - Langages : modularité, API, paradigmes, bugs

- Mois : avril-mai.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-LANG-03, T-LANG-04, T-LANG-05.
- Documents à produire : cours modularité, fiche API, TD paradigmes, TP revue de code.
- TD : découper un programme, repérer dépendances et sources de bugs.
- TP : refactorer un module et écrire tests de non-régression.
- Évaluation : revue de code structurée.
- Sujet pratique : corriger un bug localisé.
- Projet : stabiliser le code du projet final.
- Différenciation : grille de revue simplifiée ; extension sur comparaison de paradigmes.
- Ressources Drive candidates : projets anciens, scripts à corriger.
- Lien bac écrit : analyser modularité et bugs.
- Lien bac pratique : corriger et tester.
- Lien Grand Oral : expliquer une décision d'architecture logicielle.

## T15 - Calculabilité, programme comme donnée, arrêt

- Mois : mai.
- Volume horaire : 8 h, dont 1 h de projet.
- Capacités officielles : T-LANG-01.
- Documents à produire : cours culture scientifique, TD raisonnement, fiche limites du calcul.
- TD : distinguer problème, programme, entrée, terminaison et décidabilité.
- TP : activité débranchée ou pseudo-code, sans exiger de preuve formelle hors programme.
- Évaluation : questions argumentées.
- Sujet pratique : aucun sujet lourd ; période sensible.
- Projet : préparer une capsule orale sur limites du calcul.
- Différenciation : exemples concrets ; extension clairement marquée approfondissement.
- Ressources Drive candidates : supports culture informatique, débats.
- Lien bac écrit : formuler une réponse argumentée.
- Lien bac pratique : lien indirect via raisonnement sur terminaison.
- Lien Grand Oral : thème possible sur calculabilité et limites.

## T16 - Diviser pour régner, tri fusion

- Mois : mai.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-ALGO-03.
- Documents à produire : cours diviser pour régner, TD tri fusion, TP implémentation, fiche complexité.
- TD : décomposer un problème et recomposer une solution.
- TP : coder tri fusion avec tests et traces.
- Évaluation : devoir algorithmique.
- Sujet pratique : tri fusion ou découpage récursif guidé.
- Projet : identifier une sous-partie décomposable.
- Différenciation : pseudo-code fourni ; extension sur complexité en n log n.
- Ressources Drive candidates : exercices tri fusion, scripts récursifs.
- Lien bac écrit : justifier un schéma diviser pour régner.
- Lien bac pratique : coder une fonction récursive de tri.
- Lien Grand Oral : expliquer une stratégie algorithmique.

## T17 - Programmation dynamique

- Mois : mai-juin.
- Volume horaire : 10 h, dont 3 h de projet.
- Capacités officielles : T-ALGO-04.
- Documents à produire : cours mémoïsation/tabulation, TD problèmes guidés, TP optimisation.
- TD : reconnaître sous-problèmes recouvrants et relation de récurrence simple.
- TP : transformer une solution récursive coûteuse en solution mémoïsée.
- Évaluation : problème guidé.
- Sujet pratique : calcul optimisé avec dictionnaire ou tableau.
- Projet : optimisation limitée si elle répond à un besoin réel.
- Différenciation : table préremplie ; extension sur comparaison mémoire/temps.
- Ressources Drive candidates : exercices mémoïsation, problèmes classiques.
- Lien bac écrit : expliquer une table de calcul.
- Lien bac pratique : programmer une version mémoïsée simple.
- Lien Grand Oral : discuter compromis temps-mémoire.

## T18 - Boyer-Moore

- Mois : juin.
- Volume horaire : 8 h, dont 2 h de projet.
- Capacités officielles : T-ALGO-05.
- Documents à produire : cours recherche textuelle, TD tables de décalage, TP recherche de motif.
- TD : appliquer les décalages sur exemples courts.
- TP : implémenter une version pédagogique limitée et testée.
- Évaluation : analyse d'algorithme.
- Sujet pratique : recherche de motif dans chaîne.
- Projet : utiliser recherche textuelle sur données fictives.
- Différenciation : alphabet réduit ; extension sur variantes de Boyer-Moore.
- Ressources Drive candidates : exercices chaînes, scripts recherche.
- Lien bac écrit : tracer l'algorithme.
- Lien bac pratique : coder une recherche de motif simplifiée.
- Lien Grand Oral : expliquer pourquoi certains algorithmes gagnent du temps.

## T19 - Bac écrit, pratique, Grand Oral, projet final

- Mois : juin.
- Volume horaire : 18 h, dont 12 h de projet.
- Capacités officielles : synthèse de T-HIST-01 à T-ALGO-05.
- Documents à produire : planning révisions, banque sujets pratiques, grille Grand Oral, dossier projet final.
- TD : sujets écrits courts couvrant structures, bases, systèmes, réseaux, langages et algorithmes.
- TP : entraînements sujets pratiques en temps contraint.
- Évaluation : entraînements écrits et pratiques ; soutenance de projet.
- Sujet pratique : deux sessions blanches avec grille explicite.
- Projet : finalisation, démonstration, soutenance, bilan individuel.
- Différenciation : choix de sujets gradués ; extension sur amélioration technique du projet.
- Ressources Drive candidates : sujets pratiques, évaluations, anciens projets.
- Lien bac écrit : consolidation de toutes les rubriques.
- Lien bac pratique : entraînement direct aux sujets.
- Lien Grand Oral : problématique, plan, démonstration et recul critique.

## Points de vigilance annuels

- T-ALGO-02 n'est pas porté par la séquence pilote seule : il est planifié en T08 et doit rester `partial` tant que les documents dédiés ne sont pas relus.
- T-ALGO-01 n'est pas associé à la séquence pilote structures : il est réservé aux arbres et ABR.
- ABR est déplacé en T06 ; dans la séquence pilote, il doit rester un aperçu non évalué.
- BFS/DFS sont conservés comme application de graphes dans T08, pas comme point de départ de l'année.
- Les périodes Ramadan et Aïd allègent les évaluations lourdes ; SQL est fractionné et accompagné.
- La préparation bac écrit, pratique et Grand Oral est continue mais concentrée en T19.

## Capacités officielles planifiées

T-HIST-01, T-STRUCT-01, T-STRUCT-02, T-STRUCT-03, T-STRUCT-04, T-STRUCT-05, T-BDD-01, T-BDD-02, T-BDD-03, T-ARCH-01, T-ARCH-02, T-ARCH-03, T-ARCH-04, T-LANG-01, T-LANG-02, T-LANG-03, T-LANG-04, T-LANG-05, T-ALGO-01, T-ALGO-02, T-ALGO-03, T-ALGO-04, T-ALGO-05.

---
title: "T13 - TD - chiffrement HTTPS"
level: "terminale"
sequence_id: "T13"
document_type: "td"
status: "needs_review"
version: "0.3.0"
source: "BO 2019"
source_creation: "generated_from_program"
theme: "Sécurité"
notion: "chiffrement HTTPS"
objectifs:
  - "travailler chiffrement HTTPS sur des données explicites"
  - "produire une réponse justifiée et contrôlée"
  - "identifier les cas limites"
  - "corriger les erreurs fréquentes du chapitre"
private_data: false
official_program:
  capacities:
    - "T-ARCH-04A"
    - "T-ARCH-04B"
---

# T13 - TD - chiffrement HTTPS

## Objectifs
- Lire une donnée disciplinaire précise avant de répondre.
- Produire une méthode vérifiable et un résultat contrôlable.
- Traiter un cas limite sans le transformer en généralité.
- Relier chaque correction à une erreur fréquente observable.

## Capacités officielles
- T-ARCH-04A
- T-ARCH-04B

## Fiche liée et séance liée
- Fiche liée : `03_progressions/fiches_cours/terminale/T13/T13_fiche_cours_chiffrement_https.md`.
- Séance liée : `T13-S1` dans la progression annuelle.
- Statut : support `needs_review`, non validé et non publiable.

## Situation de travail
Un navigateur établit une connexion HTTPS avec serveur.example.

## Progression socle / standard / approfondissement
- Socle : exercices 1 et 2, lecture guidée de la donnée.
- Standard : exercices 3 à 6, production écrite et justification.
- Approfondissement : exercices 7 et 8, transfert ou comparaison.

## Exercices
### Exercice 1 - Distinguer chiffrement symétrique/asymétrique
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-04A.
- Données : Clé publique serveur Kpub, clé privée Kpriv, clé de session Ks.
- Consigne : Associer les rôles.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 2 - Lire un certificat
- Type : lecture/analyse.
- Niveau : socle.
- Capacité officielle : T-ARCH-04B.
- Données : Certificat: sujet serveur.example, émetteur CA-NSI, validité 2026-01-01 à 2027-01-01.
- Consigne : Dire ce qui est vérifié.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 3 - Dérouler un handshake simplifié
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-04A.
- Données : Client propose suites ; serveur envoie certificat ; secret de session établi.
- Consigne : Écrire les étapes.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 4 - Calculer un haché jouet
- Type : production/écriture.
- Niveau : standard.
- Capacité officielle : T-ARCH-04B.
- Données : h(m)=somme codes ASCII mod 10, message "AB".
- Consigne : Calculer h.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 5 - Certificat expiré
- Type : cas limite.
- Niveau : standard.
- Capacité officielle : T-ARCH-04A.
- Données : Date du jour 2028-03-01, certificat valable jusqu’à 2027-01-01.
- Consigne : Dire la décision.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 6 - Justifier HTTPS contre écoute
- Type : justification.
- Niveau : standard.
- Capacité officielle : T-ARCH-04B.
- Données : Un attaquant lit le trafic Wi-Fi.
- Consigne : Expliquer ce qui reste visible.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 7 - Identifier attaque homme du milieu
- Type : lecture/analyse.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-04A.
- Données : Certificat présenté: sujet serveur.example, émetteur inconnu LocalProxy.
- Consigne : Conclure.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.
### Exercice 8 - Écrire une politique de mot de passe
- Type : production/écriture.
- Niveau : approfondissement.
- Capacité officielle : T-ARCH-04B.
- Données : Service interne NSI.
- Consigne : Donner trois règles justifiées.
- Production attendue : fournir la valeur, la trace, la table, la requête ou le pseudo-code demandé par l’exercice.
- Critère de réussite : le résultat se contrôle avec la valeur, la trace, la table, la requête ou le pseudo-code produit.

## Corrigé
### Corrigé exercice 1
- Capacité mobilisée : T-ARCH-04A.
- Donnée utilisée : Clé publique serveur Kpub, clé privée Kpriv, clé de session Ks.
- Résultat attendu : Kpub/Kpriv servent à authentifier/établir le secret ; Ks sert ensuite au chiffrement symétrique rapide des données.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 2
- Capacité mobilisée : T-ARCH-04B.
- Donnée utilisée : Certificat: sujet serveur.example, émetteur CA-NSI, validité 2026-01-01 à 2027-01-01.
- Résultat attendu : Le navigateur vérifie le nom serveur.example, la période de validité et la signature par une autorité de confiance CA-NSI.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 3
- Capacité mobilisée : T-ARCH-04A.
- Donnée utilisée : Client propose suites ; serveur envoie certificat ; secret de session établi.
- Résultat attendu : 1 ClientHello ; 2 ServerHello+certificat ; 3 vérification certificat ; 4 établissement Ks ; 5 données chiffrées avec Ks.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 4
- Capacité mobilisée : T-ARCH-04B.
- Donnée utilisée : h(m)=somme codes ASCII mod 10, message "AB".
- Résultat attendu : ASCII A=65, B=66, somme=131, 131 mod 10 = 1. Ce haché jouet n’est pas cryptographiquement sûr.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 5
- Capacité mobilisée : T-ARCH-04A.
- Donnée utilisée : Date du jour 2028-03-01, certificat valable jusqu’à 2027-01-01.
- Résultat attendu : Le navigateur doit refuser ou afficher une alerte forte : la validité temporelle est dépassée.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 6
- Capacité mobilisée : T-ARCH-04B.
- Donnée utilisée : Un attaquant lit le trafic Wi-Fi.
- Résultat attendu : L’attaquant peut voir l’adresse IP et le domaine selon contexte, mais pas le contenu HTTP chiffré par la clé de session.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 7
- Capacité mobilisée : T-ARCH-04A.
- Donnée utilisée : Certificat présenté: sujet serveur.example, émetteur inconnu LocalProxy.
- Résultat attendu : Si LocalProxy n’est pas une autorité approuvée, la chaîne de confiance échoue : risque de MITM.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.
### Corrigé exercice 8
- Capacité mobilisée : T-ARCH-04B.
- Donnée utilisée : Service interne NSI.
- Résultat attendu : Longueur minimale 12, interdiction mots de passe connus, hachage salé côté serveur. Ces règles limitent brute force et fuite de base.
- Contrôle : reprendre la valeur, la trace, la table, la requête ou le pseudo-code de l’énoncé et expliciter le cas limite si l’exercice le demande.

## Erreurs fréquentes
- EF1 : répondre par un mot-clé sans citer la donnée ; remédiation : entourer les valeurs utiles avant de rédiger.
- EF2 : donner un résultat sans méthode ; remédiation : imposer une ligne méthode puis une ligne résultat.
- EF3 : oublier le cas limite ; remédiation : refaire l’exercice 5 avec la donnée minimale.
- EF4 : confondre justification et paraphrase ; remédiation : écrire une phrase qui relie donnée, règle et conclusion.

## Remédiation ciblée
- Reprendre deux exercices en ne gardant que les données numériques ou symboliques.
- Faire corriger une réponse incomplète par un binôme avec une grille donnée/méthode/résultat/contrôle.
- Produire une variante courte avec une donnée changée et vérifier que la méthode reste valable.

## Différenciation
- Socle : fournir les données annotées et demander seulement le résultat contrôlé.
- Standard : demander méthode complète, résultat et contrôle écrit.
- Approfondissement : demander une variante de la donnée et une comparaison de deux démarches.

## Lien avec la progression
| Élément | Référence | Statut |
|---|---|---|
| Fiche | T13_fiche_cours_chiffrement_https.md | needs_review |
| Séance | T13-S1 | progression existante |
| Évaluation | T13_evaluation_chiffrement_https.md | needs_review |

## Source et traçabilité
- Recherche locale effectuée dans le dossier Documents_DRIVE avant création.
- Aucun fichier Drive n’a été repris directement dans ce support.
- Source de création : programme officiel et progression locale, avec statut `needs_review`.

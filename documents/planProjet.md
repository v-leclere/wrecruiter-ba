# Analyse fonctionnelle et définition des objectifs

## Besoin et fonctionnalités
L'entreprise vend à ses clients tout un panel d'outils permettant de gérer avec précision ses actifs.
Afin de leur permettre de calculer ces actifs, nous avons décidé de mettre en place une calculatrice.
Cette calculatrice doit offrir un usage simple et non ambigu des opérations de calculs arithmétiques, aussi la notation polonaise inversée a été retenue.
L'outil doit pouvoir réaliser correctement tout type de calcul arithmétique de base et donner la possibilité à son utilisateur de consulter l'historique des calculs passés à tout moment.

## Livrables
A l'issue de la phase de développement, il est attendu que l'outil soit livré avec son fichier de déploiement, une documentation d'API et, dans la mesure du possible, des tests automatisés de non régression (fonctionnels et/ou unitaires).

## Planification du projet
L'attente autour de cet outil étant grande, le projet doit avoir été livré après recette le mardi 9 avril à 10 heures au plus tard pour respecter le cycle de déploiement hebdomadaire de notre application.

# Conception

## Architecture
L'outil sera décomposé en deux éléments : une API backend qui réalise les calculs et un front web qui sert d'interface utilisateur.

## Spécifications techniques

### Saisie d'un calcul
Une route API doit permettre de saisir une fonction arithmétique au format NPI, l'interpréter et renvoyer comme message de réponse le résultat de la fonction.
Du fait de tenir un historique des opérations, cette route utilisera le verbe POST et non PUT (envoyer deux fois le même calcul doit générer deux entrées dans l'historique).

### Récupération de l'historique de calcul
Une route API doit permettre de télécharger au format CSV la liste des opérations passées et les résultats de ces opérations.

# Développement

## Développement itératif
L'organisation du projet se fera sous forme d'un sprint du 5 au 9 avril.
Durant ce sprint, le développement se fera en respectant les normes de programmation et les bonnes pratiques adéquates.

## Tests et recette
À l'issue de chaque développement, des tests unitaires et/ou fonctionnels sanctionneront chaque évolution de la base de code et s'assurera de sa stabilité et de son bon fonctionnement.
À la fin de la phase de développement, une recette aura lieu afin de vérifier que tous les tests d'acceptation sont passés avec succès.

# Livraison

## Documentation
Une documentation de l'outil et de son API terme est souhaitable et souhaitée.
Une documentation de mise en œuvre afin de déployer l'outil au sein de l'existant doit être écrite.

## Déploiement
Le déploiement de l'outil se fera en tant compte des obligations opérationnelles de nos clients : elle aura lieu lors des opérations planifiées de déploiement hebdomadaires.

## Formation
Une communication sur le déploiement de cet outil se fera dans un second temps, en plus de proposer une éventuelle formation des utilisateurs finaux à cette calculatrice.

# Maintenance

## Support technique
Les demandes de nos clients se feront par les canaux de support technique habituels (ticketing, etc)
Un suivi de la montée en compétence de nos clients sur cet outil se fera via ce support afin de s'assurer du bon usage de la calculatrice.

## Evolution de l'outil
Il est attendu que le support technique rapporte tout problème technique rencontré par nos clients afin d'engager des opérations de maintenance évolutive.

# Gestion de projet

## Suivi et reporting
Du fait du temps relativement court alloué à ce projet et de l'envergure limitée à ce dernier, il n'est pas prévu d'effectuer un suivi régulier de l'avancement ni des dépenses engagées.
Un rapport sur l'adoption de l'outil est envisagé une fois de déploiement effectué pour jauger de la pertinence des nouvelles fonctionnalités apportées.

## Amélioration continue
L'équipe de développement pourra prendre en charge les évolutions fonctionnelles et les correctifs tels que remontés par le support technique dans le cadre du temps hebdomadaire alloué aux opérations de maintenance.
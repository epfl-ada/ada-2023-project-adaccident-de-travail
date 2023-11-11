# ADA

## Todo refaire les RQ

Global RQ: what makes a movie have a sequel? (first part) (on s'intéresse aux films orignaux et on fait tout le dataset)
Global RQ: How do sequels differ from their original films? (second part)
Global RQ: what makes a good sequel? (Third part)

Research : 
RQ1: Are sequels or prequels as much popular as the original film? (popular in the sense of grossings)
RQ2: Do the cast usually change greatly?
RQ3: Do genre vary greatly between sequels and original?
RQ4: Do storylines change between original and sequels?
RQ5: Do critics reviews or consumer matter more in succes?


# Part 1
On compare les films qui ont une sequels par rapport à ceux qui n'en ont pas et aussi par rapport à tous les films
**Trois datasets : Tous les films, films avec sequel, films sans sequel**
- Stats sur revenus
  - Revenus moyen/median par film sans sequel vs avec sequel vs tous les films
- Durée
  - Durée moyen/median par film sans sequel vs avec sequel vs tous les films
- Mois de sortie
  - Répartition par mois avec vs sans vs tous les films
- Année de sortie
  - Ratio films avec sequel (orginaux) / tout films par année
  - Ratio sequel / tous films par année
- (Langues)
- Pays d'origine
  - Réparition par pays films sans sequel vs avec vs tous les films
- Genre du film
  - On prend les n genre les plus fréquents (style 20)
  - On prend les deux main genres par films pour tous les films
  - On fait une heatmap entre les deux genres pour tous les films
  - On fait une heatmap entre les deux genres pour les films avec sequel
  - On fait une heatmap entre les duex genres pour les films sans sequel
  - On compare ensuite si la paire de genres la plus populaire est aussi celle la plus populaire dans les films qui ont une sequel
    - Par ex: (Action/Adventure) est très fréquent pour tous les films, (Romance/Action) pas du tout
    - Mais (Romance/Action) est très populaire pour les films avec suite
- Types de personnages
	- Age
      	- Médiane des âges de acteurs pour les trois datasets
      	- Binning par tranche d'âge (Genre [35;45[)
	- Genre
    	- Ratio par film M/F pour les trois datasets
# Part 2 (sur les suites)
On compare les films originaux par rapport à leur suite
Dataset : paire de films (original; suite), toutes les suites, tous les orginaux
Problème : les sagas seront plus représentées dans le dataset
Exemple : 
	(Harry Potter 1; Harry Potter 2), (Harry Potter 2; Harry Potter 3), ..., (Harry Potter 6; Harry Potter 7) vs (Kill Bill 1, Kill Bill 2)
	Harry Potter a 6 fois plus de poids que Kill Bill
	Mais ça semble assez rare d'avoir plus qu'une sequel.

- Stats sur revenus
  - Revenus tous originaux vs tous suite - médiane par année
  - Ratio revenu sequel / original par paire. CDF ? Binning ?
- Durée
  - Durée tous originaux vs tous suite - médiane ou moyenne ?
  - Ration durée sequel / original par paire. CDF ? Binning ?
- Mois de sortie
  - Histogramme par mois de originaux vs suites
- Année de sortie
  - Au bout de combien de temps un sequel sort. Durée en mois ou semaines entre la sortie de l'original et la sequel.
- (Langues)
- (Pays d'origine)
- Genre du film
  - Heatmap entre les genres représentés dans tous les originaux et les suites (cf. P1)
  - Comparaison de l'évolution des genres entre un film original et sa suite. (Probablement que ça va pas changer mais bien de le montrer)
    - Distance entre les genres orignal vs suite
- Types de personnages
  - Distance entre original vs suite, quelle proportion du cast revient ?
	- Age
    	- Médiane suite vs original (cf. P1)
    	- à discuter. soustraire le temps passé entre les deux films ?
	- Genre
    	- Ratio M/F tous suite vs tous original
    	- Évolution par paire
- Changement du scénario
  - Similarité sysnopsis dans le sens -> peut-être thèmes ?
- Personnages récurrents
  - Par paire ratio persos qui reviennent

# Part 3
On compare les sequels entre eux (y'a le bon sequel et le mauvais sequel)
Dataset : toutes les suites
à voir si c'est pertinent

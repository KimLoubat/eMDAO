query = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?constraint
WHERE {
    ?requirement bikeo:concerns ?constraint ;
                 rdf:type bikeo:Requirement .
    ?constraint rdf:type bikeo:Constraint .       
}
"""

# Exécuter la requête SPARQL
results = g.query(query)

# Afficher les résultats
print("Contrainte associée à l'exigence sur le roulement :")
for row in results:
    print(row)


query1 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?designVariable
WHERE {
    ?instance bikeo:hasElement ?designVariable ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?designVariable rdf:type bikeo:DesignVariable .  
}
"""

results1 = g.query(query1)

print("Variables de conception de la matrice XDSM :")
for row in results1:
    print(row)

query2 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?stateVariable
WHERE {
    ?instance bikeo:hasElement ?stateVariable ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?stateVariable rdf:type bikeo:State_Variable .  
}
"""

results2 = g.query(query2)

print("La variable d'état de la matrice XDSM:")
for row in results2:
    print(row)

query2 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?mdoMethod
WHERE {
    ?instance bikeo:hasElement ?mdoMethod ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?mdoMethod rdf:type bikeo:MDOMethod .  
}
"""

results2 = g.query(query2)

print("La méthode MDO de la matrice XDSM:")
for row in results2:
    print(row)

query3 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?discipline
WHERE {
    ?instance bikeo:hasElement ?discipline ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?discipline rdf:type bikeo:Discipline .  
}
"""

results3 = g.query(query3)

print("Les disciplines de la matrice XDSM:")
for row in results3:
    print(row)

query4 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?discipline ?disciplineOrder ?inputVariable
WHERE {
    ?instance bikeo:hasElement ?discipline ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?discipline rdf:type bikeo:Discipline ;       
                bikeo:hasInInput ?inputVariable ;
                rdfs:comment ?disciplineOrder .

} 
GROUP BY ?discipline ?inputVariable 
ORDER BY ASC(?disciplineOrder)
"""

results4 = g.query(query4)

print("Les variables en entrée de chaque discipline:")
for row in results4:
    print(row)

query5 = """
PREFIX bikeo: <http://purl.org/ontology/bikeo#> 
SELECT ?discipline ?disciplineOrder ?outputVariable
WHERE {
    ?instance bikeo:hasElement ?discipline ;
              rdfs:label "Bearing XDSM Matrix"@en .
    ?discipline rdf:type bikeo:Discipline ;       
                bikeo:hasInOutput ?outputVariable ;
                rdfs:comment ?disciplineOrder .
} GROUP BY ?discipline ?outputVariable
ORDER BY ASC(?disciplineOrder)
"""

results5 = g.query(query5)

print("Les variables en sortie de chaque discipline:")
for row in results5:
    print(row)

##########Pour afficher les sous-systèmes d'un système donné, par exemple le mbike :

query6 = ("""
PREFIX bikeo: <http://purl.org/ontology/bikeo#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?commonPartLabel
WHERE {
    ?system bikeo:hasPart ?commonPart ;
                rdfs:label "mbike"@en .
    ?commonPart rdf:type/rdfs:subClassOf* bikeo:CommonPart .   
    ?commonPart rdfs:label ?commonPartLabel .    
}
""")

results6 = g.query(query6)

listResults6 = []

for row in results6:
    elt = str(row[0]) #alternative : row["commonPartLabel"]
    listResults6.append(elt)

print(listResults6)
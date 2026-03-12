------------------------------------------------------------------------------------------------------------------------

# eMDAO Repository

eMDAO is an approach for integrating requirements into MDAO matrices during the design process.
It is based on the MARS ontology and the MainTrix tool.
This repository contains the first proof of concept for eMDAO using the Mbike use case.

------------------------------------------------------------------------------------------------------------------------

## Repository structure

```
.
├── Mbike/
│   └── mars.rdf            # RDF ontology file
│   └── script.py           # Python script executing SPARQL queries and loading MainTrix interface
│   └── requirements.txt    # Python dependencies
└── README.md
```

## Ontology

The ontology (`Mbike/mars.rdf`) defines the classes, properties, and relationships used to represent engineering requirements and MDAO matrices knowledge.

It can be opened with ontology editors such as Protégé or loaded into an RDF triple store for querying.

## SPARQL queries

The file `Mbike/script.py` contains example Python code demonstrating how to execute SPARQL queries over the MARS ontology.

The script uses `rdflib` to:

* load the ontology
* execute SPARQL queries
* print query results

## Installation

Clone the repository:

```bash
git clone https://github.com/username/example-ontology.git
cd example-ontology
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running the SPARQL queries

Execute the Python script:

```bash
python Mbike/script.py
```

The script will load the ontology and display the results of the defined SPARQL queries.

## License

All the content in this repository are under the Apache 2.0 license.


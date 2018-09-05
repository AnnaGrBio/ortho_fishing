# ortho_fishing

## Presentation

This programme is design to produce a list of orthologs of human genes in each of the 10 clupeocephala fishes present in Ensembl. 

In order to run, it requires:

* all the phylogenetic trees of human genes, available from Ensembl or Hugues Roest Crollius and Alexandra Louis
* the list of human genes to look for. It is ESSENTIAL that this list be named "human_genes"
* You need to install Biopython

Output

The programme generates 4 output files.

* The "genes_duplicate" file contains the list of requested human genes (under "human_genes") which have several orthologs (due to duplications) in the corresponding fish, as well as the codes of the orthologous genes in the fish.
* The "genes_singleton" file contains the list of requested genes (under "human_genes") which have a single ortholog in the corresponding fish, as well as the code of each ortholog.
* The "genes_without_fishes" file contains the list of human genes which were not found in teleost fishes, and appeared for the most part in tetrapods.
* The "genes_without_clupeocephala" file contains the list of genes which do not have an ortholog in the corresponding fish.


## Run ortho_fishing

1. Decompress the "human_phylogeny_2.7_modified" file and put all the resulting trees in the directory.

2. Insert the programme in the same directory, as well as the list "liste_finale".

It is essential that "human_genes" contain the Ensembl codes of the human genes whose orthologs in fishes are being looked for, each followed by a carriage return.
The enclosed "human_genes" contains the codes of all human genes. However, it is possible to run the programme with only one code.

3. Go to the working directory which contains all the files.

4. Run the programme using the code `python ortho_fishing.py`

5. The programme will ask for the path to the directory you are using. It must include the complete path, starting with /home/ and ending with the directory name.

6. The programme will then display 10 numbers which correspond to the 10 fishes present in the trees. Type in the number of the chosen fish.
















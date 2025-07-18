# ARTEM-KT

Applying [ARTEM](https://github.com/david-bogdan-r/ARTEM) to RNA tertiary motif search using kink-turns as an example.

## Reference

[E.F. Baulin, D.R. Bohdan, D. Kowalski, M. Serwatka, J. Świerczyńska, Z. Żyra, J.M. Bujnicki, (2024) ARTEM: a method for RNA tertiary motif identification with backbone permutations, and its example application to kink-turn-like motifs. bioRxiv. DOI: 10.1101/2024.05.31.596898](https://doi.org/10.1101/2024.05.31.596898)

## Check out [our other developments](https://github.com/febos/wiki)

## Content 

### cif

Kink-turns and isosteric motifs in mmCIF format

### figures

Source figure files

### introns

The seven representative group II intron structures in mmCIF format

### othermotifs

Data on the G4, GNRA-tetraloop, i-motif, and parallel-pairing motif

### refmotifs

Two reference motifs - a Kt7 kink-turn and a k-junction, in mmCIF format

### sto_logo

Source files on the ribosomal k-junction conservation analysis

### files

- **REPRODUCE.md** - The steps to reproduce the results
- **TableS1.xlsx** - Supplementary Table S1, 26,564 kink-turn matches obtained with ARTEM 
- **TableS2.xlsx** - Supplementary Table S2, 780 kink-turn matches used for benchmarking
- **TableS4.xlsx** - Supplementary Table S4, source benchmarking data for group II introns
- **1ffk_hits.tsv** - 11,025 kink-turn matches obtained with ARTEM against module #1
- **3d2g_hits.tsv** - 18,727 kink-turn matches obtained with ARTEM against module #2
- **annotated_hits.tsv** - 26,564 kink-turn hits obtained with ARTEM and annotated with urslib2, source file for Supplementary Table S1
- **kt7_13res_template.pdb** - 13-residue kink-turn template used for benchmarking
- **nrlist_3.312_4.0A.csv** - [Representative set of RNA structures](http://rna.bgsu.edu/rna3dhub/nrlist/release/3.312)
- **pdb_download.py** - Python script that downloads RNA-containing PDB entries
- **post-processing.ipynb** - Post-processing Jupyter Notebook
- **unique_hits.py** - Python script for merging 1ffk_hits.tsv & 3d2g_hits.tsv
- **unique_hits.tsv** - 26,564 kink-turn hits obtained with ARTEM, input for urslib2 annotation




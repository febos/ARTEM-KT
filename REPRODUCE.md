

## PDB search

Prepare ARTEM

 - "git clone https://github.com/david-bogdan-r/ARTEM"

Prepare a search database

 - "mkdir PDB"
 - "pip install requests"
 - "python3 pdb_download.py" (for DNA structures comment lines 5-6 and uncomment lines 7-8)
 
Run ARTEM

 - "python3 ARTEM/artem.py r=./PDB/*.cif q=refmotifs/1ffk_0_kt7.cif rres=#1 qres=":_77_82 :_92_94 :_97_100" sizemin=12 rmsdmax=2.0 rnosub=1 qrst=":_79_81 :_93_94 :_97_98" silent=True > 1ffk_hits.tsv"
 
 - "python3 ARTEM/artem.py r=./PDB/*.cif q=refmotifs/3d2g_A_kj.cif rres=#1 qres=":_8_10 :_36_38 :_42 :_44_46 :_69_72" sizemin=12 rmsdmax=2.0 rnosub=1 qrst=":_9 :_37_38 :_42 :_44 :_71_72" silent=True > 3d2g_hits.tsv"

Merge identical hits between the motifs

 - "python3 unique_hits.py"
 
Prepare urslib2
 
 - "git clone https://github.com/febos/urslib2"
 
 - "mv urslib2 urslib2_repo"
 
 - "ln -s urslib2_repo/urslib2 urslib2"
 
 - set the path to DSSR in urslib2/config.py

Annotate hits

 - see post-processing.ipynb

## group II introns

 - "python ARTEM/artem.py q=refmotifs/1ffk_0_kt7.cif qres=":_77_82 :_92_94 :_97_100" sizemin=12 r=introns/ silent=True" 
 
 - "python ARTEM/artem.py q=refmotifs/1ffk_0_kt7.cif qres=":_77_82 :_92_94 :_97_100" sizemin=11 r=introns/ silent=True"
 
## other motifs

G4 search in RNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDB/*.cif q=othermotifs/8d79_parallel_G4.pdb rres=#1 sizemin=4 rmsdmax=2 silent=True > othermotifs/G4_RNA_hits.tsv"
 
G4 search in DNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDBDNA/*.cif q=othermotifs/8d79_parallel_G4.pdb rres=#1 sizemin=4 rmsdmax=2 silent=True > othermotifs/G4_DNA_hits.tsv"
 
GNRA search in RNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDB/*.cif q=othermotifs/3sux_GNRA.pdb rres=#1 sizemin=6 silent=True qrst="/X:_65_70 |strand|" > othermotifs/GNRA_RNA_hits.tsv"
 
GNRA search in DNA-containing PDB entries
 
 - "python3 ARTEM/artem.py r=./PDBDNA/*.cif q=othermotifs/3sux_GNRA.pdb rres=#1 sizemin=6 silent=True qrst="/X:_65_70 |strand|" > othermotifs/GNRA_DNA_hits.tsv"
 
i-motif search in RNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDB/*.cif q=othermotifs/1i9k_imotif.pdb rres=#1 sizemin=8 silent=True > othermotifs/imotif_RNA_hits.tsv"

i-motif search in DNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDBDNA/*.cif q=othermotifs/1i9k_imotif.pdb rres=#1 sizemin=8 silent=True > othermotifs/imotif_DNA_hits.tsv"
 
Parallel-pairing motif search in RNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDB/*.cif q=othermotifs/8sh5_parallelpairing.pdb rres=#1 sizemin=8 silent=True  > othermotifs/parallelpairing_RNA_hits.tsv"

Parallel-pairing motif search in DNA-containing PDB entries

 - "python3 ARTEM/artem.py r=./PDBDNA/*.cif q=othermotifs/8sh5_parallelpairing.pdb rres=#1 sizemin=8 silent=True  > othermotifs/parallelpairing_DNA_hits.tsv"
 
 
 
 

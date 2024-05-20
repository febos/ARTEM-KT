import os

hits = ["1ffk_hits.tsv",
        "3d2g_hits.tsv"]

outp = open("unique_hits.tsv","w")


outp.write("\t".join(['ID','SIZE','RMSD','RMSDSIZE',
                      'RESRMSD','PRIM','SCND','REF','QRY'])+'\n')

hitdict = {} # PDB: frozenset: [rmsd, size, ref, line]

for file in hits:
    with open(file) as inp:
        lines = inp.readlines()
        for line in lines[1:]:
            linesplit = line.strip().split()
            rmsd = float(linesplit[2])
            size = int(linesplit[1])
            ref = linesplit[-1]
            pdb = os.path.basename(linesplit[-2])[:4]
            if pdb not in hitdict:
                hitdict[pdb] = {}
            hit = frozenset([x.split('=')[0]
                             for x in linesplit[-3].split(',')])
            issub = False
            for prev in sorted(hitdict[pdb].keys()):
                if prev < hit:
                    hitdict[pdb].pop(prev)
                elif hit < prev:
                    issub = True
                    break
            if issub:
                continue
            if hit not in hitdict[pdb] or\
               rmsd < hitdict[pdb][hit][0]:
                hitdict[pdb][hit] = [rmsd, size, ref, line]

for pdb in sorted(hitdict.keys()):
    for hit in sorted(hitdict[pdb].values(), key = lambda x: (x[2],x[1],-x[0])):
        outp.write(hit[3])

outp.close()



import os, glob

overlapthresh = 0.8

nr = {}
with open('nrlist_3.312_4.0A.csv') as inp:
    for line in inp:
        if line.startswith("CLASS") or not line:
            continue
        ls = line.strip().split('","')[1].split('+')
        for ent in ls:
            ents = ent.split('|')
            pdb, ch = ents[0], ents[2]
            if pdb not in nr:
                nr[pdb] = set()
            nr[pdb].add(ch)

print(len(nr),sum(len(nr[x]) for x in nr))
        
artem = []
unique = []

for file in ('annotated_hits.tsv',):
    with open(file) as inp:
        lines = inp.readlines()
        for line in lines[1:]:
            linesplit = line.strip().split('\t')
            rmsd = float(linesplit[4])
            size = int(linesplit[3])
            pdb = linesplit[0][:4]
            hit = frozenset(['1.'+x for x in linesplit[5:19] if x.strip()])
            chs = {x.split('.')[1] for x in hit}
            desc = linesplit[-3]+(',J'+linesplit[-4] if linesplit[-4].strip() else '')
            if linesplit[-2] == 'YES':
                desc += ',kink'

            if pdb in nr and (chs & nr[pdb]):

                ch = chs
                artem.append([pdb,ch,rmsd,size,'artem',desc,hit])

                new = True
                for k,uniq in enumerate(unique):
                    if uniq[0] != pdb or not (uniq[1] & ch):
                        continue
                    hit2 = uniq[-1]
                    if (len(hit2 & hit) / min(len(hit2),len(hit))) >= overlapthresh:
                        new = False
                        if size > uniq[3] or (size == uniq[3] and rmsd < uniq[2]):
                            unique[k] = [pdb,ch,rmsd,size,'artem',desc,hit]
                        break
                if new:
                    unique.append([pdb,ch,rmsd,size,'artem',desc,hit])
       
print(len(artem),len(unique),len([1 for x in unique if x[-2]=='LC,kink']))

artem = unique
dssr = []

for pdb in nr:
    dssrpath = "DSSR/{}.out1".format(pdb)
    if not os.path.exists(dssrpath):
        continue
    with open("DSSR/{}.out1".format(pdb)) as inp:
        lines = inp.readlines()
        for k,line in enumerate(lines):
            if "Normal k-turn" in line:
                s1 = set(lines[k+2].strip().split()[3].replace('..','.').split(','))
                s2 = set(lines[k+3].strip().split()[3].replace('..','.').split(','))
                ch = {x.split('.')[1] for x in s1} | {x.split('.')[1] for x in s2}
                hit = frozenset(s1 | s2)
                if ch & nr[pdb]:
                    dssr.append([pdb,ch,'dssr',hit])


print(len(dssr))

cnt = 0
for k1,ent in enumerate(artem):
    matched = False

    pdb, ch, hit = ent[0], ent[1], ent[-1]

    for k2, ent2 in enumerate(dssr):
        if ent2[0] != pdb or not (ent2[1] & ch):
            continue
        hit2 = ent2[-1]
        if len(hit2 & hit) / len(hit) >= overlapthresh:
            artem[k1][-3] += ',dssr'
            dssr[k2][-2] += ',artem'
            break

for i in range(len(dssr)):
    pdb, ch, tools, hit = dssr[i]
    if 'artem' not in tools:
        artem.append([pdb,ch,0,0,tools,'',hit])

print(len(artem))

rmsxpdbs = set()
rmsxfiles = sorted(glob.glob("RNAMotifScanX/knk/*.knk"))
rmsx = []

for file in rmsxfiles:

    pdb = os.path.basename(file)[:4]
    if pdb not in nr:
        continue
    rmsxpdbs.add(pdb)
    with open(file) as inp:
        lines = inp.readlines()
        for line in lines[1:]:
            if line.strip():
                rmsx.append(line.strip())

print(len(rmsxpdbs))

for x in rmsx:
    print(x)

'''from collections import Counter

a = Counter([x[-3] for x in artem if x[-2] in ('','LC,kink')])
print(a)

for x in artem:
    if x[0] in rmsxpdbs:
        print(x)'''

for i in range(len(artem)):

    if artem[i][0] in rmsxpdbs:
        artem[i].append(3)
    else:
        artem[i].append(2)

    if ',' in artem[i][4] and 'artem' in artem[i][4]:
        artem[i].append("TRUE")
    else:
        artem[i].append("")

with open("KinkTurnBench2.csv","w") as outp:
    outp.write('\t'.join([str(x) for x in ["PDB","CHAINS","ARTEM_RMSD","ARTEM_SIZE",
                                           "IDENTIFIED_BY","TYPE","BENCHMARK_NO","TRUE_FALSE","RESIDUES"]])+'\n')

    for x in sorted(artem, key = lambda y: (y[4],y[5],y[0],y[1],int(sorted(y[-3])[0].split('.')[3]))):
        outp.write('\t'.join([str(x) for x in [x[0],','.join(sorted(x[1])),x[2],
                                               x[3],x[4],x[5],
                                               x[7],x[8],
                                               ','.join(sorted(x[6],key = lambda y: (y.split('.')[1],int(y.split('.')[3])))),
                                               ]])+'\n')


#[pdb,ch,rmsd,size,'artem',desc,hit]









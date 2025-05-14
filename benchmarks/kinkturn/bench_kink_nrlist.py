

import os

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

                ch = sorted(chs & nr[pdb])[0]
                artem.append([pdb,ch,rmsd,size,desc,hit])

                new = True
                for k,uniq in enumerate(unique):
                    if uniq[0] != pdb or uniq[1] != ch:
                        continue
                    hit2 = uniq[-1]
                    if (len(hit2 & hit) / min(len(hit2),len(hit))) >= overlapthresh:
                        new = False
                        if size > uniq[3] or (size == uniq[3] and rmsd < uniq[2]):
                            unique[k] = [pdb,ch,rmsd,size,desc,hit]
                        break
                if new:
                    unique.append([pdb,ch,rmsd,size,desc,hit])
       
print(len(artem),len(unique))

artem = unique
dssr = []

for pdb in nr:
    dssrpath = "DSSR/{}.out1".format(pdb)
    if not os.path.exists(dssrpath):
        continue
    
    with open("DSSR/{}.out1".format(pdb)) as inp:
        lines = inp.readlines()

        for k,line in enumerate(lines):
            if "Normal k-turn;" in line:
                s1 = set(lines[k+2].strip().split()[3].replace('..','.').split(','))
                s2 = set(lines[k+3].strip().split()[3].replace('..','.').split(','))
                ch = sorted(s1)[0].split('.')[1]
                hit = frozenset(s1 | s2)
                if ch in nr[pdb]:
                    dssr.append([pdb,ch,hit])

cnt = 0
print(len(dssr))
for ent in dssr:

    matched = False

    pdb, ch, hit = ent

    for ent2 in artem:
        if ent2[0] != pdb or ent2[1] != ch:
            continue
        hit2 = ent2[-1]
        if len(hit2 & hit) / len(hit2) >= overlapthresh:
            print(len(hit2 & hit),len(hit2))
            #print(hit)
            #print(hit2)
            cnt += 1
            matched = True
            break

    if not matched:
        #print()
        #print(pdb,ch,sorted(hit,key = lambda x: int(x.split('.')[3])))
        #print()
        pass
        
print(cnt)

cnt = 0
for ent in artem:
    matched = False

    pdb, ch, hit = ent[0], ent[1], ent[-1]

    for ent2 in dssr:
        if pdb == '5G4U':
            print(hit)
            print(hit2)
            print(hit2 & hit)
        if ent2[0] != pdb or ent2[1] != ch:
            continue
        
        hit2 = ent2[-1]
        if len(hit2 & hit) / len(hit) >= overlapthresh:
            #print(len(hit2 & hit),len(hit2))
            #print(hit)
            #print(hit2)
            cnt += 1
            matched = True
            break

    #print(ent[-2],matched)

    if not matched and ent[-2]=='LC,kink':
        sorted_hit = sorted(hit,key = lambda x: int(x.split('.')[3]))
        #print(pdb,ch,sorted_hit)






























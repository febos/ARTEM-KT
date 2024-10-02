import os,requests,json,glob


date   = "2023-12-07"
folder = "./PDB"
mol    = "RNA"
#folder = "./PDBDNA"
#mol    = "DNA"

def DownloadPDB():

    empty = False
    start = 0
    rows  = 25

    while not empty:

        empty = True
        print(start)

        query = '%7B"query"%3A%7B"type"%3A"group"%2C"logical_operator"%3A"and"%2C"nodes"%3A%5B%7B"type"%3A"'+\
                'terminal"%2C"service"%3A"text"%2C"parameters"%3A%7B"attribute"%3A"entity_poly.rcsb_entity_polymer_type'+\
                '"%2C"operator"%3A"exact_match"%2C"negation"%3Afalse%2C"value"%3A"{}"%7D%7D%2C%7B"type"%3A"terminal'.format(mol)+\
                '"%2C"service"%3A"text"%2C"parameters"%3A%7B"attribute"%3A"rcsb_accession_info.initial_release_date"%2C"'+\
                'operator"%3A"less_or_equal"%2C"negation"%3Afalse%2C"value"%3A"{}"%7D%7D%5D%2C"label"%3A"'.format(date)+\
                'text"%7D%2C"return_type"%3A"entry"%2C"request_options"%3A%7B"paginate"%3A%7B"start"%3A{}%2C"rows'.format(start)+\
                '"%3A{}%7D%2C"results_content_type"%3A%5B"experimental"%5D%2C"sort"%3A%5B%7B"sort_by"%3A"score"%2C"'.format(rows)+\
                'direction"%3A"desc"%7D%5D%2C"scoring_strategy"%3A"combined"%7D%7D'

        x = requests.get("https://search.rcsb.org/rcsbsearch/v2/query?json="+query)

        for row in x.json()["result_set"]:
            print("downloading {}...".format(row['identifier']),end=' ')
            r = requests.get("https://files.rcsb.org/download/{}.cif.gz".format(row['identifier']))
            filename = os.path.join(folder,"{}.cif.gz".format(row['identifier']))
            open(filename, 'wb').write(r.content)
            os.system('gunzip ' + filename)
            print('DONE')
            empty = False

        start += rows
        


if __name__ == "__main__":

    os.makedirs(folder, exist_ok=True)
    DownloadPDB()

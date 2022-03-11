from collections import defaultdict

import numpy as np

from cyvcf2 import VCF

import logging
logging.basicConfig(level=logging.INFO)

t3andme_v3_file = '/home/dan/Downloads/90365083240/' + \
    'genome_Dan_Bolser_v3_Full_20210922075748.txt'

snps_of_interest = [
    'rs2271616', 'rs10490770', 'rs11919389', 'rs1886814', 'rs72711165',
    'rs912805253', 'rs10774671', 'rs1819040', 'rs77534576', 'rs2109069',
    'rs74956615', 'rs4801778', 'rs13050728'
]

# The imputed file is a shortcut we can use re. haplotypes
imputed_vcf_chr_files = []
for chr in [3, 6, 8, 12, 17, 19, 21]:
    imputed_vcf_chr_files.append("/home/dan/Downloads/90365083240/" +
    f"Sanger Imputation Server/hrc-eagle2.vcfs/{chr}.vcf.gz")


logging.info(f"reading file '{t3andme_v3_file}'")
t3andme_snps_by_pos = defaultdict(dict)
t3andme_snps_by_ids = dict()
with open(t3andme_v3_file, 'r') as f:
    for l in f:
        if l[0] == '#':
            continue
        (id, chr, pos, alele) = l.split('\t')

        # Ignoring several can's of worms...
        t3andme_snps_by_pos[chr][int(pos)] = id

        assert id not in t3andme_snps_by_ids
        t3andme_snps_by_ids[id] = [chr, pos]


logging.info(f"converting to numpy for later")
t3andme_snps_np_pos = dict()
for chr, pos in t3andme_snps_by_pos.items():
    t3andme_snps_np_pos[chr] = np.asarray(sorted(pos.keys()))


logging.info(f"opening imputed vcf chromosomes")
imputed_snps_by_pos = defaultdict(dict)
imputed_snps_by_ids = dict()
for f in imputed_vcf_chr_files:
    logging.info(f"opening vcf '{f}'")
    vcf = VCF(f)

    for v in vcf:
        # Fix missing IDs where we can...
        if v.ID is None:
            if v.POS in t3andme_snps_by_pos[v.CHROM]:
                id = t3andme_snps_by_pos[v.CHROM][v.POS]
                logging.debug(f"found missing snp '{id}'")
                v.ID = id
            else:
                continue

        # This is a can of worms (tri-allelic SNPs), see
        # 'debug_imutation_results.py'
        if v.ID in imputed_snps_by_ids:
            imputed_snps_by_ids[v.ID] = None
            continue

        # Ignoring several can's of worms, see
        # 'debug_imutation_results.py'
        imputed_snps_by_pos[v.CHROM][v.POS] = v.ID
        imputed_snps_by_ids[v.ID] = v

    # DEBUGGING
    break


# Get the 10 closest snps to the snps_of_interest
close_snps = defaultdict(list)
for id in snps_of_interest:
    logging.info(f"Finding SNPs close to {id} in the 23andMe v3 array.")

    if id not in imputed_snps_by_ids:
        logging.error(f"MISSING SNP '{id}'")
        continue

    chr = imputed_snps_by_ids[id].CHROM
    pos = imputed_snps_by_ids[id].POS

    logging.info(f"SNP {id} has chromosome {chr}, position {pos}.")

    # Good old numpy arrays
    delta = abs(t3andme_snps_np_pos[chr] - pos)

    min_index = np.argmin(delta)

    for near_idx in range(min_index-5, min_index+5):
        near_pos = t3andme_snps_np_pos[chr][near_idx]
        logging.debug([id, delta[near_idx], near_pos, t3andme_snps_by_pos[chr][near_pos]])

        close_snps[id].append( t3andme_snps_by_pos[chr][near_pos] )



import requests, sys
     
server = "https://rest.ensembl.org"
ext = "/info/variation/populations/homo_sapiens?filter=LD"
     
r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
     
if not r.ok:
     r.raise_for_status()
     sys.exit()
    
decoded = r.json()

for pop in decoded:
    print(pop['name'])


for id1, id2s in close_snps.items():

    print(id1)

    for id2 in id2s:
        print(id2)
        
        for pop in decoded:
            print(f"{pop}")

            if not 'name' in pop:
                continue

            pop = pop['name']
            ext = f"/ld/human/pairwise/{id1}/{id2}?population_name={pop}"

            print(server+ext)
    
            r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
 
            if not r.ok:
                r.raise_for_status()
                sys.exit()
 
            decoded = r.json()
            print(repr(decoded))
            print('')              
        print('')
        print('')
    print('')
    print('')
    print('')
    
